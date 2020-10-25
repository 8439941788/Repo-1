import random
list=["s","w","g"]
print("NUMBER OF ATTEMPTS=10")
print("Snake as s,Water as w,Gun as g")
print("lets the game begin")
print("your score represented by 'z',comp score represented by 'y'")
name=input("Enter your name")
for i in range(10):
    v = random.choice(list)
    x = input("enter your choice")

    if x=='s':
      if x=='s'and v=='s':
        print("you choose",x)
        print("comp choose",v)
        print("Draw")

      elif x=='s'and v=='w':
        print("you choose",x)
        print("comp choose",v)
        print("you won")


      elif x=='s'and v=='g':
        print("you choose",x)
        print("comp choose",v)
        print("comp won")


    elif x=='w':
      if x=='w'and v=='s':
         print("you choose",x)
         print("comp choose",v)
         print("comp won")


      elif x=='w'and v=='w':
         print("you choose",x)
         print("comp choose",v)
         print("draw")

      elif x=='w'and v=='g':
         print("you choose",x)
         print("comp choose",v)
         print("you won")


    elif x=='g':
      if x=='g'and v=='s':
         print("you choose",x)
         print("comp choose",v)
         print("you won")



      elif x=='g'and v=='w':
         print("you choose",x)
         print("comp choose",v)
         print("comp won")

      elif x=='g'and v=='g':
         print("you choose",x)
         print("comp choose",v)
         print("draw")

    print("no of attempt left",10-(i+1))







