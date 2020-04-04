import numpy
import pandas

labels = ['a','b','c']
data = [10,20,30]
arr = numpy.array(data)
d = {"a": 10,"b":10,"c":30}

print(pandas.Series(data))
print(pandas.Series(data, labels))
print(pandas.Series(arr, data))
print(pandas.Series(d))
print(pandas.Series(labels))
print(pandas.Series([sum,print,len]))

ser1 = pandas.Series([1,2,3,4], ["USA", "Germany", "USSR", "Japan"])
ser2 = pandas.Series([1,2,5,4], ["USA", "Germany", "Italy", "Japan"])
print(ser1, ser2, ser1["USA"])

print(ser1 + ser2)

print()

numpy.random.seed(101)
df = pandas.DataFrame(numpy.random.randn(5,4),["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)
print(df["W"], type(df["W"]))
print(df[["W", "Z"]])
df["new"] = df["W"] + df["Y"]
print(df)
df.drop("new", axis=1, inplace = True)
print(df)
df.drop("E", inplace=True)
print(df)
print(df.loc["A"])
print(df.iloc[3])
print(df.loc["B", "Y"])
print(df.loc[["A", "B"], "Y"])
print(df.loc[["A", "B"], ["X","Z"]])
booldf = df > 0
print(booldf)
print(df[booldf])
print(df["W"]>0)
print(df[df["W"]>0])
print(df[df["Z"]<0])
print(df[df["W"]>0][["X", "Y"]])
print((df["W"]>0) & (df["Y"]>1))
print((df["W"]>0) | (df["Y"]>1))
#df.reset_index(inplace=True)
newind = "CA NY WY OR".split()
df["States"] = newind
print(df)
print(df.set_index("States"))
print(df)


outside = ["G1", 'G1','G1', "G2","G2","G2"]
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pandas.MultiIndex.from_tuples(hier_index)

df= pandas.DataFrame(numpy.random.randn(6,2), hier_index, ["A", "B"])
print(df)
print(df.loc["G1"])
print(df.loc["G1"].loc[1])
print(df.index.names)
df.index.names = ["Groups", "Num"]
print(df)
print(df.loc["G2"].loc[2]["B"])
print(df.xs("G1"))
print(df.xs(1, level="Num"))

d = { "A":[1,2,numpy.nan], "B": [5, numpy.nan,numpy.nan], "C":[1,2,3]}
df = pandas.DataFrame(d)
print(df)
print(df.dropna())
print(df.dropna(axis=1))
print(df.dropna(thresh=2))
print(df.fillna(value="Value"))
print(df["A"].fillna(value=df["A"].mean()))

data = {"Company": ["GOOG", "GOOG", "MSFT","MSFT", "FB", "FB"],
        "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
        "Sales": [200, 120, 340, 124, 243, 350]}
df = pandas.DataFrame(data)
print(df)
print(df.groupby("Company").mean())
print(df.groupby("Company").sum())
print(df.groupby("Company").std())
print(df.groupby("Company").sum().loc["FB"])
print(df.groupby("Company").count())
print(df.groupby("Company").max())
print(df.groupby("Company").describe())
print(df.groupby("Company").describe().transpose()["FB"])

df1 = pandas.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pandas.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])

df3 = pandas.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

print(pandas.concat([df1,df2,df3]))
print(pandas.concat([df1,df2,df3], axis=1))

left = pandas.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pandas.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(pandas.merge(left, right, on = "key"))

left = pandas.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pandas.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

print(left.join(right))

df = pandas.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())
print(df["col2"].unique(), df["col2"].nunique())
print(df["col2"].value_counts())
print(df[df["col1"]>2])

def times2(number):
    return number*2

print(df["col1"].apply(times2))
print(df["col3"].apply(len))
print(df["col2"].apply(lambda value: value * 2))
print(df.columns)
print(df.index)
print(df.sort_values("col2"))
print(df.isnull())

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pandas.DataFrame(data)
print(df.pivot_table(values="D", index=["A","B"], columns=["C"]))
print(df.pivot_table(values="D", index=["A","B"], columns=["C"]).isnull())

df = pandas.read_csv("..\\files\\example")
df.to_csv("..\\files\\my output", index=False)
df = pandas.read_excel("..\\files\\Excel_Sample.xlsx", sheet_name="Sheet1")
print(df)
df.drop("Unnamed: 0", axis= 1, inplace=True)
df.to_excel("..\\files\\Excel_Sample_Fixed.xlsx", sheet_name="NewSheet")

data = pandas.read_html("https://www.fdic.gov/bank/individual/failed/banklist.html")
print(data[0].head())

import sqlalchemy
engine = sqlalchemy.create_engine("sqlite:///:memory:")

df.to_sql("my_table", engine)
sqldf = pandas.read_sql("my_table", con=engine)
print(sqldf)
