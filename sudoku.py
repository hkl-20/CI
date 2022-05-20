import numpy as np
import random

from chromosome import Chromosome
from population import Population
from selection import Tournament
from crossover import Crossover

random.seed()

class Check(Chromosome):
    def __init__(self, values):
        self.values = values
        return
        
    def rowDuplicate(self, row, value):
        for column in range(0, 9):
            if(self.values[row][column] == value):
               return True
        return False

    def columnDuplicate(self, column, value):
        for row in range(0, 9):
            if(self.values[row][column] == value):
               return True
        return False

    def blockDuplicate(self, row, column, value):
        r = 3*(int(row/3))
        c = 3*(int(column/3))

        for x in range(3):
            for y in range(3):
                if(self.values[r+x][c+y] == value):
                    return True
        return False

class Sudoku(object):
    def __init__(self):
        self.check = None
        return
        
    def solve(self):
        phi = 0
        sigma = 1
        mutation_rate = 0.06
        crossoverRate = 0.8
        mutations = 0

        popSize = 1000
        numElite = int(0.05*popSize)
        gens = 1000

        self.population = Population()

        self.population.seed(popSize, self.check)

        for generation in range(0, gens):

            bestFitness = 0.0
            for i in range(0, popSize):
                fitness = self.population.chromosomes[i].fitness
                if(fitness == 1):
                    print("Generation %d" % generation)
                    print("Congratulations! The solution was found at ", generation," generation!")
                    print(self.population.chromosomes[i].values)
                    return self.population.chromosomes[i]

                if(fitness > bestFitness):
                    bestFitness = fitness

            print("Total Generations: ",generation, ":: Best Fitness - ", bestFitness)

            self.population.sort()
            elites = []

            for i in range(0, numElite):
                elite = Chromosome()
                elite.values = np.copy(self.population.chromosomes[i].values)
                elites.append(elite)

            next_population = []
            for count in range(numElite, popSize, 2):

                tournament = Tournament()
                parent1 = tournament.compete(self.population.chromosomes)
                parent2 = tournament.compete(self.population.chromosomes)
                
                cross = Crossover()
                child1, child2 = cross.crossover(parent1, parent2, crossoverRate)

                for x in child1, child2: 
                    prevFitness = x.fitness
                    isMutated = x.mutate(mutation_rate, self.check)
                    x.fitnessUpdate()
                    if(isMutated):
                        mutations += 1
                        if(prevFitness < x.fitness):
                            phi = phi + 1
                
                next_population.append(child1)
                next_population.append(child2)

            for e in range(0, numElite):
                next_population.append(elites[e])

            self.population.chromosomes = next_population
            self.population.fitnessUpdate()
            
            phi = phi / mutations
            if(mutations == 0):
                phi = 0
            
            sigma = sigma*0.996
            if(phi > 0.2):
                sigma = sigma/0.996
            
            mutations = 0
            phi = 0
            mutation_rate = abs(np.random.normal(loc=0.0, scale=sigma, size=None))
        return None

    def save(self, path, solution):
        with open(path, "w") as f:
            np.savetxt(f, solution.values.reshape(9*9), fmt='%d')
        return
    
    def load(self, path):
        with open(path, "r") as f:
            sudokuGrid = (9, 9)
            values = np.loadtxt(f).reshape(sudokuGrid).astype(int)
            self.check = Check(values)
        return
