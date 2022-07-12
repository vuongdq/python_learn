import numpy as np
import pandas as pd

df = pd.read_csv('test.csv',header = None)
print(df)
df = df[2]
df.to_csv('test_out.csv')