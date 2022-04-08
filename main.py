name= input("Enter your name: ")
print(name, "you are going on an adventure")


feedback= input("You're on a dark road in the middle of nowhere and you've come to the end of the road. Which way would you like to  go,left or right? ").lower()

if feedback == "left":
   feedback   = input("You then again find a river.Would you swim across or walk around it? ")
   
elif feedback == "right":
    input("You then find a  weak looking bridge do you use it or leave? ")
    
    if feedback == "use":
          print("You fall of the bridge and break your limbs")
    elif feedback== "walk":
        print("Now you will be living in the forest")
    else:
        print("Invalid choice. You lose")
       
   
if feedback == "swim":
    print("Oops a crocoodile just ate you") 
    
elif feedback== "walk":
    print("You have starved and died while trying to walk around the river.")
else:
    print("Invalid choice. You lose.")
   
    
print("Thank you for your participation" ,name,)       
      