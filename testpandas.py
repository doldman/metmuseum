import pandas as pd



hokusai = r'HokusaiMetObjects.csv'

df = pd.read_csv(hokusai)

print(df['Dimensions'])
