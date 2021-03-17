# concatenate lists
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]

list_3 = list_1 + list_2
print(list_3) # [1, 2, 3, 4, 5, 6, 7, 8]

list_1.extend(list_2)
print(list_1) # [1, 2, 3, 4, 5, 6, 7, 8]


# dataframe: select first x columns by index
import pandas as pd

df = pd.DataFrame({'col_A': [1, 2, 3], 'col_B': [4, 5, 6], 'col_C': [7, 8, 9]})

print(df.iloc[:, 0:2])


# dataframe: select columns by name
import pandas as pd

df = pd.DataFrame({'col_A': [1, 2, 3], 'col_B': [4, 5, 6], 'col_C': [7, 8, 9]})

print(df[['col_A', 'col_B']])


# dataframe: select first x rows by index
import pandas as pd

df = pd.DataFrame({'col_A': [1, 2, 3], 'col_B': [4, 5, 6], 'col_C': [7, 8, 9]})

print(df.iloc[0:2, :])


# dictionaries/dicts: sort
list_of_grades = [{'name': 'Jennifer', 'final': 95}, {'name': 'David', 'final': 92}, {'name': 'Aaron', 'final': 98}]

print(sorted(list_of_grades, key = lambda x: x['name'])) # [{'name': 'Aaron', 'final': 98}, {'name': 'David', 'final': 92}, {'name': 'Jennifer', 'final': 95}]

def sort_by_name(item):
    return item['name']

print(sorted(list_of_grades, key = sort_by_name))


# lambdas
lambda_fun = lambda arg: arg + 10
print(lambda_fun(5)) # 15

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum')) # Full name: Guido Van Rossum


# matrix: min/max 
matrix = [[1, 2, 4], [8, 9, 0]]

all_items = []

for arr in matrix:
    for el in arr:
        all_items.append(el)

print (max(all_items), min(all_items)) # 9 0






