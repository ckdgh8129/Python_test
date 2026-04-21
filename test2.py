가위 = 1
바위 = 2
보 = 3
num = int(input("가위바위보 : "))
num2 = int(input("가위바위보 : "))

if num==1 and num2==2:
    print("승자 : 2")
elif num==2  and    num2==3:
    print("승자 : 2")
elif num==3 and num2==1:
    print("승자 : 2")
elif num==1 and num2==3:
    print("승자 : 1")
elif num==2 and num2==1:
    print("승자 : 1")
elif num==3 and num2==2:
    print("승자 : 1")

else:
    print("무승부")

