import pickle

def load(fname):
    with open(fname, 'rb') as output:
        return pickle.load(output)

def save(obj, fname):
    with open(fname, 'wb') as output:
        return pickle.dump(obj,output)
