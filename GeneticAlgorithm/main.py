from random import randrange

from Individu import Individu

# Possible value : 0, 25, 50, 75, 100
MIN_PERCENT_IMMUNITY = 75

# Base size of the population
SIZE = 1000

# Period for log
WHEN_LOG = 50

# Limit of population size
MAX_POPULATION_SIZE = 10_000

# Limit of cycle iterate
MAX_CYCLE = 10_000


def random_populate(size):
    return [Individu(random_genetic_code()) for _ in range(size)]


def selection_by_rank(population, immunised_genetic_code):
    return [individu for individu in population if individu.calculateImmunity(immunised_genetic_code) >= 75]


def random_genetic_code():
    return [randrange(2) for _ in range(8)]


def create_growing_genetic_code(parent_1, parent_2):
    return parent_1.get_genetic_code()[:4] + parent_2.get_genetic_code()[4:]


def run_genetic_genetic():
    IMMUNATED_GENETIC_CODE = random_genetic_code()
    POPULATION = random_populate(SIZE)

    # infection
    POPULATION[randrange(len(POPULATION))].infected()

    CYCLE = 0

    while len(POPULATION) > MAX_POPULATION_SIZE or CYCLE < MAX_CYCLE:

        if CYCLE % WHEN_LOG == 0:
            print("Cycle : {} - Population size : {}".format(CYCLE, len(POPULATION)))

        # selection
        POPULATION = selection_by_rank(POPULATION, IMMUNATED_GENETIC_CODE)

        if len(POPULATION) <= 1:
            print(POPULATION)
            return

        # growing
        population_size_before_growing = len(POPULATION)

        for i in range(int(population_size_before_growing / 4)):
            parent_1 = randrange(population_size_before_growing)
            parent_2 = randrange(population_size_before_growing)
            while parent_1 == parent_2:
                parent_2 = randrange(population_size_before_growing)

            POPULATION.append(Individu(create_growing_genetic_code(POPULATION[parent_1], POPULATION[parent_2])))

        # mutation
        POPULATION[randrange(len(POPULATION))].mutation()

        # cycle of life
        TEMP = []
        for index, individu in enumerate(POPULATION):
            individu.decrease_life()
            if individu.life_expectancy > 0:
                TEMP.append(individu)

        POPULATION = TEMP

        CYCLE += 1


if __name__ == "__main__":
    run_genetic_genetic()
