"""
Filename: trivia_game.py
Author: <Croft, Malakai>>
Created: <9/25/2026>
Instructor: Burgess
"""
#Answered Correctly: 10
Correct=0

#Total score: 20
Score=0


x=input("What is the default data type for numbers in Python?")
if x=="none":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1

X=input("What symbol is used to perform the modulo operation in Python?")
if x=="5":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1

X=input("Strings are actually arrays of what data type?")
if x=="Characters":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1

X=input("What function is used to perform the modulo operation in Python?")
if x=="%":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1


X=input("What keyword is used to perform the modulo operation in Python?")
if x=="%":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
         Correct-=1

X=input("What is the term for combining multiple lists into one list?")
if x=="Concatenation":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1

X=input("What function would you use to find how many items in a list?")
if x=="Len()":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1

X=input("What method is used to perform the modulo operation in Python?")
if x=="%":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1

X=input("What symbol is used for exponents in Python?")
if x=="**":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1

X=input("What method is used to convert a string to all lowercase characters?")
if x=="lower():":
    Score+=2
    Correct+=1
    #print("Correct!")
    print("Correct! You have been awarded 2 points!")
else:
    if Score>0:
        Score-=1

"Thank you for playing the Trivia Game!"
"you answered 10/10 questions correctly"
"and received a score of 20/20!"

print("Questions answered correctly")
print(f"{Correct}/10")
print(f"{Score}/20")