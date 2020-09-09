# Program to read a paragraph and calculate the word count, sentence count & more
# Written by Matt Taylor
import os
import csv

paragraph_path = os.path.join("Resources/paragraph_1.txt")

with open(paragraph_path) as file:
    paragraph_data = csv.reader(file, delimiter=" ")

    