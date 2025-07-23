nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)           # map diye shob number ke square kore

evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(evens)             # filter diye shudhu even number gulo ber kore

names = ["Alice", "Bob"]
marks = [85, 90]
paired = list(zip(names, marks))
print(paired)            # 2 ta list ke pair kore: [('Alice', 85), ('Bob', 90)]

paired = [*names, *marks]
print(paired)            # 2 ta list ke pair kore: ['Alice', 'Bob', 85, 90]
