
max1= None
min1 = None
ct=1
while True:
    a = input()
    if(a=='done'):
        print(max1)
        print(min1)
        break
    else:
        try:
            c = int(a)
            if(ct==1):
                max1=c
                min1=c
                ct=2
            elif(ct>1):
                if(c>max1):
                    max1 = c
                if(c<min1):
                    min1 = c
                    continue
        except:
            print("Invalid input")
            break
