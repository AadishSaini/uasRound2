import pandas as pd

df = pd.DataFrame({
    'Yes' : [50, 21],
    'No' : [131, 2]},
    index=['row1', 'row2'],
)

print(df, "\n\n")

lis = pd.Series([1, 2, 3, 4, 5], 
                index=['row1', 'row2', 'row3', 'row5', 'row6'],
                name = 'lis',)

print(lis)
