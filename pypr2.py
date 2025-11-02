num_str = int(125)
num_str = str(num_str)
print(num_str)

message = "Hi, my name is Python!"
message = message.replace("y", "0")
message = message.replace("i", "1")
print(message)

split_test = "This is a split test"
parts_split_test = split_test.split(" ")
string_join = " ".join(parts_split_test)
print(string_join)
print("Довжина рядка:", len(string_join))

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)
print("Індекс елементу 6 у списку list_extend:", list_extend.index(6))
print("Довжина списку list_append:", len(list_append))

dict_test = {"car": "Toyota", "price": 4900, "where": "EU"}
print("car:", dict_test["car"])
print("where:", dict_test["where"])
print("keys:", list(dict_test.keys()),"values:", list(dict_test.values()))
print("items:", list(dict_test.items()))