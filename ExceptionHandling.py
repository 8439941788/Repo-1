list=[]
num=None
while(True):
    num=input("Enter your input")
    if num=='done':
       break

    try:
        num==int(num)
        list.append(num)

    except:
        print("INVALID INPUT")

print("Maximum number is",max(list))
print("Minimum number is",min(list))



