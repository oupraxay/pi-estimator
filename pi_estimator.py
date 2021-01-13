##############################################################

# Contributeurs : OUPRAXAY Philippe, TOURE Almamy Moustapha
# 13/01/2021
# Sujet: Estimation de pi avec Spark et Numpy
# Master2 SEP- Eco

##############################################################
import findspark
findspark.init()


# importation des library
import pandas as pd
import numpy as np
import math
from time import time
from random import random
from pyspark import SparkContext, SparkConf

# instanciation de spark
conf = SparkConf().setAppName('Pi-Estimator').setMaster("local")
sc = SparkContext(conf=conf)

 # definition de la fonction de simulation aleaoire
def is_point_inside_unit_circle(p):
    x,y = random(), random()
    return 1 if x*x + y*y < 1 else 0 # verifie si ces deux ponts sont dans le cercle
    
 # verification de la fonction
print(is_point_inside_unit_circle(0))

##estimation de pi avec spark
#1) Definition de la fonction pi_estimator_spark(n)
def pi_estimator_spark(n):
    start_t = time()
    
    # creation d'un RDD 
    count= sc.parallelize(range(0,n)).map(is_point_inside_unit_circle)
    # comptage de point se trouvant à l'interieur 
    inside = count.filter(lambda x: x==1).count()
    
    # Calculer de la valeur de pi_estimator
    
    pi_estimator = (4 * inside /n)
    end_t = time()
    # Determination de la durée de l'operation
    durée = end_t - start_t
    # ecart entre pi
    ecart = (pi_estimator - math.pi)
    return (pi_estimator, durée, ecart)
    
    ##estimation de pi avec numpy
    def pi_estimator_numpy(n):
    start_time = time()
    table = np.zeros((n,1))
    for j in range(0,n) :
        table[j,:] =is_point_inside_unit_circle(1)
    num = np.sum(table)
    
    pi_estimator2 = 4*(num/n)
    end_time = time()
    durée = end_time - start_time
    ecart2 = (pi_estimator2 - math.pi)
    return (pi_estimator2, durée, ecart2)
    
    ##verification
    
    pi_estimator_numpy(100000)
    
    pi_estimator_spark(100000)
    
    # pour n = 1000000
    pi_estimator_numpy(1000000)
    
    pi_estimator_spark(1000000)
    
    # arret de spark en fin de programme
    sc.stop()
