class Evaluator:
    # Takes an input population list and target word, and returns a list of numbers relating to the fitness#
    #of each phrase. Fitness is given as either the total number of matching letters, or the 
    #percentage of matching letters depending on the function called.
    

    def __init__(self, population_list = None, target_word = None):
        self.population_list = [0] if population_list == None else population_list
        self.target_word = ["Word not received"] if target_word == None else target_word

    def fitness(self):
        fitness_list =[0] * len(self.population_list) #create a list populated by zeros, the same length as number of guess words. 
        for word in range(len(self.population_list)):
            for letter in range(len(self.population_list[word])):
                if (self.population_list[word][letter] == self.target_word[letter]):
                    fitness_list[word] = fitness_list[word] + 1
        return fitness_list

    def fitness_percent(self):
        fitness_percent = self.fitness()
        for score in range(len(fitness_percent)):
            fitness_percent[score] = round(fitness_percent[score] * 100 / len(self.target_word), 1)

        return fitness_percent
