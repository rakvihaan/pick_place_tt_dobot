import tkinter as tk
import time
import config as cfgg
import random
import serial
import DobotDllType as dType
import all_functions_file as q
import csv
from pynput import keyboard
# import sss as s
# import heartrate; heartrate.trace(browser=True)

ardu = serial.Serial(port = 'COM6', baudrate=9600, timeout = 0.1)

# database_file = "d_database_1.csv"
database_file = "\d_database_1.csv"
accu_state = 0
# q.create_empty_csv(12,4)
dobot_max_h = 115
dobot_min_h = 20


def writee(state):
	global accu_state
	accu_temp = ""
	if state == "t":
		if accu_state ==0 :
			accu_state = 1
			accu_temp = "o"
		elif accu_state ==1:
			accu_state = 0	 
			accu_temp = "c"
	elif state == "c":
		accu_state = 1
		accu_temp = "o"
	elif state == "o":
		accu_state = 0
		accu_temp = "c"
	elif state == "b":
		accu_temp = 'b'
	elif state	== 'n':
		accu_temp = 'n'
	ardu.write(accu_temp.encode('utf-8'))

def exitt(root):
	dType.DisconnectDobot(api)
	root.destroy()

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

writee("o")
writee("n")

api = dType.load()
x=0
y=0
z=0
state = dType.ConnectDobot(api, "COM5", 115200)[0]
print("Connect status:",CON_STR[state])

if (state == dType.DobotConnect.DobotConnect_NoError):

	dType.SetQueuedCmdClear(api)

	dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
	dType.SetPTPJointParams(api, 400, 400, 400, 400, 400, 400, 400, 400, isQueued = 1)
	dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)
	dType.SetPTPJumpParams(api, 0, 200, isQueued = 1)
	pos = dType.GetPose(api)
	x = pos[0]
	y = pos[1]
	z = pos[2]
	rHead = pos[3]
	dist_btw_slots = 20.5
	indexx = 0

	init_pos = [216,-105,115]
	x1 = init_pos[0]
	y1= init_pos[1]
	z1 = init_pos[2]


	x2 = 139#136
	y2 = -260#-266
	z2=z1

	x3 = 141
	y3 = 194
	z3=z1
# running = False

# # x+x-y+y-
# statee = [0,0,0,0]
# # xyzr
# initpos = [232,76,12,45]
# dpressed = False

def toxy(x1,y1,z1,z2,sd):
	# global x,y,z
	if (state == dType.DobotConnect.DobotConnect_NoError):
		pos = dType.GetPose(api)
		x = pos[0]
		y = pos[1]
		z = pos[2]
		dType.SetQueuedCmdClear(api)
		# indexx = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, x+1, y+1, z+1, rHead, 1)[0]
		if x >180:
			indexx = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, x, sd[y1], dobot_max_h, rHead, 1)[0]
			indexx = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, sd[x1], sd[y1], z1, rHead, 1)[0]
			indexx = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, sd[x1], sd[y1], z2, rHead, 1)[0]
		
		elif x <=180:
			indexx = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, sd[x1], y, dobot_max_h, rHead, 1)[0]
			indexx = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, sd[x1], sd[y1], z1, rHead, 1)[0]
			indexx = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, sd[x1], sd[y1], z2, rHead, 1)[0]
		
		
		dType.SetQueuedCmdStartExec(api)
		# print(sd[x1], sd[y1], z1, z2)
		# print(indexx)
		while indexx > dType.GetQueuedCmdCurrentIndex(api)[0]:
			dType.dSleep(100)
		# print("sdf")
		dType.SetQueuedCmdStopExec(api)	
		# print("Asd")


def dobottttt():
	# tox=0
	# toy=0
	count = 0
	for i in range(0,6):
		for j in range(0,4):
			#puick and place
			# dobot_scan(1,j,i,tox,toy)
			dobot_scan(1,j,i)
					

def get_emp_slot(tray_list):
	# print(tray_list)
	for i in range(0,len(tray_list)):
		for j in range(0,len(tray_list[0])):
			try:
				if tray_list[i][j] == 0:
					# print(i,j)
					# return [j,i]
					return [i,j]
			except:
				return [99,99]


