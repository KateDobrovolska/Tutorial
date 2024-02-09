#-------------------------------------Метод пошуку інформації в строках-- методи Find and Index----------------------------------------

# files = ['video.avi', 'audio.mp3', 'document.doc', 'folder']
# for file in files:
#     indx = file.find('.')
#     if indx !=-1:
#         suffix = file[indx+1:]
#         print(f'File: {file} Index: {indx} Suffix: {suffix}')
#     else:
#         print(f'File: {file} Suffix: not found')
#------------------------------------------------------------------------
# files = ['video.avi', 'audio.mp3', 'document.doc', 'folder']
# for file in files:
#     try:
#         indx = file.index('.')
#         suffix = file[indx+1:]
#         print(f'File: {file} Index: {indx} Suffix: {suffix}')
#     except ValueError:
#         print(f'File: {file} Suffix: not found')
# #-------------------------------------------------------------------------
# files = ['video.avi', 'audio.mp3', 'document.doc', 'folder', 'backup.tar.gz']
# for file in files:
#     try:
#         indx = file.rindex('.') # rindex шукати починаючи справа
#         suffix = file[indx+1:]
#         print(f'File: {file} Index: {indx} Suffix: {suffix}')
#     except ValueError:
#         print(f'File: {file} Suffix: not found')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------Строкові методи: Split & Join-------------------------------------------------------------------
# text = 'First sentence. Second sentence. Third sentence.' # розбити строку на список речень 
# sentences = text.split(".")
# print(sentences)
#---------------------------------------------------------------
# import re
# text = 'First sentence. Second sentence! Third sentence?' # розбити строку на список речень, якщо рвзні знаки в кінці 
# sentences = re.split("[\.\!\?]", text)
# print(sentences)
#---------------------------------------------------------------
# import re
# text = 'First sentence. \nSecond sentence! \nThird sentence?' # \n -перенос строки  
# print(text)
# sentences = text.split("\n") # розбиває строку на елементи списку 
# print(sentences)
# new_text = ' '.join(sentences) # збирає список в строку 
# print(new_text)
#--------------------------------------------------------------------
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# header = '|{:^15}|{:^15}|{:^15}|'.format('int', 'int^2', 'int^3') #три колонки відцентровані по центру
# separator = '-'*len(header)
# body = ''
# for num in numbers:
#     body += '|{:^15}|{:^15}|{:^15}|\n'.format(num, num**2, num**3)
# table = '\n'.join([separator, header, separator, body, separator])
# print(table)
#---------------------------------------------------------------------------------------------------------------
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# header ='|{:^15}|{:^15}|{:^15}|{:^15}|'.format('int', 'dex', 'oct','bin') #три колонки відцентровані по центру
# separator = '-'*len(header)
# body = ''
# for num in numbers:
#     body += '|{0:^15d}|{0:^15x}|{0:^15o}|{0:^15b}|\n'.format(num, num**2, num**3)
# table = '\n'.join([separator, header, separator, body, separator])
# print(table)
#-----------------------------------------------Method Translate---------------------------------------------------------------
# trans_map = {ord('Я'): 'Ya', ord('н'): 'n', ord('а'): 'a'}
# ukr_name = 'Яна'
# lat_name = ukr_name.translate(trans_map)
# print(ukr_name, '=', lat_name, sep=' ')
# -----------------------------------------------------------------------------------------------------------------------------
# trans_map = {ord('Я'): 'Ya', ord('н'): 'n', ord('а'): 'a', ord('о'): 'o'}
# text = 'Hello World'
# index = text.find('World')
# new_index = text.translate(trans_map).find('World')
# print(index)
#------------------------------------------------------------------------------------------------------------------------------
# mut - мутабельность - изменяемость, упорядоченость, уникальность элементов 
# immut - не имменяемый, нельзя добавлять, удалять и изменять елементы  
# ord - упорядоченая 
# nu - не уникальная 
# un - уникальные елементы 
# no - не упорядоченая коллекция 

# list        mut   ord     nu []
# tuple       ord   immut   nu (,)
# set         mut   no      un {}
# frozenset   immut no      un frozenset()
# dict        mut   no      un (nu for values) {'key': 'value'} 
# str         immut ord     nu '' "" """""" ''''''
#-------------------------------------------------------------------------------------------------------------------------------
# V1_підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]
# def real_len(text):
#     return len(text.replace('\n', '').replace('\f', '').replace('\r', '').replace('\t', '').replace('\v', ''))

# print(real_len('Alex\nKdfe23\t\f\v.\r'))
#-----------------------------------------------------------------------------------------
# V2 _
# def real_len(text):
#     exclusion = ['\n', '\f', '\r', '\t', '\v']
#     count = 0
#     for i in text:
#         if i not in exclusion:
#             count += 1

#     return count

# print(real_len('Alex\nKdfe23\t\f\v.\r'))
#-----------------------------------------------------------------------------------------
# У модулі роботи з функціями ми писали функцію get_fullname для складання повного імені користувача. 
# Виконаємо невелике продовження для цього завдання та напишемо функцію is_check_name, яка приймає два параметри (fullname, first_name) і повертає логічне значення True або False. Це результат перевірки, чи є рядок first_name префіксом рядка fullname. 
# Функція is_check_name чутлива до регістру літер, тобто "Sam" і "sam" для неї різні імена.
# def is_check_name(fullname, first_name):
#     result = False
#     if fullname.split(' ')[0] == first_name:
#         result = True
#     else: 
#         result = False
#     return result

#------------------------------------------------------------------------------------------
# def is_check_name(fullname, first_name):
    # return True if fullname.split(' ')[0] == first_name else False # second variant


num1 = 2147483647
num2 = 3
print(num1+num2)

