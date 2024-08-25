import os.path, time

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
filetime = os.path.getmtime(r'C:\Users\PROVE\pythonProject7\sample2.txt ')
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
filesize = os.path.getsize('sample2.txt')
parent_dir = os.path.dirname('sample2.txt')
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
      f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
