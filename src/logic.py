from trick_data import ACCEPTABLE_STANCES, TRICKS
import random


class GeneticAlgorithm:
    def start_ga(
            self,
            num_of_tricks: int,
            population_size: int,
            breeding_pool: int,
            crossover_rate: float,
            mutation_rate: float,
            update_gui
    ) -> None:
        self.population = []

        for _ in range(population_size):
            line = []

            for _ in range(num_of_tricks):
                line.append(random.choice(list(TRICKS)))
            self.population.append(line)

        generation = 1
        best_fitness = 0
        best_line = None

        while generation <= 100:
            self.fitness()
            self.selection(breeding_pool)

            current_best_fitness = self.sorted_fitness[0][1]
            if current_best_fitness > best_fitness:
                best_fitness = current_best_fitness
                best_line = self.sorted_fitness[0][0]

            update_gui(
                generation,
                best_line,
                best_fitness
            )

            self.crossover(population_size, crossover_rate, num_of_tricks)
            self.mutation(mutation_rate)

            generation += 1

    def fitness(self) -> None:
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

    def selection(self, breeding_pool: int) -> None:
        self.sorted_fitness = sorted(
            zip(self.population, self.fitness_scores),
            key=lambda x: x[1],
            reverse=True
        )

        self.parents = []

        for i in range(breeding_pool):
            self.parents.append(self.sorted_fitness[i][0])

    def crossover(
            self,
            population_size: int,
            crossover_rate: float,
            num_of_tricks: int
    ) -> None:
        new_population = []

        for _ in range(population_size):
            rand_parent1 = random.choice(self.parents)
            rand_parent2 = random.choice(self.parents)

            if random.random() < crossover_rate:
                crossover_point = random.randint(1, num_of_tricks - 1)

                child = rand_parent1[:crossover_point] + \
                    rand_parent2[crossover_point:]
            else:
                child = rand_parent1.copy()

            new_population.append(child)

        self.population = new_population

    def mutation(self, mutation_rate: float) -> None:
        for child in self.population:
            for i in range(len(child)):
                if random.random() < mutation_rate:
                    child[i] = random.choice(list(TRICKS))


class FileSaving:
    def __init__(self):
        pass
