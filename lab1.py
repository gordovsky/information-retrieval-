import os
import re


def iterateThroughDir(directory):
    dictionary = set()
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            with open(directory+'/'+file, "r") as myfile:
                text = re.split('; |, |\*|\n|\s|\.|\"|\'|\?|\(|\)|\[|\]|-|\$|#|:', myfile.read())
                print('File {0} : {1}'.format(file, len(text)))
                for w in text:
                    dictionary.add(w)
    return dictionary

def createIdentityMatrix():


def invertedIndex():

dictionary = iterateThroughDir("C:/Users/col403/Desktop/lab1")

d = list(dictionary)
d.sort()

dictionary_file = open("dictionary_file.txt", "w")

print('output file length: {0}'.format(len(d)))
for w in d:
    dictionary_file.write(w+'\n')
