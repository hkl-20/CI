from chromosome import Chromosome
import numpy as np
import random
random.seed()

class Crossover(object):
    def __init__(self):
        return
    
    def crossover(self, parent1, parent2, crossoverRate):
        child1 = Chromosome()
        child2 = Chromosome()
        
        child1.values = np.copy(parent1.values)
        child2.values = np.copy(parent2.values)

        rndNum = np.random.uniform(0, 1)
            
        if (rndNum < crossoverRate):
            crossover_point1 = np.random.randint(0, 8)
            crossover_point2 = np.random.randint(1, 9)

            while(crossover_point1 == crossover_point2):
                crossover_point2 = np.random.randint(1, 9)
                crossover_point1 = np.random.randint(0, 8)
                if(crossover_point1 > crossover_point2):
                    crossover_point1, crossover_point2 = crossover_point2, crossover_point1
                    
            for i in range(crossover_point1, crossover_point2):
                child1.values[i], child2.values[i] = self.crossover_rows(child1.values[i], child2.values[i])
        return child1, child2

    def crossover_rows(self, row1, row2): 
        child_row1 = np.zeros(9)
        child_row2 = np.zeros(9)
        remaining = list(range(1, 9+1))
        cycle = 0
        
        while((0 in child_row1) and (0 in child_row2)):
            if(cycle % 2 == 0): 
                index = self.find_unused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                child_row1[index] = row1[index]
                child_row2[index] = row2[index]
                next = row2[index]
                
                while not(next == start): 
                    index = self.find_value(row1, next)
                    child_row1[index] = row1[index]
                    remaining.remove(row1[index])
                    child_row2[index] = row2[index]
                    next = row2[index]
                cycle += 1

            elif (cycle % 2 != 0):
                index = self.find_unused(row1, remaining)
                start = row1[index]
                remaining.remove(row1[index])
                child_row1[index] = row2[index]
                child_row2[index] = row1[index]
                next = row2[index]
                
                while not(next == start):
                    index = self.find_value(row1, next)
                    child_row1[index] = row2[index]
                    remaining.remove(row1[index])
                    child_row2[index] = row1[index]
                    next = row2[index]
                    
                cycle += 1
            
        return child_row1, child_row2  
           
    def find_unused(self, parent_row, remaining):
        for i in range(0, len(parent_row)):
            if(parent_row[i] in remaining):
                return i

    def find_value(self, parent_row, value):
        for i in range(0, len(parent_row)):
            if(parent_row[i] == value):
                return i
