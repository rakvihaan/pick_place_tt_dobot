import tkinter as tk

# sx_var = tk.StringVar()
# sy_var = tk.StringVar()
# dx_var = tk.StringVar()
# dy_var = tk.StringVar()

class dobotCurrentPos:
	def __init__(self,pos):
		self.X = pos[0]
		self.Y = pos[1]
		self.Z = pos[2]
		self.R = pos[3]
		self.J1 = pos[4]
		self.J2 = pos[5]
		self.J3 = pos[6]
		self.J4 = pos[7]

running = False

# temp_bar = ""

# x+x-y+y-
statee = [0,0,0,0]
# xyzr
initpos = [232,76,12,45]
dpressed = False

tray_source = []
tray_comp = []
tray_isComp = []

for i in range(0,12):
	tray_comp.append([0]*4)
	tray_isComp.append([0]*4)
	tray_source.append([1]*4)




