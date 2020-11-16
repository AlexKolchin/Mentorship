text = ['abba', 'abhfj', 'abccda']
word = 'abccda'
i = 0
new_list = []
new_word = ''
for letter in word:
    if letter == word[-1-i]:
        i+=1
        new_list.append(letter)
    else:
        if len(new_list) != 0:
            new_list.remove(letter)
        break


print(new_list)

