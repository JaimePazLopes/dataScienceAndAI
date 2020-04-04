import pandas

df = pandas.read_csv("..\\files\\Salaries.csv")
print(df.head())
print(df.info())
print(df["BasePay"].mean())
print(df["OvertimePay"].max())
print(df[df["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"])
print(df[df["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"])
print(df.loc[df["TotalPayBenefits"].idxmax()])
print(df[df["TotalPayBenefits"] == df["TotalPayBenefits"].max()])
print(df.loc[df["TotalPayBenefits"].idxmin()])
print(df.groupby(['Year'])['BasePay'].mean())
print(df["JobTitle"].nunique())
print(df['JobTitle'].value_counts().head())
print(sum(df[df["Year"] == 2013]["JobTitle"].value_counts() == 1))
print(sum(df['JobTitle'].apply(lambda x : 'chief' in x.lower())))
df["title_len"] = df["JobTitle"].apply(len)
print(df[["TotalPayBenefits", "title_len"]].corr())
print()
df = pandas.read_csv("..\\files\\Ecommerce Purchases")
print(df.head())
print(df.info())
print(df["Purchase Price"].mean())
print(df["Purchase Price"].max())
print(df["Purchase Price"].min())
print(df[df["Language"] == "en"].count())
print(df[df["Job"] == "Lawyer"].count())
print(df["AM or PM"].value_counts())
print(df["Job"].value_counts().head())
print(df[df["Lot"] == "90 WT"]["Purchase Price"])
print(df[df["Credit Card"] == 4926535242672853]["Email"])
print(df[(df["CC Provider"] == "American Express") & (df["Purchase Price"] > 95)].count())
print(sum(df['CC Exp Date'].apply(lambda x: '25' == x[3:])))
df['Email Provider'] = df['Email'].apply(lambda x: x.split("@")[1])
print(df['Email Provider'].value_counts().head())

print(df['Email'].apply(lambda x: x.split("@")[1]).value_counts().head())








