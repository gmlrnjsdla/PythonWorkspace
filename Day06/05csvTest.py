import pandas as pd
foodDf = pd.read_csv('../data/food.csv')
# pd.set_option('display.max_rows',None)
pd.options.display.max_rows = 10
pd.options.display.max_columns = 2


print(foodDf)

# print(foodDf.head())
# print(foodDf.tail())
