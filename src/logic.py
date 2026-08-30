from trick_data import ACCEPTABLE_STANCES, TRICKS
import random


class GeneticAlgorithm:
    def __init__(self):
        pass

    def start_ga(self, num_of_tricks, population_size, breeding_pool, crossover_rate, mutation_rate):
        self.population = []

        for _ in range(population_size):
            line = []

            for _ in range(num_of_tricks):
                line.append(random.choice(list(TRICKS)))
            self.population.append(line)

        generation = 1
        # best_fitness = 0
        # gens_without_improvement = 0

        while True:
            self.fitness()
            self.selection()

            # code for gens without improvement

            # display generation

            # breaking the loop

            self.crossover()
            self.mutation()

            generation += 1

    def fitness(self):
        self.fitness_scores = []

        for line in self.population:
            score = 0

            unique_difficulties = set()
            unique_tricks = set()

            for trick in line:
                unique_difficulties.add(TRICKS[trick]['difficulty'])
                unique_tricks.add(trick)
            score += len(unique_difficulties)
            score += len(unique_tricks)

            for i in range(len(line) - 1):
                current_stance = TRICKS[line[i]]['stance']
                next_stance = TRICKS[line[i + 1]]['stance']

                if current_stance == next_stance or next_stance == ACCEPTABLE_STANCES[current_stance]:
                    score += 1

            # award fitness for category

            self.fitness_scores.append(score)

    def selection(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass


class FileSaving:
    def __init__(self):
        pass
