from tkinter import *
import random

root=Tk()
root.title("Luck friend Wheel")
root.geometry("400x400")




list1 = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W",  "X", "Y" , "Z"]


def random_number():
    random_no1 = random.randint(0,25)
    random_no2 = random.randint(0,25)
    random_no3 = random.randint(0,25)
    random_no4 = random.randint(0,25)
    random_no5 = random.randint(0,25)
    random_letter_1= list1[random_no1] 
    random_letter_2= list1[random_no2]
    random_letter_3= list1[random_no3]
    random_letter_4= list1[random_no4]
    random_letter_5= list1[random_no5]
    print("your random word  is: " + random_letter_1+random_letter_2+random_letter_3+random_letter_4+random_letter_5)
    
    
btn1 = Button(root)
btn1 = Button(root, text="What is your random word ", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER)

root.mainloop()