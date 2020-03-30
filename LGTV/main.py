import tkinter as tk
from tkinter import HORIZONTAL
from tkinter import ttk
from tkinter import messagebox
import control as ctrl
import os
from configparser import ConfigParser

class LGRemote:
    def __init__(self, parent):
        self.parent = parent
        self.create_gui()

    def create_gui(self):
        self.parent.title("Remote LG TVs")
        self.parent.columnconfigure([0, 1], weight=1, minsize=75)
        self.parent.rowconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=50)
        self.parent.resizable(0, 0)
        self.parent.eval('tk::PlaceWindow . center')

        # adding image (remember image should be PNG and not JPG) 
        self.imgUp = tk.PhotoImage(file = os.path.join(os.getcwd(), r"images",r"upArrow.png")).subsample(20, 20)
        self.imgLf = tk.PhotoImage(file = os.path.join(os.getcwd(), r"images",r"leftArrow.png")).subsample(20, 20)
        self.imgRg = tk.PhotoImage(file = os.path.join(os.getcwd(), r"images",r"rightArrow.png")).subsample(20, 20)
        self.imgWheel = tk.PhotoImage(file = os.path.join(os.getcwd(), r"images",r"wheel.png")).subsample(20, 20)
        self.imgDown = tk.PhotoImage(file = os.path.join(os.getcwd(), r"images",r"downArrow.png")).subsample(20, 20)

        frame99 = tk.Frame(self.parent, width=200, height=30, bg="yellow")
        btScan = tk.Button(frame99, text="SCAN", bg="white", command = self.scanDevices)
        btScan.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

        #Frame Ten TV
        frame1 = tk.Frame(self.parent, width=200, height=30, bg="yellow")

        self.lbLeftName = tk.Label(frame1, text="TVLG L", bg="yellow")
        self.lbLeftName.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
        self.cbLeft = ttk.Combobox(frame1, values =cbListValue,postcommand=self.updateComboValues)
        self.cbLeft.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)
        self.cbLeft.bind("<<ComboboxSelected>>", lambda index: self.pairDevice(self.cbLeft.current(), "leftIndex"))
        try:
            if appConfig.getint('combobox', 'leftIndex') >= 0:
                self.cbLeft.current(appConfig.getint('combobox', 'leftIndex'))
        except:
            pass

        #Frame nut on/off
        frame2 = tk.Frame(self.parent, width=200, height=100)
        #Them button TV on/off
        self.btnLeftOn = tk.Button(frame2, text="ON", bg="white", padx = 10, command =lambda: self.on(self.cbLeft.current()))
        self.btnLeftOn.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=20)
        self.btnLeftOff = tk.Button(frame2, text="OFF", bg="white", padx = 10, command =lambda: self.off(self.cbLeft.current()))
        self.btnLeftOff.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=20)
        #Frame nut HDMI
        frame3 = tk.Frame(self.parent, width=200, height=100)
        self.btnLeftHdmi1 = tk.Button(frame3, text="HDMI_1", bg="white", command =lambda: self.setInput(self.cbLeft.current(), "HDMI_1"))
        self.btnLeftHdmi2 = tk.Button(frame3, text="HDMI_2", bg="white", command =lambda: self.setInput(self.cbLeft.current(), "HDMI_2"))
        self.btnLeftHdmi1.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        self.btnLeftHdmi2.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=5, pady=5)
        #Frame tang giam am luong
        frame4 = tk.Frame(self.parent, width=200, height=100)
        self.leftVolume = tk.Scale(
            frame4,
            from_ = 0,
            to = 100,
            orient = HORIZONTAL,
            label = "Volume",
            resolution = 1,
            command=self.setVolume
        )
        self.leftVolume.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        #Frame mui ten dieu huong
        frame5 = tk.Frame(self.parent, width=200, height=100)
        self.leftArrowUp = tk.Button(frame5, text="", bg="white", image = self.imgUp, command =lambda: self.channelUp(self.cbLeft.current()))
        self.leftArrowUp.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        #Frame mui ten dieu huong
        frame6 = tk.Frame(self.parent, width=200, height=100)
        #frame6.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.leftArrowLeft = tk.Button(frame6, text="", bg="white", image = self.imgLf)
        self.leftArrowLeft.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
        self.leftArrowRight = tk.Button(frame6, text="", bg="white", image = self.imgRg)
        self.leftArrowRight.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)
        self.leftWheel = tk.Button(frame6, text="", bg="white", image = self.imgWheel, command =lambda: self.listChannel(self.cbLeft.current()))
        self.leftWheel.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=5, pady=5)
        #Frame mui ten dieu huong
        frame7 = tk.Frame(self.parent, width=200, height=100)
        self.leftArrowDown = tk.Button(frame7, text="", bg="white", image = self.imgDown, command =lambda: self.channelDown(self.cbLeft.current()))
        self.leftArrowDown.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        #Frame nut control
        frame8 = tk.Frame(self.parent, width=200, height=100, pady = 50)
        #frame8.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.btnLeftBack = tk.Button(frame8, text="Back", bg="white", padx = 10)
        self.btnLeftExit = tk.Button(frame8, text="Exit", bg="white", padx = 10)
        self.btnLeftBack.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=50, pady=5)
        self.btnLeftExit.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=50, pady=5)

        #Frame Ten TV
        frame9 = tk.Frame(self.parent, width=200, height=30, bg="yellow")
        #Them label TV LEFT/RIGHT
        self.lbRightName = tk.Label(frame9, text="TVLG R", bg="yellow")
        self.lbRightName.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
        self.cbRight = ttk.Combobox(frame9, values =cbListValue,postcommand=self.updateComboValues)
        self.cbRight.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)
        self.cbRight.bind("<<ComboboxSelected>>", lambda index: self.pairDevice(self.cbRight.current(), "rightIndex"))
        try:
            if appConfig.getint('combobox', 'rightIndex') >= 0:
                self.cbRight.current(appConfig.getint('combobox', 'rightIndex'))
        except:
            pass

        #Frame nut on/off
        frame10 = tk.Frame(self.parent, width=200, height=100)
        #Them button TV on/off
        self.btnRightOn = tk.Button(frame10, text="ON", bg="white", padx = 10, command =lambda: self.on(self.cbRight.current()))
        self.btnRightOn.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx= 20)
        self.btnRightOff = tk.Button(frame10, text="OFF", bg="white", padx = 10, command =lambda: self.off(self.cbRight.current()))
        self.btnRightOff.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=20)
        #Frame nut HDMI
        frame11 = tk.Frame(self.parent, width=200, height=100)
        self.btnRightHdmi1 = tk.Button(frame11, text="HDMI_1", bg="white", command =lambda: self.setInput(self.cbRight.current(), "HDMI_1"))
        self.btnRightHdmi2 = tk.Button(frame11, text="HDMI_2", bg="white", command =lambda: self.setInput(self.cbRight.current(), "HDMI_2"))
        self.btnRightHdmi1.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        self.btnRightHdmi2.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=5, pady=5)
        #Frame tang giam am luong
        frame12 = tk.Frame(self.parent, width=200, height=100)
        self.rightVolume = tk.Scale(
            frame12,
            from_ = 0,
            to = 100,
            orient = HORIZONTAL,
            label = "Volume",
            resolution = 1
        )
        self.rightVolume.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        #Frame mui ten dieu huong
        frame13 = tk.Frame(self.parent, width=200, height=100)
        self.rightArrowUp = tk.Button(frame13, text="", bg="white", image = self.imgUp, command =lambda: self.channelUp(self.cbRight.current()))
        self.rightArrowUp.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        #Frame mui ten dieu huong
        frame14 = tk.Frame(self.parent, width=200, height=100)
        self.rightArrowLeft = tk.Button(frame14, text="", bg="white", image = self.imgLf)
        self.rightArrowLeft.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
        self.rightArrowRight = tk.Button(frame14, text="", bg="white", image = self.imgRg)
        self.rightArrowRight.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=5, pady=5)
        self.rightWheel = tk.Button(frame14, text="", bg="white", image = self.imgWheel, command =lambda: self.listChannel(self.cbRight.current()))
        self.rightWheel.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True, padx=5, pady=5)
        #Frame mui ten dieu huong
        frame15 = tk.Frame(self.parent, width=200, height=100)
        self.rightArrowDown = tk.Button(frame15, text="", bg="white", image = self.imgDown, command =lambda: self.channelDown(self.cbRight.current()))
        self.rightArrowDown.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        #Frame nut control
        frame16 = tk.Frame(self.parent, width=200, height=100, pady = 50)
        self.btnRightBack = tk.Button(frame16, text="Back", bg="white", padx = 10)
        self.btnRightExit = tk.Button(frame16, text="Exit", bg="white", padx = 10)
        self.btnRightBack.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=50, pady=5)
        self.btnRightExit.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True, padx=50, pady=5)
        ############################
        # Aligment Frame
        ############################
        frame99.grid(row=0,column = 1)
        frame1.grid(row=1, column=0)
        frame2.grid(row=2, column=0)
        frame3.grid(row=3, column=0)
        frame4.grid(row=4, column=0)
        frame5.grid(row=5, column=0)
        frame6.grid(row=6, column=0)
        frame7.grid(row=7, column=0)
        frame8.grid(row=8, column=0)
        frame0 = tk.Frame(self.parent, width=50, height=900)
        self.label = tk.Label(
            frame0,
            text="",
            foreground="white",  # Set the text color to white
            background="black"  # Set the background color to black
        )
        self.label.pack(fill=tk.BOTH, expand=True)
        frame0.grid(row=2, column=1)
        frame9.grid(row=1, column=2)
        frame10.grid(row=2, column=2)
        frame11.grid(row=3, column=2)
        frame12.grid(row=4, column=2)
        frame13.grid(row=5, column=2)
        frame14.grid(row=6, column=2)
        frame15.grid(row=7, column=2)
        frame16.grid(row=8, column=2)

    def updateComboValues(self):
        self.cbLeft["values"] = cbListValue
        self.cbRight["values"] = cbListValue
    
    def scanDevices(self):
        global devices
        global cbListValue
        outputFile = os.path.join(workspace,"devices.json")
        devices = ctrl.scan_devices(outputFile)
        # devices = ctrl.read_devices_list("devices.json")
        # Update combobox value
        cbListValue.clear()
        for item in devices:
            cbListValue.append(item['model'] + "_" + item['address'])
        self.updateComboValues()
        messagebox.showinfo("Notify","Scan completed!")

    def off(self, index):
        if index >= 0:
            device = devices[index]
            name = device['uuid']
            address = device['address']
            command = "off"
            args = []
            config = ctrl.read_config_file(name, address)
            if config == None :
                messagebox.showerror("Error","Can not get config file!")
                return
            print(config)
            ctrl.send_command(name, command, args, config)
        else:
            messagebox.showerror("Error!","You must select TV device")

    def on(self, index):
        if index >= 0:
            device = devices[index]
            name = device['uuid']
            address = device['address']
            command = "on"
            args = []
            config = ctrl.read_config_file(name, address)
            if config == None :
                messagebox.showerror("Error","Can not get config file!")
                return
            print(config)
            ctrl.send_command(name, command, args, config)
        else:
            messagebox.showerror("Error!","You must select TV device")

    def pairDevice(self, index, side):
        try:
            device = devices[index]
            name = device['uuid']
            address = device['address']
            configFile = name + "_" + address + ".json"
            configFile = os.path.join(workspace,configFile)
            if os.path.isfile(configFile) == False:
                # result = ctrl.pair_device(name, address, configFile)
                result = True
                if result == False:
                    messagebox.showerror("Error 002!","Can not pair TV device")
                else:
                    appConfig.set("combobox", side, str(index))
            else:
                appConfig.set("combobox", side, str(index))
                print("Device index %d had already paired" % index)
        except:
            messagebox.showerror("Error 001!","Can not pair TV device")

    def executeCommand(self, index, command, args):
        if index >= 0:
            device = devices[index]
            name = device['uuid']
            address = device['address']
            config = ctrl.read_config_file(name, address)
            if(config == None):
                messagebox.showerror("Error","Can not get config file!")
                return
            ctrl.send_command(name, command, args, config)

    def setVolume(self, eventObject):
        l_slider_value  = self.leftVolume.get()
        index = self.cbLeft.current()
        command = "setVolume"
        args = [str(l_slider_value)]
        self.executeCommand(index, command, args)

    def getCurrentVol(self, index):
        command = "audioVolume"
        args = []
        sources = self.executeCommand(index, command, args)
        return sources

    def getListInputs(self, index):
        print("Function getListInputs : index = " + str(index))
        command = "listInputs"
        args = []
        self.executeCommand(index, command, args)

    def setInput(self, index, inputId):
        print(index)
        command = "setInput"
        args = [inputId]
        self.executeCommand(index, command, args)

    def listChannel(self, index):
        command = "listChannels"
        args = []
        self.executeCommand(index, command, args)

    def channelUp(self, index):
        command = "inputChannelUp"
        args = []
        self.executeCommand(index, command, args)

    def channelDown(self, index):
        command = "inputChannelDown"
        args = []
        self.executeCommand(index, command, args)


def on_closing():
    print("Form closing event!")
    with open('config.ini', 'w') as f:
        appConfig.write(f)
    window.destroy()

def loadDevicesList():
    global devices
    global cbListValue
    file = os.path.join(workspace,"devices.json")
    devices = ctrl.read_devices_list(file)
    if devices != None:
        cbListValue.clear()
        for item in devices:
            cbListValue.append(item['model'] + "_" + item['address'])

def main():
    # get device list
    loadDevicesList()
    fm = LGRemote(window)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()


if __name__ == '__main__':
    appConfig = ConfigParser()
    appConfig.read('config.ini')
    cbListValue = list()
    devices = list()
    workspace = os.path.join(os.path.expanduser("~"),".lgtv")
    if not os.path.exists(workspace):
        os.makedirs(workspace)
    print("workspace : %s" % workspace)
    window = tk.Tk()
    main()