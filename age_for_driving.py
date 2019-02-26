country = input('請問你是哪國人：')
age = input('請輸入年齡：')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('你可以在台灣考駕照/開車')
    else:
        print('你還不能在台灣考駕照/開車')
elif country == '加拿大':
    if age >= 16:
        print('你可以在加拿大考駕照/開車')
    else:
        print('你還不能在加拿大考駕照/開車')