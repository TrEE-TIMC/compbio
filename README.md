# HOW TO update stuff on our wonderful website

* Log into your github account and make sure the computer you are on has been listed through a ssh key
* Clone the repo:

`git clone git@github.com:TrEE-TIMC/compbio.git`


Now the fun can start!

NB: if you want to avoid to enter your SSH passphrase upon each action, you can used `ssh-add` once and for all on your computer.


So then the process is:
- make changes to the site
- push
- take a coffee!
- look at the webpage!


To be noted:
* Index page is HTML
* The rest are markdown pages. See [here for a cheat sheet.](https://www.markdownguide.org/cheat-sheet/)
* Stored files are in the **files** folder
* Publications are automatically listed from the **_publications** folder via the publications.md file.


## Adding publications

The template is the following:


	---
	title: "Identification of protein secretion systems in bacterial genomes"
	collection: publications
	permalink: /publication/2016-abby_curry
	venue: Scientific Reports
	citation: '<b>Abby, S.</b>, Cury, J., Guglielmini, J., Néron, B., Touchon, M., and
	Rocha, E. (2016). Identification of protein secretion systems in bacterial
	genomes. <i> Scientific Reports</i>,'
	oa_paperurl: https://www.nature.com/articles/srep23080
	githuburl: 'https://github.com/gem-pasteur/macsyfinder'
	year: 2016
	---

If you are lazy and would like to create these automatically, please follow
instructions from [scripts/README.md](https://github.com/TrEE-TIMC/compbio/blob/gh-pages/scripts/README.md)
