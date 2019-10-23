import os
import fnmatch
from collections import Counter


def ffind(pattern, path):
    result = []
    for name in os.listdir(path):
        if fnmatch.fnmatch(name, pattern):
            result.append(path + name)
    return result


def calc_num_of_char(File):
    rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    alphabet = dict(zip(rus + [chr(elem) for elem in range(97, 123)], [0] * (len(rus) + 26)))
    with open(File, 'r', encoding = 'utf-8') as f:
        f_lines = f.readlines()
        for line in f_lines:
            # приводим к одному регистру все буквы
            line.lower()
            for letter in alphabet:
                alphabet[letter] += line.count(letter)
        print('{File} : \n {alphabet}'.format(File = File, alphabet = alphabet))
    return alphabet


files = ffind('*.txt', './') # указываем нужный нам формат файлов
rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet = dict(zip(rus + [chr(elem) for elem in range(97, 123)], [0] * (len(rus) + 26)))
for File in files: # пробегаемся по всем файлам из нашей текущей директории        
    alphabet = dict(Counter(alphabet) + Counter(calc_num_of_char(File)))
# выводим общее количество букв во всех файлах
print('Total number of letters in the all files in the directory : \n {alphabet}'.format(alphabet = alphabet))
