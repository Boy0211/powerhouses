# Code
## Algoritmes
Voor onze case is er gebruikt gemaakt van verschillende algoritmes. Uiteraard
verschillen de resultaten van elk algoritme ten opzichte van elkaar.
Hieronder worden alle gebruikte algoritmen besproken en geanalyseerd.

---
### Greedy 1
Het principe van ons eerste algoritme is relatief simpel. Een while loop
met de lengte van de hoeveelheid huizen, met daarin een for loop. In deze
for loop wordt gekeken welke batterij op dat moment het meeste ruimte overheeft.
Aan deze batterij wordt het eerstvolgende huis toegevoegd waarna deze while loop
wordt herhaald tot dat alle huizen zijn ingedeeld in batterijen.


[Result Greedy 1](/resultaten/Images/Greedy1.png "Hyperlink")  
[Greedy 1](/code/algorithmes/greedy.py "Hyperlink")

> Score: 0.5915492957746479  
> Costs: 73546


### Greedy 2
Het principe van dit algoritme berust voor een deel op dat van greedy 1.
Echter wordt er niet gekeken naar de batterij met de meeste ruimte, maar voor
elk huis naar de dichtsbijzijnde batterij. Wanneer de dichtsbijzijnde batterij
al vol zit wordt er naar de volgende dichtsbijzijnde batterij gekenen als
mogelijk, het huis hieraan toegevoegd.

[Result Greedy 2](/resultaten/Images/Greedy_2.png "Hyperlink")

> Score: 0.885187920825785   
> Costs: 56977

### Random Hillclimber
Nadat er een valide indeling van huizen in batterijen is gemaakt, wordt de
hillclimber toegepast. Deze gaat iteratief opzoek naar een betere oplossing.
Het hillclimber algoritme maakt gebruikt van een swap functie tussen huizen.
Dit algoritme maakt een swap tussen huizen als dat mogelijk is, tot het niet
meer mogelijk is.

[Random Hillclimber + Greedy 2](/resultaten/Images/greedy_2+randomhillclimber.png "Hyperlink")


### Hillclimber
Dit algoritme is een variant op de orginele hillclimber. Het hillclimber
algoritme maakt gebruikt van een swap functie tussen huizen.
Deze swap zal enkel plaatsvinden als dit een gunstig effect heeft op de score.

[Result Hillclimber + Greedy 1](/resultaten/Images/Greedy1+Hillclimber2.png "Hyperlink")

> Score: 0.9360780065005417  
> Costs: 56374

[Result Hillclimber + Greedy 2](/resultaten/Images/greedy_2+hillclimber.png "Hyperlink")

> Score: 0.9206315258431915  
> Costs: 56347


### Random greedy
Dit algoritme probeert compleet random huizen in te delen bij batterijen,
totdat er een valide oplossing is uitgekomen. Oplossinen die niet valide zijn
worden weer verwijderd. Om dit algoritme te laten draaien wordt er een N aantal
oplossingen ingevoerd.
