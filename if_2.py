#Практика: Сравнение строк




def f_str(x,y):
    if type(x) != str != type(y):
        return("0")
    if type(x) == str == type(y) and len(x) == len(y):
        return("1")      
    elif len(x) > len(y):
        return("2")   
    elif x != y and y == "learn":
        return("3") 
    # Дана! Без else это нормально что так получилось ? Работает жеш =)
      

z = f_str("python", "learn1")
print(z)
z = f_str("python", "learn")
print(z)
z = f_str("132", "learn")
print(z)
z = f_str(123, 333)
print(z)