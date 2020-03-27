import tkinter as tk
from tkinter import HORIZONTAL
from tkinter import ttk

window = tk.Tk()

window.title("Remote LG TVs")
window.columnconfigure([0, 1], weight=1, minsize=75)
window.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=50)

# adding image (remember image should be PNG and not JPG) 

# adding image (remember image should be PNG and not JPG) 
imgUp = tk.PhotoImage(file = r"images\upArrow.png").subsample(20, 20)
imgLf = tk.PhotoImage(file = r"images\leftArrow.png").subsample(20, 20)
imgRg = tk.PhotoImage(file = r"images\rightArrow.png").subsample(20, 20)
imgWheel = tk.PhotoImage(file = r"images\wheel.png").subsample(20, 20)
imgDown = tk.PhotoImage(file = r"images\downArrow.png").subsample(20, 20)

########################################################################
######################### LEFT TV ######################################
########################################################################

#Frame Ten TV
frame1 = tk.Frame(master=window, width=200, height=30, bg="yellow")
#frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
#Them label TV LEFT/RIGHT
llb_TVLeft = tk.Label(master=frame1, text="TVLG L", bg="yellow")
llb_TVLeft.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
lcb_TVLeft = ttk.Combobox(master=frame1)
lcb_TVLeft.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)
#Frame nut on/off
frame2 = tk.Frame(master=window, width=200, height=100)
#frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
#Them button TV on/off
lbtON_TVLeft = tk.Button(master=frame2, text="ON", bg="grey")
lbtON_TVLeft.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
lbtOFF_TVRight = tk.Button(master=frame2, text="OFF", bg="grey")
lbtOFF_TVRight.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)

#Frame nut HDMI
frame3 = tk.Frame(master=window, width=200, height=100)
#frame3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
lbtHDMI1_TVLeft = tk.Button(master=frame3, text="HDMI_1", bg="grey")
lbtHDMI2_TVLeft = tk.Button(master=frame3, text="HDMI_2", bg="grey")
lbtHDMI1_TVLeft.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
lbtHDMI2_TVLeft.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=5, pady=5)

#Frame tang giam am luong
frame4 = tk.Frame(master=window, width=200, height=100)
#frame4.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
lvol = tk.Scale(
    frame4,
    from_ = 0,
    to = 100,
    orient = HORIZONTAL,
	#tickinterval=10,
    resolution = 1,
    ####################
    #command=change_vol
    ####################
)
lvol.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

#Frame mui ten dieu huong
frame5 = tk.Frame(master=window, width=200, height=100)

lbtArrowUp = tk.Button(master=frame5, text="", bg="grey", image = imgUp)
lbtArrowUp.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

#Frame mui ten dieu huong
frame6 = tk.Frame(master=window, width=200, height=100)
#frame6.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

lbtArrowLf = tk.Button(master=frame6, text="", bg="grey", image = imgLf)
lbtArrowLf.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)

lbtArrowRg = tk.Button(master=frame6, text="", bg="grey", image = imgRg)
lbtArrowRg.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)


lbtWheel = tk.Button(master=frame6, text="", bg="grey", image = imgWheel)
lbtWheel.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=5, pady=5)

#Frame mui ten dieu huong
frame7 = tk.Frame(master=window, width=200, height=100)

lbtArrowUp = tk.Button(master=frame7, text="", bg="grey", image = imgDown)
lbtArrowUp.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

#Frame nut control
frame8 = tk.Frame(master=window, width=200, height=100, pady = 50)
#frame8.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
lbtBack = tk.Button(master=frame8, text="Back", bg="grey")
lbtExit = tk.Button(master=frame8, text="Exit", bg="grey")
lbtBack.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
lbtExit.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)


########################################################################
######################### RIGHT TV ######################################
########################################################################

#Frame Ten TV
frame9 = tk.Frame(master=window, width=200, height=30, bg="yellow")
#Them label TV LEFT/RIGHT
rlb_TVLeft = tk.Label(master=frame9, text="TVLG R", bg="yellow")
rlb_TVLeft.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
rcb_TVLeft = ttk.Combobox(master=frame9)
rcb_TVLeft.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)
#Frame nut on/off
frame10 = tk.Frame(master=window, width=200, height=100)
#Them button TV on/off
rbtON_TVLeft = tk.Button(master=frame10, text="ON", bg="grey")
rbtON_TVLeft.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
rbtOFF_TVRight = tk.Button(master=frame10, text="OFF", bg="grey")
rbtOFF_TVRight.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)

#Frame nut HDMI
frame11 = tk.Frame(master=window, width=200, height=100)
rbtHDMI1_TVLeft = tk.Button(master=frame11, text="HDMI_1", bg="grey")
rbtHDMI2_TVLeft = tk.Button(master=frame11, text="HDMI_2", bg="grey")
rbtHDMI1_TVLeft.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
rbtHDMI2_TVLeft.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=5, pady=5)

#Frame tang giam am luong
frame12 = tk.Frame(master=window, width=200, height=100)
rvol = tk.Scale(
    frame12,
    from_ = 0,
    to = 100,
    orient = HORIZONTAL,
	#tickinterval=10,
    resolution = 1,
    ####################
    #command=change_vol
    ####################
)
rvol.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

#Frame mui ten dieu huong
frame13 = tk.Frame(master=window, width=200, height=100)

rbtArrowUp = tk.Button(master=frame13, text="", bg="grey", image = imgUp)
rbtArrowUp.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

#Frame mui ten dieu huong
frame14 = tk.Frame(master=window, width=200, height=100)
rbtArrowLf = tk.Button(master=frame14, text="", bg="grey", image = imgLf)
rbtArrowLf.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)

rbtArrowRg = tk.Button(master=frame14, text="", bg="grey", image = imgRg)
rbtArrowRg.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)


rbtWheel = tk.Button(master=frame14, text="", bg="grey", image = imgWheel)
rbtWheel.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=5, pady=5)

#Frame mui ten dieu huong
frame15 = tk.Frame(master=window, width=200, height=100)

lbtArrowUp = tk.Button(master=frame15, text="", bg="grey", image = imgDown)
lbtArrowUp.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

#Frame nut control
frame16 = tk.Frame(master=window, width=200, height=100, pady = 50)
rbtBack = tk.Button(master=frame16, text="Back", bg="grey")
rbtExit = tk.Button(master=frame16, text="Exit", bg="grey")
rbtBack.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
rbtExit.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)

############################
# Aligment Frame
############################
frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)
frame3.grid(row=2, column=0)
frame4.grid(row=3, column=0)
frame5.grid(row=4, column=0)
frame6.grid(row=5, column=0)
frame7.grid(row=6, column=0)
frame8.grid(row=7, column=0)

frame0 = tk.Frame(master=window, width=50, height=900)
label = tk.Label(
	master=frame0,
    text="",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack(fill=tk.BOTH, expand=True)

frame0.grid(row=2, column=1)


frame9.grid(row=0, column=2)
frame10.grid(row=1, column=2)
frame11.grid(row=2, column=2)
frame12.grid(row=3, column=2)
frame13.grid(row=4, column=2)
frame14.grid(row=5, column=2)
frame15.grid(row=6, column=2)
frame16.grid(row=7, column=2)

#################
#Start gui
#################
window.resizable(0, 0)
window.eval('tk::PlaceWindow . center')
window.mainloop()