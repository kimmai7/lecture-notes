import pickle

with open('dictionary.pickle', 'rb') as file:
    dictionary = pickle.load(file)
    print(dictionary)