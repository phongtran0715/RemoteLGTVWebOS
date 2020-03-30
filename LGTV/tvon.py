import os
import json
import control
def main():
    #Read devices list
    devicesFile = os.path.join(workspace,"devices.json")
    devices = control.read_devices_list(devicesFile)
    if devices == None:
        print("Info! Not found any existed devices")
        print("Info! Start to scan devices")
        try:
            device = control.scan_devices(devicesFile)
        except:
            print("Error 00! : Scan device unsuccessful")
    # Pairing
    if devices == None:
        print("Can not found any devices")
        return
    for item in devices:
        name = item['uuid']
        address = item['address']
        model = item['model']
        configFile = name + "_" + address + ".json"
        configFile = os.path.join(workspace,configFile)
        if os.path.isfile(configFile) == False:
            print("Paring TV device : %s - %s" % (model, address))
            try:
                result = ctrl.pair_device(name, address, configFile)
                if result == False:
                    print("Error 01! Can not pair TV device")
            except:
                print("Error 02! Can not pair TV device")
                continue
        else:
            print("Device %s - %s had already paired" % (model, address))

        # Send turn on command
        command = "on"
        args = []
        authConfig = control.read_config_file(name, address)
        if authConfig == None :
            print("Error 03! Can not get authen config file!")
            continue
        print("Sending turn on command to TV : %s - %s" % (model, address))
        try:
            control.send_command(name, command, args, authConfig)
            print("Turn on successful!")
        except:
            print("Error 04! Can not turn on TV",)

if __name__ == '__main__':
    workspace = os.path.join(os.path.expanduser("~"),".lgtv")
    if not os.path.exists(workspace):
        os.makedirs(workspace)
    main()