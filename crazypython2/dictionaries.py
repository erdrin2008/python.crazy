#collection of items, mutable, not indexable, works on a pair key:value
contact_into={
    "alma":"044159972",
    "erin":"049654321"
}
print(contact_into)
alma_info=contact_into["alma"]
print(alma_info)
contact_into["Orkidea"]="049000123"
contact_into["Orkidea"]="0490000123"
contact_into["Orkidea"]="0490001023"
del contact_into["Orkidea"]
print(contact_into)
keys=contact_into.keys
print(keys)
values=contact_into.values()
print(values)
items=contact_into.items()
print(items) #print out the key-value pair as a lists
