#Рядки:
#1
num_str = 125
num_str = str(num_str)
print(type(num_str))

#2
message = 'Hi, my name is Python!'
new_message = message.replace('y', '0').replace('i', '1')
print(new_message)

#3
split_test = 'This is a split test'
words = split_test.split()
string_join = ' '.join(words)
print(string_join)

#4
mylenth = len(string_join)
print(mylenth)

#Списки:
#1
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

#2
list_extend = [4, 5, 6]
list_extend2 = [7, 8, 9]
list_extend.extend(list_extend2)
print(list_extend)

#3
next_index = list_extend.index(6)
print(next_index)

#4
length_list_append = len(list_append)
print(length_list_append)

#Словники:
#1
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])

#2
print("\nКлючі:")
for key in dict_test.keys():
    print(key)
print("\nЗначення:")
for value in dict_test.values():
    print(value)

#3
print("\nПари ключ-значення:")
for key, value in dict_test.items():
    print(f"{key}: {value}")






































