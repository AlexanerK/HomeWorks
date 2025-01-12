import os
import time
directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        parent_dir = os.getcwd()
        filepath = os.path.join(root,file)
        filesize = os.stat(filepath).st_size
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        print(f'Обнаружен файл:{file},Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')






