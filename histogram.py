



# argument may be filename
def histogram(source_txt):
    """function which takes a source_text  and return a histogram data structure that stores each unique word along with the number of times the word appears in the source text."""
    lines = open(source_txt, "r")

    word_histogram = {}

    for word in lines:
  
        word = word.rstrip()
        #if the word is not in the histogram, it's the first time we have seen the word
        if word not in word_histogram:
            word_histogram[word]= 1
        else: 
            word_histogram[word] = word_histogram[word] + 1 
  
    return(word_histogram)




def unique_words(word_histogram):
    """function that takes a histogram argument and returns the total count of unique words in the histogram"""
    total_count= 0
    for words in word_histogram:
        if words in word_histogram == 1:
            total_count += 1
    return total_count


def frequency(word,histogram):
    """function that takes a word and histogram argument and returns the number of times that word appears in a text."""
    return histogram(word)


if __name__ == "__main__":
    my_histogram= histogram("words.txt")
    print(my_histogram)
    print("0000000000000000")
    print(frequency(,my_histogram))
    unique_words(my_histogram)