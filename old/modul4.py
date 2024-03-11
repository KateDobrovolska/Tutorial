#--------------------------------------------------------------------------------------------------
#data = [1, -3, 4, 100, 0, -5, 10, 1, 1]
#def prepare_data(data):
#    sorted_list = sorted(data)
#    sorted_list.pop(0)
#    sorted_list.pop(-1)
#   return sorted_list

#--------------------------------------------------------------------------------------------------
# text = 'Lora Ipsum is simply dummy text of the printing and typesetting industry.'
# dict_counter = {} # {'L':1, 'o':2}
# for char in text: # перебрати строку за допомогою for
#     try: 
#         count = dict_counter[char] # отримаэмо значення по ключу 
#     except KeyError:
#         count = 0
#     count +=1  # значення каунт збыльшуэмо на одиницю, тому що цей символ трапився в нашому циклі і ми оновлюємо значення в нашому словнику 
#     dict_counter[char] = count # записуємо значення по ключу

# print(dict_counter)
#---------------------------------------------------------------------------------------------------
# text = 'Lora Ipsum is simply dummy text of the printing and typesetting industry.'
# dict_counter = {} # {'L':1, 'o':2}
# for char in text: # перебрати строку за допомогою for
#     count = dict_counter.get(char, 0) # метод словника get, який приймає першим аргументом ключ char, та другим аргументом по замовчуванню він підставляє None, тобто якшо ключа не буде знайдено, то він поверне None, а нам потрібно, щоб він повернув 1, тобто ініціалізував нашу змінну count 
#     count +=1  # значення каунт збыльшуэмо на одиницю, тому що цей символ трапився в нашому циклі і ми оновлюємо значення в нашому словнику 
#     dict_counter[char] = count # записуємо значення по ключу

# print(dict_counter)

