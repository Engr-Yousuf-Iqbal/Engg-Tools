#########################         GUI        ##############################
from tkinter import*
root=Tk()
######### Setting window Started   ##############
root.title("A&Y Engineering Solutions")
root.iconbitmap("Eng_Icon.ico")
W=700
H=500
xwidth=root.winfo_screenwidth()
yheight=root.winfo_screenheight()
x=int(xwidth/2-W/2)
y=int(yheight/2-H/2)
root.geometry(f"{W}x{H}+{x}+{y}")
root.resizable(False,False)
# Transparancy
root.attributes("-alpha",0.98)
# Background
root.config(bg="green")
######### Window settings completed #############


root.mainloop()
######################### Backend of the APP ##############################
import numpy as np
print("This is a Y+ Calculator for CFD Applications")
rho= 1.225 #float(input("Enter density: "))
V= 25 #float(input("Enter Velocity: "))
L= 1 #float(input("Enter Characteristic Length: "))
mu= 1.789e-5 #float(input("Enter dynamic viscosity: "))
dy1= 0.003
Re=rho*V*L/mu
print(Re)
Cf=0.058/Re**0.2
tao_w=0.5*Cf*rho*V**2
ut=np.sqrt(tao_w/rho)
Yplus=ut*dy1*rho/mu
print(int(Yplus))
