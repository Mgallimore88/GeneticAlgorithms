from rand_string import rand_string
from Population import Population
from Evaluator import Evaluator
from Parents import Parents
from EnuBubbleSort import (
    bubble_sort,
)  # ?? Is the syntax for importing a function from a .py file the same as the syntax for importing a class from a .py file?
from crossover import cross_populate

target_string = "the quick brown fox jumped over the lazy dog"
seed_count = 100  # number of starting phrases
parent_count = 3  # number of parents per generation
inheritence_rate = 10  # lower => more of the
mutation_rate = 100  # inverse of rate
initialPopulation = Population(
    len(target_string), seed_count
).initialise()  # make a population object
# originally I was making an object called initialPopulation, then performing the
# populate function in the object to try to return a list of words. instead what was returned was a
# object. I could not print initialPopulation because its type was 'obj'. Now I am
# setting initialPopulation = the output of a member function of the class Populate. this returns
# a list like i wanted. Another way to do this may be subclassing?


# Compare the population with the target and return a percentage similarity for each member
fitnesses = Evaluator(initialPopulation, target_string).fitness_percent()

# choose the strongest words from the list, return the n strongest parents along with their fitnesses
myParents = Parents(initialPopulation, fitnesses, parent_count).maxfinder()

# Create a population of children which inherit a proportion of their letters from the n parents
children = cross_populate(myParents, seed_count, inheritence_rate)
print("CHILDREN: ")
print(children)

newParents = myParents

# Main loop: mutation is implemented in the crossover object.
count = 0
while newParents[-1][0] != target_string:
    child_fitnesses = Evaluator(children, target_string).fitness_percent()
    newParents = Parents(children, child_fitnesses, parent_count).maxfinder()
    children = cross_populate(newParents, seed_count, inheritence_rate, mutation_rate)
    count += 1
    print(f"strongest parent:  {newParents[-1][0]}")


print(f"{str(count)} Generations")
