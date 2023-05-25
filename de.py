import pickle
# Load the pickled file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Inspect the contents of the model
print(model)