import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt


def best_leaf_nodes(train_X, val_X, train_y, val_y):
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

    model = RandomForestRegressor(max_leaf_nodes=2)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)

    best_mae = mean_absolute_error(val_y, predictions)
    leaf = 2
    for i in range(3, 1000, 2):
        model = RandomForestRegressor(max_leaf_nodes=i)
        model.fit(train_X, train_y)
        predictions = model.predict(val_X)

        curr_mae = mean_absolute_error(val_y, predictions)
        print("for ", i, " nodes \t \t \t \t", curr_mae)
        if curr_mae < best_mae:
            best_mae = curr_mae
            leaf = i
    return leaf

filePath = "./melb_data.csv"

data = pd.read_csv(filePath)
data = data.dropna(axis=0)


y = data.Price


melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[melbourne_features]



train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
leaf_nodes = best_leaf_nodes(train_X, train_y, val_X, val_y)



print(leaf_nodes, "is the best leaf node")
model = RandomForestRegressor(max_leaf_nodes=leaf_nodes)



model.fit(train_X, train_y)
predictions = model.predict(val_X)



mae = mean_absolute_error(val_y, predictions)
print(mae)
