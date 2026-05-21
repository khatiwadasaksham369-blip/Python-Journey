import random
print("Welcome! to the System,Sir!")

items = {
       "rock":-1,
       "paper":0,
       "scissor":1

          }


reverse_items = {
        -1:"rock",
        0:"paper",
        1:"scissor"

        }
for password in range(3):
    password1= input("Enter password:")
    if password1 == "sk":
        user1="y"
        while user1=="y":
            computer= random.choice(list(items.values()))
       
            human_input= input("Enter your input:").lower()
   


            if human_input not in items:
                print("Invalid input!")
                continue
                   


            human = items[human_input]

            print("Computer choose:", reverse_items[computer])


            if human == computer:
                print("Draw!")


            elif ( (human==0 and computer==-1) or
                    (human==-1 and  computer==1)or
                    (human==1 and computer==0)  
                    ):

                print("You wins! Congratulations!")

            else:
                print("Computer wins!")
        
            user1=input("Do you want to continue(y/n)").lower()
        break  

else:
    print("Wrong password.\nSystem lock!")







