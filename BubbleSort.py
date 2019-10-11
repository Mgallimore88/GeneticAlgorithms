# Takes an input list of integers and uses a bubble sort swapping algorithm
# to find and return the highest n values in the list. If the 2nd argument
# of the input field is left blank, n = full list and the whole list is sorted.
# Otherwise only the n comparisons required are made and returned.


def bubble_sort(input_list, num_of_values=None):  # Set default output to entire list
    if num_of_values == None:
        num_of_values = len(input_list)
    else:
        num_of_values = num_of_values
    # proof# print(input_list)

    n = 1
    for _ in range(
        num_of_values
    ):  # ?? is it ok to have unused varibles in loops? Should a while loop be used instead or should I reference Shake somewhere?                 #Here a shake represents the rising to the top of the list of one max value
        for bubble in range(
            len(input_list) - n
        ):  # bubble = one swap or move along the list
            if input_list[bubble] > input_list[bubble + 1]:
                input_list[bubble], input_list[bubble + 1] = (
                    input_list[bubble + 1],
                    input_list[bubble],
                )
        # proof# print("n " + str(n) + str(input_list))
        n += 1
    # proof# print(input_list[-int(num_of_values):])
    print(f"input_list {input_list}")
    return input_list[-int(num_of_values) :]


# proof# bubble_sort([90,80,70,60,50,40,30,20,10])
