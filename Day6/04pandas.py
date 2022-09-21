import pandas as pd

data = {'age':[23,43,15,19],
        'name':['길동','춘향','순신','감찬'],
        'height':[175.3,180.3,179.6,160.6]}

df1 = pd.DataFrame(data, columns=['name','age','height'])

print(df1)
print(df1.name)
print(df1.iloc[:,1])