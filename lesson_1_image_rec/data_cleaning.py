import pandas as pd

# Ok so we want to change how the csv shows where all of the files are
# We would like to append Images/train/ to every line in the csv.

# Import the csv as a dataframe

data = pd.read_csv("train.csv")

# print(data.head())

# print(data.shape[0])

for i in range(data.shape[0]):
    indv = data.iloc[i]
    indv.filename = 'Images/train/' + indv.filename
    data.iloc[i] = indv



data.to_csv('train_clean.csv')


# for i in range(10):
#     print(data.iloc[i])

# indv_file = data.iloc[0]

# print(indv_file)

# print('filename' in dir(indv_file))

# print(type(indv_file.filename))

# indv_file.filename = 'Images/train/' + indv_file.filename

# print(indv_file)
