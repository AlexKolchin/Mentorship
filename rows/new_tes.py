text = ['abba', 'abcddcba', 'abcs']
#word = 'abc'
new_list = []
new_word = ''
copy = []
for word in text:
    for i in range(0, len(word)):
        if word[i] == word[-1-i]:
            new_list.append(word[i])
    list1 = new_list[:4]
    list2 = new_list[4:]

print(list1)
print(list2)
print(new_list)
