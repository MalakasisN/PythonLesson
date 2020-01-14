categories=[]
for death in data:
    if not death['method_cat'] in categories:
        categories.append(death['method_cat'])
print(len(categories))
