import re
class rows():
    def repeat_letter(input_text):
        text = re.findall("[a-zа-яєїі']+", input_text, flags=re.IGNORECASE)
        new_list = []
        for word in text:
            for i in range(1, len(word)):
                if len(word) != 1 and word[i - 1] == word[i]:
                    new_list += [word]
                    input_text = input_text.replace(word, '')
        #last_list = set(new_list)
        last_list = []
        for elem in new_list:
            if elem not in last_list:
                last_list.append(elem)
        print(f'Текст без слів | {input_text}')
        print('Окремо слова | ', end='')
        print(' '.join(last_list))

    def remove_word(input_text1, input_text2):
        text1 = re.findall("[a-zа-яєїі']+", input_text1, flags=re.IGNORECASE)
        text2 = re.findall("[a-zа-яєїі']+", input_text2, flags=re.IGNORECASE)
        for word in text1:
            if word in text2:
                input_text1 = input_text1.replace(word, '')
        print(f'Текст без спільних слів | {input_text1}')

    def delete_middle(input_text):
        text = re.findall("[a-zа-яєїі']+", input_text, flags=re.IGNORECASE)

        for word in text:
            if len(word) % 2 != 0 and len(word) != 1:
                index = int((len(word) - 1) / 2)
                new_list = list(word)
                new_list.pop(index)
                last_word = ''.join(new_list)
                input_text = input_text.replace(word, last_word)
        print(f'Видалено середню букву | {input_text}')
        #print(word[:3]+word[4:])

    def find_simmetric(input_text):
        text = re.findall("[a-zа-яєїі']+", input_text, flags=re.IGNORECASE)
        new_list = []
        for word in text:
            flag = False
            for i in range(0, len(word)):
                if word[i] == word[-1 - i]:
                    flag = True
                else:
                    flag = False
                    break
            if flag == True:
                new_list.append(word)
        """last_list = []
        for elem in new_list:
            if elem not in last_list:
                last_list.append(elem)"""
        print('Симетричні слова | ', end='')
        print(' '.join(new_list))

input_text = """ Прийшла оссіння пора, ллє як з відра, хитаються дерева і чути гудіння!, сінніс - trccrt abca"""
input_text1 = '''abcd, abba, abccba - abc, zzz , sss'''
input_text2 = '''abcd, abba, fjdk, fdfhdj abccba - abc'''
rows.repeat_letter(input_text)
rows.remove_word(input_text1, input_text2)
rows.delete_middle(input_text)
rows.find_simmetric(input_text)


