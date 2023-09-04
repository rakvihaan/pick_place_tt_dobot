import tkinter as tk
import threading
import func2 as f
# import heartrate; heartrate.trace(browser=True)

root = tk.Tk()
root.title("Dobot")
root.geometry("660x450")

tk.Label(root, text="Xs: ").grid(row=0, column=0)
tk.Label(root, text="Ys: ").grid(row=0, column=2)
tk.Label(root, text="Xd: ").grid(row=1, column=0)
tk.Label(root, text="Yd: ").grid(row=1, column=2)
tk.Label(root,text="Tray source: ").grid(row=5, column=0)
tk.Label(root,text="Tray dest: ").grid(row=5, column=2)

sx_var = tk.StringVar()
sy_var = tk.StringVar()
dx_var = tk.StringVar()
dy_var = tk.StringVar()
tids_var = tk.StringVar()
tidd_var = tk.StringVar()

sx_var.set(0)
sy_var.set(0)
dx_var.set(0)
dy_var.set(0)
tids_var.set(1)
tidd_var.set(1)

sx_entry = tk.Entry(root,textvariable=sx_var)
sy_entry = tk.Entry(root,textvariable=sy_var)
dx_entry = tk.Entry(root,textvariable=dx_var)
dy_entry = tk.Entry(root,textvariable=dy_var)
tray_texts = tk.Entry(root,textvariable=tids_var)
tray_textd = tk.Entry(root,textvariable=tidd_var)

sx_entry.grid(row=0, column=1)
sy_entry.grid(row=0, column=3)
dx_entry.grid(row=1, column=1)
dy_entry.grid(row=1, column=3)
tray_texts.grid(row=5, column=1)
tray_textd.grid(row=5, column=3)


sd = [int(tray_texts.get()),int(tray_textd.get()),int(sx_entry.get()), int(sy_entry.get()), int(dx_entry.get()), int(dy_entry.get())]


button = tk.Button(root, text="Move Arm", command = lambda: f.dobottttt())
# button = tk.Button(root, text="Move Arm", command = lambda: f.dobot_scan(int(tray_texts.get()),int(sx_entry.get()),int(sy_entry.get())))
# button = tk.Button(root, text="Move Arm", command = lambda: f.dobotStoD(f.fromMatrixToCoord(int(tray_texts.get()),int(tray_textd.get()),int(sx_entry.get()),int(sy_entry.get()),int(dx_entry.get()),int(dy_entry.get()))))
# button = tk.Button(root, text="Move Arm", command = lambda: f.dobotStoD(f.fromMatrixToCoord(sd)))
# button = tk.Button(root, text="Move Arm", command = lambda: f.repeatDobotMove())
# button = tk.Button(root, text="Move Arm", command = lambda: f.dobotStoD([int(sx_entry.get()), int(sy_entry.get()), int(dx_entry.get()), int(dy_entry.get())]))
button.grid(row=2, columnspan=4)
exitbutton = tk.Button(root, text="Exit", command = lambda:f.exitt(root))
exitbutton.grid(row=3, columnspan=4)
accubutton = tk.Button(root, text="Toggle End Effector", command = lambda:f.writee("t"))
accubutton.grid(row=4, columnspan=4)
# tray_label = tk.Label(root,text="Tray Number: ").grid(row=5, column=1)
# tray_text = tk.Entry(root,width=10).grid(row=5, column = 1,columnspan=3)
# accubutton = tk.Button(root, text="Toggle End Effector", command = lambda:f.writee("t"))
# accubutton.grid(row=4, columnspan=4)

label_list = []
xx = ["X: ", "Y: ", "Z: ", "R: ", "J1: ", "J2: ", "J3: ", "J4: "]


labels = []
text_boxes = []

for i in range(8):
	label = tk.Label(root, text=xx[i])
	labels.append(label)
	text_box = tk.Text(root, height=1, width=10)
	text_boxes.append(text_box)

for i in range(4):
	labels[i].grid(row=i+6, column=0, padx=10, pady=10)
	text_boxes[i].grid(row=i+6, column=1, padx=10, pady=10)
for i in range(4,8):
	labels[i].grid(row=i+2, column=0+2, padx=10, pady=10)
	text_boxes[i].grid(row=i+2, column=1+2, padx=10, pady=10)


 
up_button = tk.Button(root, text="X+", width=5, height=2)
down_button = tk.Button(root, text="X-", width=5, height=2)
left_button = tk.Button(root, text="Y-", width=5, height=2)
right_button = tk.Button(root, text="Y+", width=5, height=2)

up_button.grid(row=0, column=9)
down_button.grid(row=2, column=9)
left_button.grid(row=1, column=8)
right_button.grid(row=1, column=10)

gapp = tk.Label(root, text="     ", width=5).grid(row=0, column=7)
gapp2 = tk.Label(root, text="     ", width=5).grid(row=3, column=9)

zup_button = tk.Button(root, text="Z+", width=5, height=2)
zdown_button = tk.Button(root, text="Z-", width=5, height=2)
rleft_button = tk.Button(root, text="R-", width=5, height=2)
rright_button = tk.Button(root, text="R+", width=5, height=2)

zup_button.grid(row=4, column=9)
zdown_button.grid(row=6, column=9)
rleft_button.grid(row=5, column=8)
rright_button.grid(row=5, column=10)

stepp = 1

up_button.bind('<ButtonPress-1>', lambda event: f.on_pressed(event, 1, stepp))
up_button.bind('<ButtonRelease-1>',lambda event: f.on_released(event, 1, stepp))

down_button.bind('<ButtonPress-1>',lambda event: f.on_pressed(event, 1, -stepp))
down_button.bind('<ButtonRelease-1>',lambda event: f.on_released(event, 1, -stepp))
# 
left_button.bind('<ButtonPress-1>',lambda event: f.on_pressed(event, 2, -stepp))
left_button.bind('<ButtonRelease-1>',lambda event: f.on_released(event, 2, -stepp))

right_button.bind('<ButtonPress-1>',lambda event: f.on_pressed(event, 2, stepp))
right_button.bind('<ButtonRelease-1>',lambda event: f.on_releaseR10511587d(event, 2, stepp))


zup_button.bind('<ButtonPress-1>', lambda event: f.on_pressed(event, 3, stepp))
zup_button.bind('<ButtonRelease-1>',lambda event: f.on_released(event, 3, stepp))

zdown_button.bind('<ButtonPress-1>',lambda event: f.on_pressed(event, 3, -stepp))
zdown_button.bind('<ButtonRelease-1>',lambda event: f.on_released(event, 3, -stepp))

rleft_button.bind('<ButtonPress-1>',lambda event: f.on_pressed(event, 4, -stepp))
rleft_button.bind('<ButtonRelease-1>',lambda event: f.on_released(event, 4, -stepp))

rright_button.bind('<ButtonPress-1>',lambda event: f.on_pressed(event, 4, stepp))
rright_button.bind('<ButtonRelease-1>',lambda event: f.on_released(event, 4, stepp))


# cmdPTP_cons = threading.Thread(target=f.sendCmdToDobot_cons)
# cmdPTP_cons.start()
update_text_boxes_thread = threading.Thread(target=lambda: f.update_text_boxes_thread_func(text_boxes))
update_text_boxes_thread.daemon = True
update_text_boxes_thread.start()

# keep_barcode = threading.Thread(traget=f.read_barcode())
# keep_barcode.setDaemon(True)
# keep_barcode.start()

root.mainloop()
