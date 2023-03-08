"""
Напишите программу удаляющую из текста все слова , содержащие "абв"
"""
def str_del(s):
    my_list = s.split()
    my_new_list = [i for i in my_list if "абв" not in i]
    return(str(my_new_list))
s = "авлодл рвгойх кфщабвы аблшабв ниофы абрффф абвойгз"
print(str_del(s))