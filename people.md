---
layout: page
title: People
subtitle: More about us…
---

## Permanent staff

{% for post in site.peoples %}
    {% if post.position == "Permanent researcher" %}
        {% include archive-people.html %}
    {% endif %}
{% endfor %}

## Postdoctoral researcher

{% for post in site.peoples %}
    {% if post.position == "postdoc" %}
        {% include archive-people.html %}
    {% endif %}
{% endfor %}


## PhD students

{% for post in site.peoples %}
    {% if post.position == "phd_student" %}
        {% include archive-people.html %}
    {% endif %}
{% endfor %}


## Interns

- **Sophal Lear** (M2 intern, supervised by [Sophie
  Abby](https://sophieabby.github.io/) and [Nelle
  Varoquaux](https://nellev.github.io))
- **Abdoulaye Diouma Sow** (M2 intern, supervised by [Sophie
  Abby](https://sophieabby.github.io/) and [Nelle
  Varoquaux](nellev.github.io))
- **Zakaria Tougui**  (M2 intern, supervised by [Antoine
  Frenoy](https://perso.crans.org/frenoy/) and [Nelle
  Varoquaux](https://nellev.github.io))
- **Emma Bouvet** (M1 intern, supervised by [Sophie
  Abby](https://sophieabby.github.io/), Margaux Jullien 
  and Ludovic Pelosi)

## Alumni

Claudia Mulat (2023, L1 intern)  
Mathilde Escleyne (2023, L2 intern)  
Fatoumata Mangane (2023, M2 intern)  
Suraj Kanwar (2023, M1 intern)  
Benoit Sauret (2022, M2 intern)  
Duc-Anh Do (2022, intern)  
Flora Gaudillière (2021, intern)  
Renato Augusto Antoniassi Battistin (2021, M1 intern)  
Vu-Lam Dang (2021, intern)  
William Schmitt (2021, PhD student)  
Qiqi He (2020, M2 intern)  
Safa Berraies (2019, M2 intern)  
Morgane Roger-Margueritat (2019&2022, L3&M2 intern)  
Clothilde Chenal (2018, L3 intern)  
Brian Villette (2018, intern)  
Judith Boldt (2016, intern)  
Loic Duquennoy (2016, intern)  
Thibaut Lepage (2015-2017, postdoc)
