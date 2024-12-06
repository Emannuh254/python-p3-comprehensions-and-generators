def return_evens(num_list):
    
    return [num for num in num_list if num % 2 == 0]


def make_exclamation(sentence_list):
    # add "!" to the end of each sentence in the list
    return [sentence + "!" for sentence in sentence_list]
