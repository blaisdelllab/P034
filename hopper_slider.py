#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 18:05:29 2022

@author: ibrahimyassine, cyruskirkman, ikponmwosapatosagie, roberttsai
"""

operant_box_version = True


from tkinter import Scale, Button, Tk
import csv
from os import path
import pigpio

if operant_box_version:
    # Setup use of pi()
    pwm = pigpio.pi()
    
    #Setup GPIO num NOT pin num
    servo_GPIO_num = 2
    pwm.set_mode(servo_GPIO_num, pigpio.OUTPUT)
    
    #set PWM frequency
    pwm.set_PWM_frequency(servo_GPIO_num, 50)
    
    hopper_vals_csv_path = str(path.expanduser('~')+"/Desktop/Box_Info/Hopper_vals.csv")
else:
    hopper_vals_csv_path = 'Hopper_vals.csv'

root = Tk()
root.title('HOPPER UP & DOWN VALUES')
# root.iconbitmap('/Users/ibrahimyassine/Desktop/Blaisdell Lab/icon.icns')
root.geometry("750x300")


def updown_v_get(v1, updown):
    if operant_box_version: 
        #modifying the hopper value
        pwm.set_servo_pulsewidth(servo_GPIO_num, v1)
    print(updown + " Value is " + v1)


up_v= Scale(root,
            from_=500,
            to=2500,
            orient ='horizontal',
            length = 700,
            label = "UP VALUE",
            font = ('Helvetica bold',16), 
            command = lambda val, ud = "UP": updown_v_get(val, ud))   #transfer_UP_V)
up_v.pack()



down_v = Scale(root,
               from_=500,
               to=2500,
               orient='horizontal',
               length= 700,
               label= "DOWN VALUE",
               font= ('Helvetica bold',16),
               command=lambda val, ud = "DOWN": updown_v_get(val, ud))
down_v.pack()

def transfer_updown_v(col, value):
    try:
        r = csv.reader(open(hopper_vals_csv_path))
        data_table = list(r)
        data_table[1][col] = value
        w = csv.writer(open(hopper_vals_csv_path, 'w'))
        w.writerows(data_table)
    except FileNotFoundError:
        print("\n **ERROR Hopper_vals.csv does not exist in directory: " + hopper_vals_csv_path)

def exit_function():
    pwm.set_PWM_dutycycle(servo_GPIO_num, 0)
    pwm.set_PWM_frequency(servo_GPIO_num, 0)
    pwm.stop()
    root.destroy()

Button(root,
       text="Transfer UP Value",
       command = lambda c = 0: transfer_updown_v(c, up_v.get())).pack()
Button(root,
       text="Transfer DOWN Value",
       command = lambda c = 1: transfer_updown_v(c, down_v.get())).pack()
Button(root,
       text= "Exit",
       bg= "red",
       command= exit_function).pack()

root.mainloop()
