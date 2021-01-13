# pi-estimator
Dans ce projet, nous cherchons la valeur de Pi avec le processus Spark et Numpy. 
Nous comparons les performances de ces processus pour n = 100 000 et n= 1 000 000


 Pour n=100000       | Spark                 |        Numpy       |
| :-----------------: |:-------------------: | :-----------------:|
| Temps d'exécution  | 1.619 Secondes       | 0.134 Secondes     |
| Valeur de Pi       | 3.14572               | 3.1442            |
| Ecart % Math.pi    | 0.0041             | 0.0026         |

 Pour n=100000       | Spark                 |        Numpy       |
| :-----------------: |:-------------------: | :-----------------:|
| Temps d'exécution  | 2.4942  Secondes       |1.0621 Secondes     |
| Valeur de Pi       | 3.13956              | 3.1425           |
| Ecart % Math.pi    | -0.002            | 0.0009         |



