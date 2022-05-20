import numpy as np
import random
from population import Population
random.seed()

# class Tournament(object):
#     def __init__(self):
#         return
        
#     def compete(self, chromosomes):
        # a = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        # b = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        # sel1,sel2 = a.fitness, b.fitness

        # if(sel1 > sel2):
#             fittest, weakest = a, b
#         else:
#             fittest, weakest = b, a 

#         rndNum = np.random.uniform(0, 1)
#         selection_rate = 0.80

#         if(rndNum < selection_rate):
#             return fittest
#         else:
#             return weakest

class Tournament(object):
    def __init__(self):
        return
    def compete(self, chromosomes): 
        a = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        b = chromosomes[np.random.randint(0, len(chromosomes)-1)]
        sel1,sel2 = a.fitness, b.fitness
        if(sel1 > sel2):
            return self.Population.sort()[:chromosomes]
        else:
            return self.Population.sort()[-chromosomes:]
