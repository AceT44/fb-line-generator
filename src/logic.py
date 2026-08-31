from trick_data import ACCEPTABLE_STANCES, TRICKS
import random


class GeneticAlgorithm:
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
            self.selection(breeding_pool)

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

            for trick in line:  # awarding fitness for non-repeated difficulties and tricks
                unique_difficulties.add(TRICKS[trick]['difficulty'])
                unique_tricks.add(trick)
            score += len(unique_difficulties)
            score += len(unique_tricks)

            for i in range(len(line) - 1):  # awarding fitness for consistency in stances
                current_stance = TRICKS[line[i]]['stance']
                next_stance = TRICKS[line[i + 1]]['stance']

                if current_stance == next_stance or next_stance == ACCEPTABLE_STANCES[current_stance]:
                    score += 1

            for i in range(len(line) - 1):  # awarding fitness for having various categories
                current_category = TRICKS[line[i]]['category']
                next_category = TRICKS[line[i + 1]]['category']

                if current_category != next_category:
                    score += 1

            self.fitness_scores.append(score)

    def selection(self, breeding_pool):
        sorted_fitness = sorted(
            zip(self.population, self.fitness_scores),
            key=lambda x: x[1],
            reverse=True
        )

        self.parents = []

        for i in range(breeding_pool):
            self.parents.append(sorted_fitness[i][0])

    def crossover(self):
        pass

    def mutation(self):
        pass


class FileSaving:
    def __init__(self):
        pass
