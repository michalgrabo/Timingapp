import pickle

tes_list = []

with open("final_pickle", "wb") as outfile:
    pickle.dump(tes_list, outfile)

with open("final_pickle", "rb") as infile:
    test_dict_reconstructed = pickle.load(infile)
print(test_dict_reconstructed)
