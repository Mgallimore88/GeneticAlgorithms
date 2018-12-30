from EnuBubbleSort import bubble_sort


class Parents:
    #returns the maximum scoring words from an input list of words, scores and requested number of parents.

    def __init__(self, input_words = None, input_scores = None, num_of_parents = None):
        self.input_words = ["Empty"] if input_words == None else input_words
        self.input_scores = ["Empty"] if input_scores == None else input_scores
        self.num_of_parents = 2 if num_of_parents == None else num_of_parents

    def maxfinder(self):
        tagparents = list(enumerate(self.input_words))
        tagscores = list(enumerate(self.input_scores))
        tagscores = bubble_sort(tagscores, self.num_of_parents)
        fitlist = [] * len(tagscores)
        #print(tagparents)
        #print(tagscores)

        #Create a combined list of scores and parents
        for i in range(len(tagscores)):
            fitlist.append(tagparents[tagscores[i][0]][1])
            fitlist.append(tagscores[i][1])
        #print(fitlist)

        #Unzip the combined scores and parents list into 2 separate lists called parents and scores
        parents=[]*int(len(fitlist)/2) # initialise the lists to half the length of combined score+parent list
        scores = []*int(len(fitlist)/2)
        for i in range(len(fitlist)):
            if i % 2 == 0: #even case
                parents.append(fitlist[i])
            else: # odd case
                scores.append(fitlist[i])

        #Zip the parents and scores lists together into tuples
        parentlist = zip(parents, scores)
        return(list(parentlist))
