# Practice
import pandas as pd
df = pd.read_csv("50_states.csv")
print(df.head())
# Access the series, row, cell

# Accessing a column
# print(df.state)

# Accessing a row
state = df[df.state == 'Arizona']

#Accessing a value of a row
print(int(state.x), int(state.y))

