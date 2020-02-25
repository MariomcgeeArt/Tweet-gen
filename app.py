from flask import Flask
from histogram import histogram
from sample import sample


app = Flask(__name__)





@app.route('/')
def create_words():
    my_file= open("words.txt",'r')
    lines = myfile.readlines()
    my_histogram = histogram(lines)

    word = sample(my_histogram)
    return word

