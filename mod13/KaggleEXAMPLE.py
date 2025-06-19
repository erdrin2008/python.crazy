import pandas as pd
df=pd.read_csv("avgIQpercountry.csv")
print(df.info()) #we see the columns of this dataset
print(df.head()) #we see the first 5 rows which is mostly only asian countries

country_data=df["Country"]
print(country_data)

subset=df[["Country","Average","IQ"]]
filter_DF=subset[subset["Average","IQ"]>100] # u saying Japan has an iq of 106 per avg of ppl holy no wonder ppl say their 50 year ahead of other countries
print(filter_DF)

#null_mask finding nemo(null) rows
null_mask=df.isnull()
null_count=null_mask.sum()
print(null_count)

#removing duplicates
df.drop_duplicates(keep="first", inplace=True)
