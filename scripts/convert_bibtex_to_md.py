import argparse
import os
import bibtexparser

parser = argparse.ArgumentParser()
parser.add_argument(
    "filename",
    help="Path to file containing bibtex formatted references")
parser.add_argument(
    "output_dir",
    help="Path to the output directory")
args = parser.parse_args()

filename = args.filename
output_dir = args.output_dir

with open(filename) as bibtex_file:
    bib_database = bibtexparser.bparser.BibTexParser(
        common_strings=True).parse_file(bibtex_file)


def get_authors(citation, format="only_last_name"):
    authors = citation["author"].split(" and ")
    authors = [a.split(", ") for a in authors]

    if format == "only_last_name":
        authors = [a[0] for a in authors]
    elif format == "abbrvnat":
        authors = [create_initials(a) for a in authors]
        authors = [" ".join([a[1], a[0]]) for a in authors]
    else:
        raise ValueError(
            "Unknown format. Please specify one of ['only_last_name']")
    return authors


def create_initials(author):
    # Start by splitting first names
    first_names = author[1].split(" ")
    # Then initialize by dealing with hyphenated names
    initialized_first_name = []
    for first_name in first_names:
        initialized_first_name.append(
            "-".join([s[0] + "." for s in first_name.split("-")]))
    initialized_first_name = " ".join(initialized_first_name)
    author[1] = initialized_first_name
    return author


def create_filename(citation):
    authors = get_authors(citation)[:4]
    # Ok… Let's just remove anything non alphanumerical which is a bit
    # annoying for people with special characters in their name but will save
    # us some trouble later on.
    authors = ["".join(filter(str.isalnum, a)) for a in authors]
    filename = citation["year"] + "-" + "_".join(authors) + ".md"
    return filename


def format_citation(citation, max_authors=4):
    authors = get_authors(citation, format="abbrvnat")
    et_al = ""
    if len(authors) > 4:
        authors = authors[:4]
        et_al = " <i>et al.</i>"
    authors = ", ".join(authors) + et_al
    title = citation["title"].replace("{", "").replace("}", "")
    try:
        journal = citation["journal"] + ","
    except KeyError:
        journal = ""

    try:
        url = citation["url"]
    except KeyError:
        url = ""

    try:
        month = citation["month"].capitalize() + " "
    except KeyError:
        month = ""

    try:
        year = citation["year"]
    except KeyError:
        year = ""

    if url:
        formatted_citation = (
            "<a href=\"{url}\">{authors}. <b>{title}</b>, <i>{journal}</i>"
            " {month}{year}</a>").format(
                url=url,
                authors=authors,
                title=title,
                journal=journal,
                month=month,
                year=year)
    else:
        formatted_citation = (
            "{authors}. <b>{title}</b>, <i>{journal}</i>"
            " {month}{year}").format(
                authors=authors,
                title=title,
                journal=journal,
                month=month,
                year=year)
    return formatted_citation


try:
    os.makedirs(output_dir)
except OSError:
    pass

for citation in bib_database.entries:
    # Clean up title name

    citation["title"] = citation["title"].replace("{", "").replace("}", "")
    try:
        note = citation["note"]
        note = note.replace(r"\_", "_")
        note = note + "\n"
    except KeyError:
        note = ""

    # create the filename
    filename = create_filename(citation).lower() 
    formatted_citation = format_citation(citation)
    print(filename)
    md = "---\n"
    md = md + "title: " + '"' + citation["title"] + '"' + "\n"
    md = md + "collection: publications\n"
    md = md + "permalink: /publication/" + filename.split(".md")[0].lower() + "\n"
    md = md + "venue: ''\n"
    md = md + "citation: '" + formatted_citation + "'\n"
    md = md + note
    md = md + "---\n"

    with open(os.path.join(output_dir, filename), "w") as f:
        f.write(md)
