a = 10
b = 5
print(a/b)
print(a%b)

num = int(input("정수 입력 : "))
power = int(input("지수 입력 : "))
a = num**power
print(a)
print("{}의 {}승은 {}입니다.".format(num, power, num**power))
print("%d의 %d승은 %d입니다." %(num, power, a))
#오...두 개 같은 값이 나오네

num = int(input("정수 입력 : "))
power = int(input("지수 입력 : "))
print("{}의 {}승은 {}입니다.".format(num, power, num**power))

a = 10
b = a + 12
b = b + 13
print(b)

a+=b
print(a)

a-=3
print(a)


a = 7
b = 3
print("a : {}".format(a))
print("b : {}".format(b))

a = 7
b = 3
temp = a
a = b
b = temp
print("a : {}".format(a))
print("b : {}".format(b))