def dobot_scan(tid,sxm,sym):
	global x1,y1,z1,x2,y2,z2,x3,y3,z3
	writee("o")
	b_dy = 0
	b_dx = 288
	dist = 20.5
	# dist = 20.75
	sx =0
	sy =0
	# dx =0
	dy =0

	if tid == 1:
		sx = x1+(sxm*dist)
		sy = y1+(sym*dist)
	elif tid == 2:
		sy = y2+(sxm*dist)
		sx = x2-(sym*dist)
	elif tid == 3:
		sx = x3-(sym*dist)
		sy = y3+(sxm*dist)
	
	sd = [sx,sy,b_dx,b_dy]
	# print(sd)
	toxy(0,1,dobot_max_h,dobot_min_h,sd)
	writee("c")
	time.sleep(0.25)

	toxy(2,3,dobot_max_h,dobot_max_h,sd) #getting to barcode scanner position

	# wait for scanning
	
	# writee('b')
	time.sleep(1)
	tt_data=read_barcode()
	# writee('b')
	# tt_data = ""
	# while not tt_data:
	# 	tt_data = read_barcode()
	# 	if tt_data:
			# break

	# writee('n')
	#  time.sleep(1)
	# tt_data = cfgg.temp_bar
	# print(tt_data)
	# tt_data = "R10511580-81"
	# print(type(tt_data))

	# td_id =q.get_tray_id(tt_data)#fetching if done or not
	td_id = int(q.search_csv_by_tt_id(database_file, tt_data))
	print(td_id)
	td_id = td_id + 2
		
	if td_id == 1:
		dx = x1+(dest_xm*dist)
		dy = y1+(dest_ym*dist)
	elif td_id == 2:
		temp_slot = get_emp_slot(cfgg.tray_comp)
		cfgg.tray_comp[temp_slot[0]][temp_slot[1]] = tt_data
		dest_xm = temp_slot[1]
		dest_ym = temp_slot[0]
		dy = y2+(dest_xm*dist)
		dx = x2-(dest_ym*dist)
	elif td_id == 3:
		temp_slot = get_emp_slot(cfgg.tray_isComp)
		cfgg.tray_isComp[temp_slot[0]][temp_slot[1]] = tt_data
		dest_xm = temp_slot[0]
		dest_ym = temp_slot[1]
		dx = x3-(dest_xm*dist)
		dy = y3+(dest_ym*dist)

	sd = [b_dx,b_dy,dx,dy]	
	toxy(2,3,dobot_max_h,dobot_min_h,sd)
	# print(sd)
	writee("o")
	time.sleep(0.25)
	toxy(2,3,dobot_max_h,dobot_max_h,sd)


def setptp():
	# global cfgg.initpos
	initposs = dType.GetPose(api)
	destpos=[]
	for i in range(0, 4):
		destpos.append(initposs[i] + cfgg.statee[i])

	dType.SetQueuedCmdClear(api)
	indexx = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVLXYZMode, destpos[0], destpos[1],destpos[2], destpos[3], 1)[0]
	
	dType.SetQueuedCmdStartExec(api)

	while indexx > dType.GetQueuedCmdCurrentIndex(api)[0]:
		dType.dSleep(100)
	# print("sdf")

	dType.SetQueuedCmdStopExec(api)
	
	# print(cfgg.initpos)

def sendCmdToDobot_cons():
	while True:
		if cfgg.dpressed:
			# print(cfgg.statee)
			setptp()
			# time.sleep(0.25)

def on_pressed(event,msg,dir):
	cfgg.statee[msg-1] = cfgg.statee[msg-1] + dir
	cfgg.dpressed = True

def on_released(event,msg,dir):
	cfgg.statee[msg-1] = cfgg.statee[msg-1] - dir
	cfgg.dpressed = False


def update_text_boxes_thread_func(text_boxes):
	while True:
		random_numbers = updatedPos()
		# print(random_numbers)
		for i in range(8):
			text_boxes[i].delete("1.0", tk.END)
			text_boxes[i].insert("1.0", str(random_numbers[i]))
		time.sleep(0.25)

def randPos():
	rpos = []
	for i in range(0,8):
		rpos.append(random.randrange(5, 70, 1))
	return rpos

def updatedPos():
	temp = dType.GetPose(api)
	currPos = cfgg.dobotCurrentPos(temp)
	currPos = toInt(currPos)
	return currPos

xx = ["X: ", "Y: ", "Z: ", "R: ", "J1: ", "J2: ", "J3: ", "J4: "]

def toInt(x):
	return [x.X, x.Y, x.Z, x.R, x.J1, x.J2, x.J3, x.J4]

def save_tray_data(timestamp,tray_list,typee):
	if typee == 0:
		temp = "completed"
	elif typee == 1:
		temp = "not_completed"
	timestamp = timestamp + "_" + temp + ".csv"
	csv_file=open(timestamp, 'a+', newline='')
	header = ['A', 'B', 'C', 'D']
	writer = csv.DictWriter(csv_file, fieldnames=header)
	writer.writeheader()

	for i in range(0,len(tray_list)):
		writer.writerow({'A':tray_list[i][0], 'B':tray_list[i][1], 'C':tray_list[i][2], 'D':tray_list[i][3]})


barcode=""
temp_bar = ""

def on_press(key,listener):
	global barcode,temp_bar
	# global barcode
	# print("sdf")
	try:
		if key == keyboard.Key.enter:
			temp_bar = barcode
			barcode=""
			# print(temp_bar)
			writee('n')
			listener.stop()
		else:
			barcode+=key.char
			# writee('n')
	except:
		pass

# import threading
r=0
def read_barcode():
	global barcode,temp_bar
	# print("sdf")
	writee('b')
	with keyboard.Listener(on_press=lambda event:on_press(event,listener)) as listener:
		try:
			listener.join()
			# writee('n')
			return temp_bar
		except:
			r=r+1
			print(r)
# keep_barcode = threading.Thread(traget=read_barcode())
# keep_barcode.setDaemon(True)
# keep_barcode.start()

# read_barcode()