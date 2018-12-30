from rand_string import rand_string
from letter_conversion import letter_conversion

class Population:
    def __init__(self, word_length = 5, seeds = 5,parents = ["empty"]): #default initialisation
        self.word_length = word_length
        self.seeds = seeds
        self.parents = parents

    
    def initialise(self): #Make a population of words in a list.
        pop_construct = ["Init"] * self.seeds
        for i in range(len(pop_construct)):
            pop_construct[i] = rand_string(self.word_length)   
        
        print("INITIAL POP")
        for row in range(len(pop_construct)):
                pop_construct[row] = "".join(pop_construct[row])
        return pop_construct

    




