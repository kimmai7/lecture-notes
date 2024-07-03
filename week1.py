# READ VS READLINES
# readlines(): reads each line and stores into a list
# read(): reads each line and stores as one string
# strip the newlines for each line by using a for loop

# STORAGE (using read())
# each line read and processing require c time
# 2c time to process those lines -> inefficient
# reading the file into one string causes the variable it's stored in to occupy lots of memory

# LIST COMPREHENSION
list_1st = [(line.rstrip('\n') for line in open('example.txt'))]
# MOST EFFICIENT WAY
#   - with statement handle file exceptions and automatically closes the file
with open('example.txt', 'r') as file:
    for i in file:
        print(i.rstrip('\n'))

# FIELDS
# read file, separate fields, convert fields to python types
# example: csv files with fields course, limit, enrollment, waitlist
# below separates fields into course and # of students who tried to enroll in it
with open('example.txt', 'r') as file:
    for i in file:
        field = i.rstrip('\n').split(',')
        print(field[0], int(field[2]) + int(field[3]))

# PICKLE
import pickle
dictionary = dict(a = 1, b = 2, c = 3)
with open('dictionary.pickle', 'rb') as file:
    dictionary = pickle.load(file)
    print(dictionary)
# returns

# SAVE TO GIT
# terminal > local
# git init > git add week1.py > git commit -m "first commit"
# CHECK GIT REPO
# git log
# GET ALL CHANGES
# git push -u --force origin main

# LEC1 CODE: B7x9


