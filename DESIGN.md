Eindproject Minor Programmeren door Job Huisman
========================================================================================================
Project over azc en politieke voorkeur per gemeente.
--------------------------------------------------------------------------------------------------------

> ## Visualisaties(MVP)(zie schetsen onderaan):
> - bar graph (Politieke partijen)
> - bar graph (opvangcijfers)
> - geographical map (kleur naar gelang grootte ratio opvang/inwoneraantal)
> 
> ## Interactie/ User Interface(MVP)(zie schetsen onderaan):
> - Infovak(linksboven) wanneer hoover over gemeentes (maplocatie; opvang per inwoner)
> - Koppeling aangeklikte plaats aan graphs(2x)
> - zichtbaarheid gemeenten te filteren op inwoneraantal (slidebar)
> 
> ## Extra visualisatie/info
> - Newsfeed (extra vanwege tijdrovende klus om data te verzamelen)
> 
> ## De databronnen:
> - huidige opvang:	Centraal Orgaan Asielzoekers
> - geplande opvang:	https://localfocus2.appspot.com/5613cc9583d28
> - politieke voorkeur:	http://data.weetmeer.nl/gemeente/collection/data/
> - conflicten:		ANP/Nieuwsberichten
> - inwoneraantallen:	cbs statline
> 
> ## Datastructuur:
> Excellfile, omzetten naar csv. Daarin volgende beschikbaar per gemeente:
> - Opvang per inwoner
> - Huidige opvangplekken
> - geplande uitbreidingsaantallen
> - % van de stemmen naar het inwoneraantal per politieke partij tweede kamer verkiezingen 2012
>
> - csv1:
> 	+ gemeente, cbs_code, inwoneraantal, opvangperinwoner, huidigeopvang, geplandeuitbreiding
> - csv2:
>	+ gemeente, cbs_code, %VVD, %CDA, %PvdA, %SP, %SGP, %PVV, %CU, %50Plus, %GroenLinks
> 
> - csv3(optioneel/extra):
>	+ gemeente, nieuwsberichten, nieuwslink
> 
> ## Technische bronnen/middelen:
> - https://commons.wikimedia.org/wiki/File%3ANederland_gemeenten_2014.svg
>	+ code cbs per gemeente voor SVG (cbs="####")
> 
> - python -m http.server 8888 &
> - http://localhost:8888/.
> 
> ## File indeling
> - azc.html
> 	+ bestand welke de verschillende js. files koppelt.
>	+ bevat ook tekst met toelichting
> - azc.css
>	+ opmaak etc.
> - azc_barchart1.js
>	+ data csv1
> - azc_barchart2.js
>	+ data csv2
> - azc_nlgeosvg.js
>	+ data csv1
>
> - azc_news.js
>	+ data csv3
> 
> ## Schets:
> Zie 
>
> ![](doc/overview.png)
> ![](doc/zoom1.png)
> ![](doc/zoom2.png)
> ![](doc/zoom3.png)