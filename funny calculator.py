# is this is
# a
# funny calculator


h=input("enter operator( + , - , * , / , % ): ")
i=int(input("input number1: "))
j=int(input("input number2: "))

if i == 43 and j == 3 and h == "*":
    print("555")
elif i == 56 and j == 9 and h == "+":
    print(77)
elif i == 56 and j == 6 and h == "/":
    print(4)
elif h ==  "*":
    k = i*j
    print(k)
elif h ==  "+":
    k = i+j
    print(k)
elif h ==  "-":
    k = i-j
    print(k)
elif h ==  "/":
    k = i/j
    print(k)
elif h ==  "%":
    k = i%j
    print(k)
else:
    print("!!!")
