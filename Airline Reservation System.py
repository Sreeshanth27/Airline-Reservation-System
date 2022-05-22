import random
import tkinter as tk
from tkinter import simpledialog
from tkinter import *

business_class_seats = []
for i in range (1,21):
    business_class_seats.append(i)
    
first_class_seats = []
for i in range (21,111):
    first_class_seats.append(i)
    
second_class_seats = []
for i in range (111,201):
    second_class_seats.append(i)
    
window_seats = []
i=1
j=4
while i<201:
    window_seats.append(i)
    i = i+4
while j<201:
    window_seats.append(j)
    j = j+4  
window_seats.sort()

class Airline:
    
    def __init__(self,seat_type,window_seat,booked_tickets1,booked_tickets2,business_class,first_class,second_class,window):
        self.seat_type = seat_type
        self.window_seat = window_seat
        self.booked_tickets1 = booked_tickets1
        self.booked_tickets2 = booked_tickets2
        self.business_class = business_class
        self.first_class = first_class
        self.second_class = second_class
        self.window = window
        
    def check_for_seats(self):
        if self.seat_type == 'B':
            if(len(self.business_class) == 0):
                return False
            else:
                return True
            
        elif self.seat_type == 'F':
            if(len(self.first_class) == 0):
                return False
            else:
                return True
            
        elif self.seat_type == 'S':
            if(len(self.second_class) == 0):
                return False
            else:
                return True
            
    def check_for_window(self):
        if self.seat_type == 'B':
            random.shuffle(self.business_class)
            for i in self.business_class:
                if i in self.window:
                    self.booked_tickets1.append(i)
                    return True
                else:
                    pass
            return False
            
        elif self.seat_type == 'F':
            random.shuffle(self.first_class)
            for i in self.first_class:
                if i in self.window:
                    self.booked_tickets1.append(i)
                    return True
                else:
                    pass
            return False
            
        elif self.seat_type == 'S':
            random.shuffle(self.second_class)
            for i in self.second_class:
                if i in self.window:
                    self.booked_tickets1.append(i)
                    return True
                else:
                    pass
            return False
            
    def check_for_non_window(self):
        if self.seat_type == 'B':
            random.shuffle(self.business_class)
            for i in self.business_class:
                if i not in self.window:
                    self.booked_tickets2.append(i)
                    return True
                else:
                    pass
            return False
        
        elif self.seat_type == 'F':
            random.shuffle(self.first_class)
            for i in self.first_class:
                if i not in self.window:
                    self.booked_tickets2.append(i)
                    return True
                else:
                    pass
            return False
        
        elif self.seat_type == 'S':
            random.shuffle(self.second_class)
            for i in self.second_class:
                if i not in self.window:
                    self.booked_tickets2.append(i)
                    return True
                else:
                    pass
            return False
            
    def confirmation(self,c):
        if c == 'Y':
            if self.window_seat == 'Y':
                k = self.booked_tickets1.pop()
                if self.seat_type == 'B':
                    self.business_class.remove(k)
                    self.window.remove(k)
                elif self.seat_type == 'F':
                    self.first_class.remove(k)
                    self.window.remove(k)
                elif self.seat_type == 'S':
                    self.second_class.remove(k)
                    self.window.remove(k)
                return k
            
            if self.window_seat == 'N':
                l = self.booked_tickets2.pop()
                if self.seat_type == 'B':
                    self.business_class.remove(l)
                elif self.seat_type == 'F':
                    self.first_class.remove(l)
                elif self.seat_type == 'S':
                    self.second_class.remove(l)
                return l
            
inp = True
ROOT = tk.Tk()
ROOT.withdraw()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)

while(inp):
    st1 = []
    st2 = []
    s = simpledialog.askstring(title = 'INFO', prompt = 'WELCOME TO SRP AIRLINES\nCHOOSE THE CLASS YOU WANT TO TRAVEL IN: ' )

    w = simpledialog.askstring(title = 'WINDOW SEAT PREFERENCE', prompt = 'WE ARE GLAD FOR YOUR CHOICE\nDO YOU WISH FOR A WINDOW SEAT: ')

    my_airline = Airline(s,w,st1,st2,business_class_seats,first_class_seats,second_class_seats,window_seats)

    if my_airline.check_for_seats() == True:
        print('WE ARE GLAD TO HAVE YOU!')
        if  w =='Y':
            if my_airline.check_for_window() == True:
                print('WINDOW SEATS ARE AVAILABLE!')
            else:
                print("SORRY! WINDOW SEATS ARE FULL!")
        elif w == 'N':
            if my_airline.check_for_non_window() == True:
                print('NON WINDOW SEATS ARE AVAILABLE!')
            else:
                print('SORRY! THE SEATS ARE FULL')
            

        a = simpledialog.askstring(title = 'CONFIRMATION', prompt = 'DO YOU WANT ME TO CONFIRM YOUR BOOKING: ')
        n = my_airline.confirmation(a)
        print(f'WELCOME ABOARD! YOUR SEAT NUMBER IS {n}')    

    else:
        print('SORRY! THE FLIGHT IS FULL')
        inp = False
    
    C = input('CLOSE THE BOOKINGS FOR TODAY? ')
    if C == 'YES':
        inp = False
    elif C == 'NO':
        inp = True