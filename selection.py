import numpy as np
import random
from population import Population
random.seed()

class Tournament(object):
    def __init__(self):
        return
        
    def compete(self, chromosomes):
        a = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        b = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        sel1,sel2 = a.fitness, b.fitness
        #       Truncation tried but had some issues
        #       if(sel1 > sel2):
        #           return Population.sort(self)[:chromosomes]
        #       else:
        #           return Population.sort(self)[-chromosomes:]
        fittest, weakest = a, b
        if(sel1 < sel2):
            fittest, weakest = b, a

        selectionRate = 0.8
        if(np.random.uniform(0, 1) < selectionRate):
            return fittest
        else:
            return weakest



