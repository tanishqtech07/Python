import random

number = random.randint(1,100) #45

count = 0
while count>0: #Infinite Loop
    count += 1
    user   = int(input('Enter your number: ')) #45
    
    if user == number: #user == number, 45 == 45
        print('You won Man..')
        print(f"You took {count} to win!")
        break

    elif user < number: #21<45
        print("Too low , Guess high")

    elif user > number:
        print('Too high value guess lower value')


#User have only 5 chances and if those chances are over either he will win or lose.