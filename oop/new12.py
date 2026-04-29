import pandas as pd

data = {
    "names": ["divya","esha","ajay","adithya","athul","niya","zehra","hari","grace","isra"],
    "marks": [19,13,16,19,20,17,19,18,20,15]
}

df= pd.DataFrame(data)
print(df.loc[[6,7]])
