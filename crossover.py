                #mouse is random size between 1 and inheritence rate. if mouse is smaller than 
                # the fitness value of a parent, that parent's letter is transposed to the current position along
                # the phrase.  Setting inheritance rate to 100 means that the fitness score of an individual parent
                # gives each of its letters a [fitness score]% chance of being selected each time the 
                # letter is assessed. 
                # Early in the simulation, a high value of inheritence rate means there is such a low chance of a 
                # parent donating its letter in the early stages, that when one parent 
                # does luckily donate a letter, the chances are great that it is
                # an incorrect letter; the child's fitness does not increase significantly, and the child is not
                # very likely to become a parent in the next generation. 
                # Lowering the value of inheritence increases the likelihood of a parent donating its letter early in 
                # the simulation, since 
                # probability of mouse being less than fitness is greater, but there comes a point where the program
                #plateaus - once the fitness of the fittest parent is equal to the inheritence rate. This is because
                # the mouse is always lower than the fitness of the parent, and so the parent's letters are always selected.
                # This exposes an issue with the way the parents fitnesses are iterated through - one by one,
                # from weakest to strongest, means that in the end only the strongest's letters are chosen.
                #  This puts a restriction on inheritence rate to be over 100, but how to deal with the early game?
                # double the chance of a parent donating genes?
from letter_conversion import letter_conversion
from random import randint
# mutate = bool


def cross_populate(parent_list, num_of_seeds, inheritence_rate = 100, mutation_rate = 1000): # takes an input of form [('word', 10.3) ('word2', 20) ... ('word_n', score_n)]
    
    children_list = []
    for child in range(num_of_seeds):
        child_constructor = [""] * len(parent_list[0][0])
        for letter in range(len(parent_list[0][0])):
            for fitness in range(len(parent_list)):
                mouse = randint(1,inheritence_rate)
                suncream = randint(0,mutation_rate) < mutation_rate
                if mouse <= parent_list[fitness][1] and suncream == True:
                    child_constructor[letter] = parent_list[fitness][0][letter]
                else:
                    child_constructor[letter] = (letter_conversion(randint(0,26)))
        
        children_list.append(child_constructor)


    for row in range(len(children_list)):
        children_list[row] = "".join(children_list[row])
    return children_list
    