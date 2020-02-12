from random import randint, choice
import sys


# get lines into list
#randomly select words from thew list /use a loop to rune the number of words
#print (words)

def dictonary_words(num_words): 
    f = open("words.txt", "r")
    words = f.readlines()
    #print(words)
    for i in range(num_words):
        print(choice(words))

        #print(words)




#print(f.read())


if __name__ == "__main__":
    num_words=sys.argv[1]
    numwords = int(num_words)
    dictonary_words(numwords)










