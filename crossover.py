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

    def crossover_rows(self, rowStart, rowEnd): 
        child_rowStart = np.zeros(9)
        child_rowEnd = np.zeros(9)
        remaining = list(range(1, 9+1))
        cycle = 0
        
        while((0 in child_rowStart) and (0 in child_rowEnd)):
            if(cycle % 2 == 0): 
                index = self.find_unused(rowStart, remaining)
                start = rowStart[index]
                remaining.remove(rowStart[index])
                child_rowStart[index] = rowStart[index]
                child_rowEnd[index] = rowEnd[index]
                next = rowEnd[index]
                
                while not(next == start): 
                    index = self.find_value(rowStart, next)
                    child_rowStart[index] = rowStart[index]
                    remaining.remove(rowStart[index])
                    child_rowEnd[index] = rowEnd[index]
                    next = rowEnd[index]
                cycle += 1

            elif (cycle % 2 != 0):
                index = self.find_unused(rowStart, remaining)
                start = rowStart[index]
                remaining.remove(rowStart[index])
                child_rowStart[index] = rowEnd[index]
                child_rowEnd[index] = rowStart[index]
                next = rowEnd[index]
                
                while not(next == start):
                    index = self.find_value(rowStart, next)
                    child_rowStart[index] = rowEnd[index]
                    remaining.remove(rowStart[index])
                    child_rowEnd[index] = rowStart[index]
                    next = rowEnd[index]
                    
                cycle += 1
            
        return child_rowStart, child_rowEnd  
           
    def find_unused(self, parent_row, remaining):
        for i in range(0, len(parent_row)):
            if(parent_row[i] in remaining):
                return i

    def find_value(self, parent_row, value):
        for i in range(0, len(parent_row)):
            if(parent_row[i] == value):
                return i
