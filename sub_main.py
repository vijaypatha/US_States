# Practice
import pandas as pd
df = pd.read_csv("50_states.csv")
print(df.head())
# Access the series, row, cell

# print(df.state)

state = df[df.state == 'Arizona']
print(int(state.x), int(state.y))

