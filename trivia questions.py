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



