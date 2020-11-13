import re
def repeat_letter(input_text):

    i = 1
    text = re.findall("[a-zа-яєїі']+", input_text, flags=re.IGNORECASE)
    new_list = []
    for word in text:
        for i in range(len(word)):
            if len(word) != 1:
                if word[i-1] == word[i]:
                    new_list += [word]
                    input_text = input_text.replace(word, '')
                i+=1
    print(input_text)
    print(' '.join(new_list))
input_text = """ Пийшла осіння пора, ллє як з відра, п'є від сп'яніння!"""
repeat_letter(input_text)

