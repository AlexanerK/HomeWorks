def custom_write(file_name,strings):
    strings_position = {}
    file = open(file_name, "w", encoding='utf_8')
    number_tell = []
    number_string = []
    string_text = []
    for i in strings:
        number_tell += [file.tell()]
        file.write(str(i) + '\n')
        string_text += [i]
    for j in range(len(strings)):
        number_string += [j+1]
    file.close()
    number_string_tell = zip(number_string, number_tell)
    strings_position = dict(zip(number_string_tell, string_text))
    return strings_position

info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
result = custom_write('test.txt',info)
for elem in result.items():
    print(elem)