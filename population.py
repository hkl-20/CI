from functools import cmp_to_key
import numpy as np
from chromosome import Chromosome
import random
random.seed()

#the value 9, represets the sudoku grid, the value of input digits allowed

def fitnessSort(x, y):
    if(x.fitness < y.fitness):
        return 1
    elif(x.fitness == y.fitness):
        return 0
    else:
        return -1

class Population(object):
    def __init__(self):
        self.chromosomes = []
        return

    def seed(self, Nc, check):
        self.chromosomes = []
        seedInput = Chromosome()
        seedInput.values = [[[] for j in range(0, 9)] for i in range(0, 9)]
        for row in range(0, 9):
            for column in range(0, 9):
                for value in range(1, 10):
                    if(check.values[row][column] == 0):
                        # checking if the value is already in the row, column or block of the puzzle
                        if not ((check.columnDuplicate(column, value) or check.blockDuplicate(row, column, value) or check.rowDuplicate(row, value))):
                            seedInput.values[row][column].append(value)
                    elif(check.values[row][column] != 0):
                        seedInput.values[row][column].append(check.values[row][column])
                        break
       
        for p in range(0, Nc):
            g = Chromosome()
            for i in range(0, 9):
                row = np.zeros(9)
                
                for j in range(0, 9):
                    if(check.values[i][j] != 0):
                        row[j] = check.values[i][j]
                    elif(check.values[i][j] == 0):
                        row[j] = seedInput.values[i][j][random.randint(0, len(seedInput.values[i][j])-1)]

                while(len(list(set(row))) != 9):
                    for j in range(0, 9):
                        if(check.values[i][j] == 0):
                            row[j] = seedInput.values[i][j][random.randint(0, len(seedInput.values[i][j])-1)]

                g.values[i] = row
            self.chromosomes.append(g)
        self.fitnessUpdate()
        print("Seeding complete.")
        return

    def sort(self):
        self.chromosomes.sort(key=cmp_to_key(fitnessSort))
        return
        
    def fitnessUpdate(self):
        # Calculate fitness for each chromosome.
        for chromosome in self.chromosomes:
            chromosome.fitnessUpdate()
        return