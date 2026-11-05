"""
Filename: Average Calculator.py
Author: <Croft, Malakai>
Created: <10/22/2026>
Instructor: Burgess
"""
s=0
av=0
ne=0
while True:

   x=int(input("Enter a number"))
   s += x
   ne += 1

   print(f"Your current number entries are {ne}")
   av = (s / ne)
   print(f"Your current average is {av} ")


   i = input("Do you want to enter another number? (y/n)")
   if i == "y":
       continue
   else:
       break
