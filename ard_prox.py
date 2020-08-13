import serial
import time
import tkinter
import struct
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

serialData = serial.Serial('com4', 9600)

while True:
    if serialData.inWaiting() > 0:
        data = serialData.readline()
        distance = float(data)
        if distance < 2.5:
            messagebox.showinfo("Notification", "Proximity Reached")
            exit()
        print(distance)
