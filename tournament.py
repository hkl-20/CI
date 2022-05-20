import numpy as np
import random
from population import Population
random.seed()

class Tournament(object):
    def __init__(self):
        return
        
    def compete(self, chromosomes):
        c1 = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        c2 = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        sel1,sel2 = c1.fitness, c2.fitness

        if(sel1 > sel2):
            fittest, weakest = c1, c2
        else:
            fittest, weakest = c2, c1 

        rndNum = np.random.uniform(0, 1)
        selection_rate = 0.80

        if(rndNum < selection_rate):
            return fittest
        else:
            return weakest

