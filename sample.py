import random 
from histogram import histogram

txt = [('cats', 3), ('dog', 4), ('rabbits', 2), ('turtles', 1)]


# histogram1 = {'hello':1, 'bye':2}
# print(histogram1.items())
def sample(histogram):
    print(histogram)
    tokens =  sum([count for word, count in histogram.items()]) 
    
    dart = random.randint(1,tokens)
    fence = 0

    for word, count in histogram.items():
        fence += count
        if fence >= dart:
         return word



if __name__ == "__main__":
    pass


    




    