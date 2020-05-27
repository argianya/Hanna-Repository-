# Task 1
my_sentence = "Learning Python is extremely interesting! Python is an interesting tool to work with data".split()
learning_dictionary = {}
for word in my_sentence:
    if word in learning_dictionary:
        learning_dictionary[word] += 1
    else:
        learning_dictionary[word] = 1
print(learning_dictionary)

# List comprehension exercise
new_list = [(i, i ** 2) for i in range(1, 11)]
print(new_list)

# Dictionary
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
definite_total = []
for each in prices:
    total: int = prices[each] * stock[each]
    definite_total.append(total)
print(definite_total)
print(sum(definite_total))
