from random import randrange


class Individu:

    def __init__(self, genetic_code):
        self.genetic_code = genetic_code
        self.life_expectancy = 5
        self.is_infected = False

    def infected(self):
        self.life_expectancy = 3 if self.life_expectancy > 3 else self.life_expectancy
        self.is_infected = True

    def calculateImmunity(self, immunised_genetic_code):
        goodGene = len([i for i, j in zip(self.genetic_code, immunised_genetic_code) if i == j])
        if goodGene >= 4:
            return 100
        if goodGene == 3:
            return 75
        if goodGene == 2:
            return 50
        if goodGene == 1:
            return 25
        return 0

    def mutation(self):
        pos = randrange(8)
        self.genetic_code[pos] = 1 if self.genetic_code[pos] == 0 else 0

    def decrease_life(self):
        self.life_expectancy -= 1

    def get_genetic_code(self):
        return self.genetic_code

    def get_life(self):
        return self.life_expectancy
