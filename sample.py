import random

txt = open('txt.py','r')
txt_lines = readlines(txt)
txt_words = txt_lines.split()







def sort(txt):

    count = 0

    for i in range(len(txt)):
        a = 0
        for a in range(i):
            if(txti] == txt[a]):
                break
            if (i == a + 1):
                count += 1
                print(txt[i], '=', round(((txt.count(txt[i])/count)*100), 2), '%')