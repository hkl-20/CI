import numpy as np
import random
random.seed()

class Chromosome(object):
    def __init__(self):
        grid = (9, 9)
        self.values = np.zeros(grid, dtype=int)
        self.fitness = -100000000000000000
        return

    def mutate(self, mutationRate, check):

        rndNum = np.random.uniform(0, 1)
        isMutated = False
        if (rndNum < mutationRate):
            while(not isMutated):
                rowStart = np.random.randint(0, 8)
                rowEnd = rowStart
                
                columnStart = np.random.randint(0, 8)
                columnEnd = np.random.randint(0, 8)
                while(columnStart == columnEnd):
                    columnStart = np.random.randint(0, 8)
                    columnEnd = np.random.randint(0, 8)   

                    if(check.values[rowStart][columnStart] == 0 and check.values[rowStart][columnEnd] == 0):
                        if(not check.columnDuplicate(columnEnd, self.values[rowStart][columnStart])
                        and not check.columnDuplicate(columnStart, self.values[rowEnd][columnEnd])):
                            temp = self.values[rowEnd][columnEnd]
                            self.values[rowEnd][columnEnd] = self.values[rowStart][columnStart]
                            self.values[rowStart][columnStart] = temp
                            isMutated = True

                        elif (not check.rowDuplicate(rowEnd, self.values[rowStart][columnStart])
                        and not check.rowDuplicate(rowStart, self.values[rowEnd][columnEnd])):
                    
                            temp = self.values[rowEnd][columnEnd]
                            self.values[rowEnd][columnEnd] = self.values[rowStart][columnStart]
                            self.values[rowStart][columnStart] = temp
                            isMutated = True
        return isMutated

    def fitnessUpdate(self):

        sumOfRows = 0
        totalRow = np.zeros(9)
        for i in range(0, 9):
            for j in range(0, 9):
                totalRow[self.values[i][j]-1] += 1

            sumOfRows += (1.0/len(set(totalRow)))/9
            totalRow = np.zeros(9)

        sumOfColumns = 0
        totalColumn = np.zeros(9)
        for i in range(0, 9):
            for j in range(0, 9):
                totalColumn[self.values[j][i]-1] += 1

            sumOfColumns += (1.0 / len(set(totalColumn)))/9
            totalColumn = np.zeros(9)
        
        sumOfBlocks = 0
        totalBlock = np.zeros(9)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                x = 0
                for k in range(0, 3):
                    y = 0
                    for l in range(0, 3):
                        totalBlock[self.values[i+x][j+y]-1] += 1
                        y += 1
                    x += 1

                sumOfBlocks += (1.0/len(set(totalBlock)))/9
                totalBlock = np.zeros(9)

        # Calculate overall fitness.
        if (int(sumOfRows) == 1):
            fitness = 1.0
        elif (int(sumOfColumns) == 1):
            fitness = 1.0
        elif (int(sumOfBlocks) == 1):
            fitness = 1.0
        else:
            fitness = sumOfColumns * sumOfBlocks
        
        self.fitness = fitness
        return
        