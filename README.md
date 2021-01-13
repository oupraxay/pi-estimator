# pi-estimator
Dans ce projet, nous cherchons la valeur de Pi avec le processus Spark et Numpy. 
Nous comparons les performances de ces processus pour n = 100 000 et n= 1 000 000

n=100000	SPARK	NUMPY
temps d'exécution	1,619	0,134
valeurs de pi	3,14572	3,1442
écart % Math.pi	0,0041	0,0026
		
		
n=1000000	SPARK	NUMPY
temps d'exécution	2,4942	1,0621
valeurs de pi	3,13956	3,1425
écart % Math.pi	-0,002	0,0009

 Pour n=100000       | Spark                 |        Numpy       |
| :-----------------: |:-------------------: | :-----------------:|
| Temps d'exécution  | 1.152  Secondes       | 0.128 Secondes     |
| Valeur de Pi       | 3.14136               | 3.13512            |
| Ecart % Math.pi    | -0.000232             | -0.00647           |

