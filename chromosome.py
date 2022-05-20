import numpy as np
import random
random.seed()

class Chromosome(object):
    def __init__(self):
        grid = (9, 9)
        self.values = np.zeros(grid, dtype=int)
        self.fitness = -100000000000000000
        return

    def fitnessUpdate(self):
        row_count = np.zeros(9)
        column_count = np.zeros(9)
        block_count = np.zeros(9)
        row_sum = 0
        column_sum = 0
        block_sum = 0
        for i in range(0, 9):
            for j in range(0, 9):
                row_count[self.values[i][j]-1] += 1

            row_sum += (1.0/len(set(row_count)))/9
            row_count = np.zeros(9)

        for i in range(0, 9):
            for j in range(0, 9):
                column_count[self.values[j][i]-1] += 1

            column_sum += (1.0 / len(set(column_count)))/9
            column_count = np.zeros(9)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                x = 0
                for k in range(0, 3):
                    y = 0
                    for l in range(0, 3):
                        block_count[self.values[i+x][j+y]-1] += 1
                        y += 1
                    x += 1

                block_sum += (1.0/len(set(block_count)))/9
                block_count = np.zeros(9)

        # Calculate overall fitness.
        if (int(row_sum) == 1 and int(column_sum) == 1 and int(block_sum) == 1):
            fitness = 1.0
        else:
            fitness = column_sum * block_sum
        
        self.fitness = fitness
        return
        
    def mutate(self, mutationRate, check):

        rndNum = np.random.uniform(0, 1)
        isMutated = False
        if (rndNum < mutationRate):
            while(not isMutated):
                row1 = np.random.randint(0, 8)
                row2 = np.random.randint(0, 8)
                row2 = row1
                
                from_column = np.random.randint(0, 8)
                to_column = np.random.randint(0, 8)
                while(from_column == to_column):
                    from_column = np.random.randint(0, 8)
                    to_column = np.random.randint(0, 8)   

                    if(check.values[row1][from_column] == 0 and check.values[row1][to_column] == 0):
                        if(not check.columnDuplicate(to_column, self.values[row1][from_column])
                        and not check.columnDuplicate(from_column, self.values[row2][to_column])
                        and not check.rowDuplicate(row2, self.values[row1][from_column])
                        and not check.rowDuplicate(row1, self.values[row2][to_column])):
                    
                            temp = self.values[row2][to_column]
                            self.values[row2][to_column] = self.values[row1][from_column]
                            self.values[row1][from_column] = temp
                            isMutated = True
        return isMutated