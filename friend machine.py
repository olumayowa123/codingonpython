maths = None
maths2 = None
def display_intro():
    print('''You boot up the computer and wait for something to happen,
The system boots and you're met by a dark figure, noticing you he jumps into the computer.
Wanting answers you are faced with a choice''')
def choose_option():
    option = input("Are you going to  jump into the computer or turn it off?")
display_intro()
choose_option
print('''before you can blink you're sucked into the computer.
An entity of some sort appears to talk to you  on a big screen
''')
print("the pocket of the biggest shirt is ready for you to jump")
print("a giant appears, he hasn't noticed you yet")
print("Giant speaking here now")
print("Do i smell human bones")
print("helper speaking now")
print("quick answer these questions")
print("hurry!")
      
from datetime import datetime

now_date = datetime.now()
print(datetime.strftime(now_date,'%A'))
print(datetime.strftime(now_date,'%B'))
print(datetime.strftime(now_date,'%Y'))
user=input("Hello" + " " +"what is your name ")
print("hello " + user)
age = input ("how old are you ")
friend= input ("are you my friend  ")
print ("hello"+ " " +user +" " +"you are" +" "+ age +" "+"years old")

if  friend == "yes" :
    print ("hello friend")
elif friend  :
    print ("That's okay")

friends= input("do you want to be my friend ")
if friends == "yes":
    print ("hello new friend")
elif friends=="no":
        why= input("why")
print("ok")
        
answer= input("what are you doing ")
if answer=="nothing":
    print("you aren't doing anything") 
elif answer:
    print("you are" + " " + answer)
maths = input("what is 10*10 ")
if maths == "100" :
    print ("You did it on your first try . impressive!")
if maths != "100":
    print ("try again")
    maths2 = input("what is 10*10 ")
if maths2 == "100" :
        print ("You did it on your second try")
elif maths2:
    print("you didn't get it :(")
col=input("What's your favourite colour")
print("I like red!")
charact=input("what is your favourite character?")
print("mine is pikachu!")
 
print("now we shall see if you can answer these questions correctly")
print("Mayowa did this")
print("With nothing but code")
print("Now lets start")

score=0
print("Hello I am symet")
Name=input("What is your name? ")
print("hello" + " "+ Name)
resan=input("are you ready for questions ")
print("lets start!")
print("question1")
question1=input("where does the president of united states live while he is in the office? ")
if question1=="white house"or question1=="the white house"or question1=="The White House" or question1=="THE WHITE HOUSE"or question1=="The white house":
    print("You got it!")
    score+=1
elif question1:
    print("You didn't get it right")
    print("The correct answer is white house")
print("question2")
question2=input("what do you get when you freeze water ")
if question2=="ice":
    print("2 in a row!")
    score+=1
elif question2:
    print("That's wrong")
    print("The correct answer is ice")
print("Question 3")
three=input("how many legs does a spider have ")
if three=="eight" or three== "8":
    print("Correct")
    score+=1
elif three:
    print("wrong")
    print("it's eight or 8")
print("Question 4")
ez=input("what number do you skip while you are counting? ")
if ez=="0" or ez=="zero":
    print("You got it!")
    score+=1
elif ez:
    print("The answer is zero or 0")
red=input("If i drink i die but if i eat i am fine what am am I ? ")
if red=="fire":
    print("Hey you are on fire")
    score+=1
elif red:
    print("thats wrong")
    print("the answer is fire")
    print("I think you need to heat up a bit")
wart=input("why did the melon jump into the pond? ")
if wart=="because it wanted to be a watermelon" or wart=="to become a watermelon" or wart=="to transform to a watermelon":
    print("thats very good")
    score+=1
elif wart:
    print("That is wrong")
    print("the answer is to become a watermelon")
qu=input("which country gifted the statue of liberty to the us?")
if qu=="France" or qu== "FRANCE" or qu=="france":
    print("WOW")
    score+=1
elif qu:
    print(" thats wrong")
ask=input("what company uses santa claus as advetisment? ")
if ask=="coca cola":
    print("I actually didn't know that")
    score+=1
elif ask:
    print("wrong its coca cola")
bg=input("what makes you happy when you are sad but sad when you are happy? ")
if bg=="it's gonna be over soon" or bg=="it is going to be over soon":
    print("you are smart")
    score+=1
elif bg:
    print("wrong it is going to be over soon ")
lol=input("what has the strongest gravitational pull? ")
if lol=="black hole":
    print("wow")
    score+=1
elif lol:
    print("it's a black hole")

bills=input("who founded microsoft")
if bills=="bill gates" or bills=="Bill Gates"or bills=="BILL GATES":
    print("that's very easy")
    score+=1
elif bills:
    print("wrong its bill gates")
    
her=input("how many hearts does an octopus have? ")
if her=="3" or her=="three":
    print("correct")
    score+=1
elif her:
    print("it is three or 3")
simba=input("what was the name of simba's father")

if simba=="Mufasa" or simba=="mufasa":
    print ("correct")
    score+=1
elif simba:
    print("it's Mufasa")

print("your score was: ",score,"/14")

    
print("now that i have your test scores which i didn't really need")
print("its the end he's found us!")
print("goodbye friend")
print("it was a pleasure meeting you")
print("                                                     ")
print("                                                     ")
print("                                                     ")
print("                                                     ")
print("                                                     ")
print("                                                     ")
def display_cont0():
    print("You wake up in the sewer yuck this place stinks i guess he didn't eat me")
    print("you find a manhole and escape the sewers aaah fresh air is so nice")
    print("you catch a ride home ")
    print("and dose off for the night")



print("Time for the next round")



import random
import time

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)


# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["jaguar","lion","tiger","film","cougar","wolf","coyote","dingo","cheetah","damage"
                   ,"plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:
print("the words are jaguar lion tiger film cougar wolf dingo cheetah damage and plants")
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()
main()


hangman()
