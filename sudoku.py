from functools import cmp_to_key
import numpy as np
import random
from chromosome import Chromosome
from population import Population
from tournament import Tournament
from crossover import CycleCrossover
random.seed()

sudokuGrid = 9

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
        i = 3*(int(row/3))
        j = 3*(int(column/3))

        for x in range(3):
            for y in range(3):
                if(self.values[i+x][j+y] == value):
                    return True
        return False

class Sudoku(object):
    def __init__(self):
        self.check = None
        return
    
    def load(self, path):
        with open(path, "r") as f:
            sudokuGrid = (9, 9)
            values = np.loadtxt(f).reshape(sudokuGrid).astype(int)
            self.check = Check(values)
        return

    def save(self, path, solution):
        with open(path, "w") as f:
            np.savetxt(f, solution.values.reshape(9*9), fmt='%d')
        return
        
    def solve(self):
        Nc = 1000
        Ne = int(0.05*Nc)
        Ng = 1000
        Nm = 0

        phi = 0
        sigma = 1
        mutation_rate = 0.06

        self.population = Population()
        self.population.seed(Nc, self.check)

        stale = 0
        for generation in range(0, Ng):
        
            print("Generation %d" % generation)

            best_fitness = 0.0
            for c in range(0, Nc):
                fitness = self.population.chromosomes[c].fitness
                if(fitness == 1):
                    print("Solution found at generation %d!" % generation)
                    print(self.population.chromosomes[c].values)
                    return self.population.chromosomes[c]

                if(fitness > best_fitness):
                    best_fitness = fitness

            print("Best Fitness - %f" % best_fitness)

            self.population.sort()
            elites = []
            for e in range(0, Ne):
                elite = Chromosome()
                elite.values = np.copy(self.population.chromosomes[e].values)
                elites.append(elite)

            next_population = []
            for count in range(Ne, Nc, 2):
                t = Tournament()
                parent1 = t.compete(self.population.chromosomes)
                parent2 = t.compete(self.population.chromosomes)
                
                cc = CycleCrossover()
                child1, child2 = cc.crossover(parent1, parent2, crossover_rate=1.0)

                old_fitness = child1.fitness
                success = child1.mutate(mutation_rate, self.check)
                child1.fitnessUpdate()
                if(success):
                    Nm += 1
                    if(child1.fitness > old_fitness):
                        phi = phi + 1

                old_fitness = child2.fitness
                success = child2.mutate(mutation_rate, self.check)
                child2.fitnessUpdate()
                if(success):
                    Nm += 1
                    if(child2.fitness > old_fitness):
                        phi = phi + 1
                
                next_population.append(child1)
                next_population.append(child2)

            for e in range(0, Ne):
                next_population.append(elites[e])

            self.population.chromosomes = next_population
            self.population.fitnessUpdate()
            
            if(Nm == 0):
                phi = 0
            else:
                phi = phi / Nm
            
            if(phi > 0.2):
                sigma = sigma/0.998
            elif(phi < 0.2):
                sigma = sigma*0.998

            mutation_rate = abs(np.random.normal(loc=0.0, scale=sigma, size=None))
            Nm = 0
            phi = 0

            self.population.sort()
            if(self.population.chromosomes[0].fitness != self.population.chromosomes[1].fitness):
                stale = 0
            else:
                stale += 1

            if(stale >= 100):
                print("The population has gone stale. Re-seeding...")
                self.population.seed(Nc, self.check)
                stale = 0
                sigma = 1
                phi = 0
                Nm = 0
                mutation_rate = 0.06
        return None
