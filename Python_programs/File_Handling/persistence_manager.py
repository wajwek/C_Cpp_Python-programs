import pickle

def save_data_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)

def load_data_pickle(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

data = {"imie": "Maciej", "lista": [1, 2, 3]}
save_data_pickle(data, "dane.pkl")

wczytane = load_data_pickle("dane.pkl")
print(wczytane)

        