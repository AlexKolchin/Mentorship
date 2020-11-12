import re

input_text = """ bbali taata - blabbla, tutu
Tratata - blabla, tutu"""
i = 0
text = re.findall('[a-zа-яё]+', input_text, flags=re.IGNORECASE)
new_list = []
new_string = ''
for word in text:
    for i in range(len(word)):
        if word[i] == word[i-1]:
            new_list += [word]
            input_text = input_text.replace(word, '')
        i+=1
print(input_text)
print(' '.join(new_list))