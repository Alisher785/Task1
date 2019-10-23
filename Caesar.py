def Caesar(s, shift, act):
    new_s = ''
    n_alphabet = []
    n_capital_letter = []

    #Если расшифровка, то надо изменить шаг в обратном направлении
    if act == 1:
        shift = -shift
    
    #создания словаря для шифра Цезаря
    alphabet = [chr(elem) for elem in range(97, 123)]
    capital_letter = [chr(elem) for elem in range(65, 91)]
    #создание нового сдвинутого алфавита
    for i in range(26):
        n_alphabet.append(alphabet[(i + shift) % 26])
        n_capital_letter.append(capital_letter[(i + shift) % 26])
    shifted_dict = dict(zip(alphabet + capital_letter, n_alphabet + n_capital_letter))

    #Расшифровка и шифрование послания
    for letter in s:
        if letter in shifted_dict:
            new_s += shifted_dict[letter]
        else:
            new_s += letter
            
    return new_s          


s = input()
shift = int(input())
act = 1 #0 - шифровка, 1 - расшифровка 
print(Caesar(s, shift, act))
