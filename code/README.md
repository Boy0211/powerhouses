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

[Result Visualized](/resultaten/Images/Screen Shot 2018-12-06 at 17.30.40.png "Hyperlink")


### Greedy 2
Het principe van dit algoritme berust voor een deel op dat van greedy 1.
Echter wordt er niet gekeken naar de batterij met de meeste ruimte, maar voor
elk huis naar de dichtsbijzijnde batterij. Wanneer de dichtsbijzijnde batterij
al vol zit wordt er naar de volgende dichtsbijzijnde batterij gekenen als
mogelijk, het huis hieraan toegevoegd.
[Link]

### Hillclimber
Nadat er een valide indeling van huizen in batterijen is gemaakt, wordt de
hillclimber toegepast. Deze gaat iteratief opzoek naar een betere oplossing.
Het hillclimber algoritme maakt gebruikt van een swap functie tussen huizen.
Deze swap zal enkel plaatsvinden als dit een gunstig effect heeft op de score.
[Link]

### Random Hillclimber
Dit algoritme is een variant op de orginele hillclimber. Het principe
is hetzelfde er op een eerdere valide oplossing swaps worden toegepast om
zo een betere nieuwe oplossing te creeëren. Maar het verschil zit erin dat dit
algoritme blijft swappen tot het niet meer mogelijk is. XXXXX
[Link]

### Random greedy
Dit algoritme genereert random geldige uitkomsten aan de hand van greedy 1.
Dit betekend dat een x aantal resultaten uitkomen door het greedy 1 algoritme
een x aantal keer te laten draaien. Het beste resultaat hiervan wordt telkens
opgeslagen.
[Link]
