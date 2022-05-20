import numpy as np
import random
random.seed()

gridSize = 9

class Chromosome(object):
    def __init__(self):
        self.values = np.zeros((gridSize, gridSize), dtype=int)
        self.fitness = -100000000000000000
        return

    def fitnessUpdate(self):
        row_count = np.zeros(gridSize)
        column_count = np.zeros(gridSize)
        block_count = np.zeros(gridSize)
        row_sum = 0
        column_sum = 0
        block_sum = 0
        for i in range(0, gridSize):
            for j in range(0, gridSize):
                row_count[self.values[i][j]-1] += 1

            row_sum += (1.0/len(set(row_count)))/gridSize
            row_count = np.zeros(gridSize)

        for i in range(0, gridSize):
            for j in range(0, gridSize):
                column_count[self.values[j][i]-1] += 1

            column_sum += (1.0 / len(set(column_count)))/gridSize
            column_count = np.zeros(gridSize)

        for i in range(0, gridSize, 3):
            for j in range(0, gridSize, 3):
                block_count[self.values[i][j]-1] += 1
                block_count[self.values[i][j+1]-1] += 1
                block_count[self.values[i][j+2]-1] += 1
                
                block_count[self.values[i+1][j]-1] += 1
                block_count[self.values[i+1][j+1]-1] += 1
                block_count[self.values[i+1][j+2]-1] += 1
                
                block_count[self.values[i+2][j]-1] += 1
                block_count[self.values[i+2][j+1]-1] += 1
                block_count[self.values[i+2][j+2]-1] += 1

                block_sum += (1.0/len(set(block_count)))/gridSize
                block_count = np.zeros(gridSize)

        # Calculate overall fitness.
        if (int(row_sum) == 1 and int(column_sum) == 1 and int(block_sum) == 1):
            fitness = 1.0
        else:
            fitness = column_sum * block_sum
        
        self.fitness = fitness
        return
        
    def mutate(self, mutation_rate, given):

        r = np.random.uniform(0, 1)
    
        success = False
        if (r < mutation_rate):
            while(not success):
                row1 = np.random.randint(0, 8)
                row2 = np.random.randint(0, 8)
                row2 = row1
                
                from_column = np.random.randint(0, 8)
                to_column = np.random.randint(0, 8)
                while(from_column == to_column):
                    from_column = np.random.randint(0, 8)
                    to_column = np.random.randint(0, 8)   

                if(given.values[row1][from_column] == 0 and given.values[row1][to_column] == 0):
                    if(not given.is_column_duplicate(to_column, self.values[row1][from_column])
                       and not given.is_column_duplicate(from_column, self.values[row2][to_column])
                       and not given.is_block_duplicate(row2, to_column, self.values[row1][from_column])
                       and not given.is_block_duplicate(row1, from_column, self.values[row2][to_column])):
                    
                        temp = self.values[row2][to_column]
                        self.values[row2][to_column] = self.values[row1][from_column]
                        self.values[row1][from_column] = temp
                        success = True
        return success