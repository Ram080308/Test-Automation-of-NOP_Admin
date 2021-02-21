import pandas as pd
myrows = ["Test" , "One" ,"Hero", "Maxi"]
df = pd.DataFrame(myrows)
df.to_excel(".\\here.xlsx")
print(df)