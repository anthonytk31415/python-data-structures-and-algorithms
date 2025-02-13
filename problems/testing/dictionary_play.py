import pandas as pd
import numpy as np
import torch

# Generate random data
df = pd.DataFrame({
    'season': np.random.choice(['2020', '2021', '2022', '2023'], size=5),
    'name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eve'], size=5),
    'mean': np.random.uniform(10, 50, size=5),
    'std': np.random.uniform(1, 10, size=5)
})

# print(df.items())



# mean_std = dict(
#                     (
#                         (v['season'], v['name']), 
#                         (v['mean'], v['std'])
#                     ) for v in df
#                 )
# print(mean_std)


df1 = pd.DataFrame()

# print(df)

a = [1,2,3]


# d = dict(((1,x), (x,x)) for x in a)
# print(d)

b = [True, False, True]
print(any(b))
print(all(b))


def split_into_two(x): 
    res = x.split(" ")
    if len(res) == 1: 
        res = [""] + res
    return res


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
testStrings = ["C81", "123", " C 123"]
for x in testStrings: 
    print(x)

def applyNormalization(X):
    return (X - X.mean()) / X.std()


# pandas play



