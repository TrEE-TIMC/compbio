---
layout: page
title: People
subtitle: More about us…
---

{% for post in site.peoples %}
    {% if post.position == "Permanent researcher" %}
        {% include archive-people.html %}
    {% endif %}
{% endfor %}

{% for post in site.peoples %}
    {% if post.position != "Permanent researcher" %}
        {% include archive-people.html %}
    {% endif %}
{% endfor %}



## Interns

- Marina Callandret

## Alumni

Margaux Jullien (2023-2026, postdoc)   
Marion Chauveau (2022-2026, PhD student/postdoc)   
Sophie-Carole Chobert (2021-2025, M2 internet, PhD Student)   
Léa Caruana De Reymonth (2025, M1 intern)  
Arthur Réveillard (2025, M2 intern)  
Hugo Mutschler (2025, M2 intern)  
Timothée Salzat-Hervouette (2024, M2 intern)  
Emma Bouvet (2024, M2 intern)  
Marija Petrovic (2024, L2 intern)  
Elham Ghobadpour (2020-2024, PhD student/postdoc)  
Lucas Etourneau (2021-2024, PhD student)  
Zakaria Tougui (2023, M2 intern)  
Emma Bouvet (2023, M1 intern)  
Abdoulaye Diouma Sow (2023, M2 intern)  
Sophal Thear (2023, M2 intern)  
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
