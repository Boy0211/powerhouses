# Code
## Algoritmes
Voor onze case is er gebruikt gemaakt van iteratief, population baed and cluster
algoritmes. Uiteraard verschillen de resultaten van elk algoritme ten opzichte
van elkaar. Hieronder worden alle gebruikte algoritmen besproken en geanalyseerd.

### Analyse Algoritmes

Op basis van onze huidige bevindingen komt de PPA het beste uit de kast. De PPA
werkt wel alleen met bestaande oplossingen waardoor het gebruik van een simpele
greedy of een greedy gevolgd door een hillClimber onvermijdelijk is. De PPA
zorgt door zijn mogelijkheid veel verschillende veranderingen toe te passen voor
een hoge verscheidenheid aan oplossing die vervolgens weer geoptimaliseerd
worden. 

---
### Greedy capacity
Het principe van ons eerste algoritme is het indelen op basis van capaciteit.
Een while loop met de lengte van de hoeveelheid huizen, met daarin een for loop.
In deze for loop wordt gekeken welke batterij op dat moment het meeste ruimte
overheeft. Aan deze batterij wordt het eerstvolgende huis toegevoegd waarna
deze while loop wordt herhaald tot dat alle huizen zijn ingedeeld in batterijen.
Greedy 1 en greedy 2 staan in hetzelfde python bestand maar zijn 2 aparte
functies.  


[Result Greedy capacity](/resultaten/Images/Greedy1.png "Hyperlink")  
[Greedy Algoritme](/code/algorithmes/greedy.py "Hyperlink")

> Wijk 1:  
> Score: 0.5915492957746479  
> Costs: 73546


### Greedy distance
Het principe van dit algoritme berust voor een deel op dat van greedy 1.
Echter wordt er niet gekeken naar de batterij met de meeste ruimte, maar voor
elk huis naar de dichtsbijzijnde batterij. Wanneer de dichtsbijzijnde batterij
al vol zit wordt er naar de volgende dichtsbijzijnde batterij gekeken. Wanneer
het mogelijk is wordt het huis hieraan toegevoegd. Dit herhaalt zich tot alle
huizen geplaats zijn.  

[Result Greedy distance](/resultaten/Images/Greedy_2.png "Hyperlink")  
[Greedy Algoritme](/code/algorithmes/greedy.py "Hyperlink")

> Wijk 1:  
> Score: 0.9207295052365475   
> Costs: 57139


### Hillclimber
Dit algoritme is een variant op de orginele hillclimber. Het hillclimber
algoritme maakt gebruikt van een swap functie tussen huizen. Echter verschilt
deze hillclimber ten opzichte van de eerdere hillclimber, in dat deze
hillclimber op zoek gaat naar de beste swap en deze uitvoert.


[Result Hillclimber + Greedy capacity](/resultaten/Images/Greedy1+Hillclimber2.png "Hyperlink")  
[Hillclimber Algoritme](/code/algorithmes/hillclimber.py "Hyperlink")

> Wijk 1:  
> Score: 0.9360780065005417  
> Costs: 56374

[Result Hillclimber + Greedy distance](/resultaten/Images/greedy_2+hillclimber.png "Hyperlink")  
[Hillclimber Algoritme](/code/algorithmes/hillclimber.py "Hyperlink")

> Wijk 1:  
> Score: 0.9206315258431915  
> Costs: 56347


### Random greedy
Dit algoritme probeert compleet random huizen in te delen bij batterijen,
totdat er een valide oplossing is uitgekomen. Een valide oplossing houdt in dat
de capaciteit in alle batterijen niet wordt overschreden en alle huizen zijn
ingeeld. Oplossinen die niet valide zijn worden weer verwijderd. Om dit
algoritme te laten draaien wordt er een N aantal runs ingevoerd.  

[Random Algoritme](/code/algorithmes/random_greedy.py "Hyperlink")


### Random Hillclimber
Nadat er een valide indeling van huizen in batterijen is gemaakt door een van
de eerdere greedy algoritmes, wordt de hillclimber toegepast. Deze gaat
iteratief opzoek naar een betere oplossing. Het hillclimber algoritme maakt
gebruikt van een swap tussen huizen om zo een betere score te verkrijgen.
Een swap is een wissel van twee random huizen in twee random batterijen.
Dit algoritme maakt een swap tussen huizen als de capaciteit van beide
batterijen dat toe laat. Mits dit de score bevorderd, gebeurd dit net zo lang
totdat het niet meer mogelijk is.

[Random Hillclimber + Greedy distance](/resultaten/Images/greedy_2+randomhillclimber.png "Hyperlink")  
[Random Hillclimber Algoritme](/code/algorithmes/randomHillclimber.py "Hyperlink")

> resultaten: [Random](/powerhouses/resultaten/random greedy + random hc n = 10,000.png "Hyperlink")

### Plant Propagation algorithm voor stationaire batterijen

[link naar bestand]

Bij het plant propagation algoritm (PPA) wordt er gebruik gemaakt van het
concept van de aarbei plant. De aarbei plant plant zich zelf voor door wanneer
hij in vruchtbare grond zich snel uit te breiden, maar wanneer hij daar niet zit
lange wortels er op uit te sturen opzoek naar vruchtbare grond.

De PPA gebruikt in ons geval dit concept.

Op basis van de score gegenereerd in de solution class, bepaalt het algoritme
of er een 'long runner' of een 'short runner' nodig is. Hoe dichter de score
bij de optimale score zit, hoe shorter de runner

> UITSLAGEN VOLGEN

### Plant Propagation algorithm voor beweeglijke batterijen

[link naar bestand]

Dit algoritme is op het zelfde concept gebasseerd als die voor stationaire
batterijen. Nu is een van de mogelijke runners ook nog het verplaatsen van
batterijen.

> Wijk 1:  
> Score: 0.9995391062455254
> Costs: 40354