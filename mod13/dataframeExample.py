import pandas as pd

data={"Name":["Alice","Bob","Charlie"],
      "age":[25,30,32],
      "city":["new york","san francisco","los angeles"]
      }

df=pd.DataFrame(data)
print(df)
