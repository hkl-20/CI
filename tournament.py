import numpy as np
import random
random.seed()

class Tournament(object):
    def __init__(self):
        return
        
    def compete(self, chromosomes):
        c1 = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        c2 = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        f1 = c1.fitness
        f2 = c2.fitness

        if(f1 > f2):
            fittest = c1
            weakest = c2
        else:
            fittest = c2
            weakest = c1

        rndNum = np.random.uniform(0, 1)
        selection_rate = 0.85

        if(rndNum < selection_rate):
            return fittest
        else:
            return weakest