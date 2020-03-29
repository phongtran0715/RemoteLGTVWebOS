# -*- coding: utf-8 -*-
from __future__ import print_function
from inspect import getargspec
import json
import os
import sys
from time import sleep
from scan import LGTVScan
from remote import LGTVRemote
from auth import LGTVAuth

def usage(error=None):
    if error:
        print ("Error: " + error)
    print ("LGTV Controller")
    print ("Author: Karl Lattimer <karl@qdh.org.uk>")
    print ("Usage: lgtv <command> [parameter]\n")
    print ("Available Commands:")

    print ("  -i                    interactive mode")

    print ("  scan")
    print ("  auth <host>")

    commands = LGTVRemote.getCommands()
    for c in commands:
        args = getargspec(LGTVRemote.__dict__[c])
        if len(args.args) > 1:
            a = ' <' + '> <'.join(args.args[1:-1]) + '>'
            print ('  ' + c + a)
        else:
            print ('  ' + c)

def parseargs(command, argv):
    print("Command:"+command)
    args = getargspec(LGTVRemote.__dict__[command])
    if args != None:
        print(args)
    args = args.args[1:-1]

    if len(args) != len(argv):
        raise Exception("Argument lengths do not match")

    output = {}
    for (i, a) in enumerate(args):
        if argv[i].lower() == "true":
            argv[i] = True
        elif argv[i].lower() == "false":
            argv[i] = False
        try:
            f = int(argv[i])
            argv[i] = f
        except:
            try:
                f = float(argv[i])
                argv[i] = f
            except:
                pass
        output[a] = argv[i]
    return output

def send_command(name, command, args, config):
    if command == "on":
        ws = LGTVRemote(name, **config[name])
        ws.on()
        return
    try:
        ws = LGTVRemote(name, **config[name])
        args = parseargs(command, args)
        ws.connect()
        if command is not None:
            ws.execute(command, args)
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()

def read_config_file(name, host):
    data = None
    workspace = os.path.join(os.path.expanduser("~"),".lgtv")
    filename = name + "_" + host + ".json"
    filename = os.path.join(workspace,filename)
    if os.path.isfile(filename) == True:
        with open(filename) as f:
            data = json.load(f)
    else:
        print("Error! Config file doesn't existed")
    return data

def pair_device(name, host, outputConfig):
    result = False
    print("Start to authen device : %s - %s" % (name, host))
    try:
        ws = LGTVAuth(name, host)
        ws.connect()
        ws.run_forever()
        sleep(1)
        config = ws.serialise()
        if outputConfig is not None:
            with open(outputConfig, 'w') as f:
                f.write(json.dumps(config))
            print ("Wrote config file: " + outputConfig)
            result = True
    except:
        print("Error! Can't pair device %s" % name)
    return result

def read_devices_list(file):
    devices = None
    if os.path.isfile(file) == True:
        with open(file) as f:
            devices = json.load(f)
    else:
        print("Waring! Devices list file doen't existed")
    return devices

def scan_devices(output_file):
    results = LGTVScan()
    devices = []
    if len(results) > 0:
        print (json.dumps({
            "result": "ok",
            "count": len(results),
            "list": results
        }))
        for it in results:
            uuid = it['uuid']
            address = it['address']
            model = it['model']
            #Save to json file
            devices.append({
                'uuid': it['uuid'],
                'model': it['model'],
                'address': it['address'],
            })
        with open(output_file, 'w+') as outfile:
            json.dump(devices, outfile)
            
    else:
        print (json.dumps({
            "result": "failed",
            "count": len(results)
        }))
    return devices

def getMac(name, address):
    ws = LGTVAuth(name, address)
    mac = ws.get_mac_address(address)
    return mac

