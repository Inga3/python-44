N = int(input("введите N= секунды от 0часов;0 мин;0сек "))

M = N // 60 # min
S = N % 60 # sek
chas = M // 60 # chas
m = M % 60 # min okonch

print( N , "секунд от начала дня =" )
print(  "часов :" , chas) # часов 
print( "мин:" , m) # минут
print( "сек:", S) # секунд
