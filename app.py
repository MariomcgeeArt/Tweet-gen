from flask import Flask
from histogram import histogram
from sample import sample


app = Flask(__name__)





@app.route('/')
def create_words():
   # my_file= open("words.txt",'r')
   # lines = my_file.readlines()
   # print(lines)
    my_histogram = histogram('words.txt')

    word = sample(my_histogram)
    print(word)
    return word

