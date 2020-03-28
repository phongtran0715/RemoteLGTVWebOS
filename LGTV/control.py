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


search_config = [
    "/etc/lgtv/config.json",
    "~/.lgtv/config.json",
    "/opt/venvs/lgtv/config/config.json"
]

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
    args = getargspec(LGTVRemote.__dict__[command])
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


def find_config():
    w = None
    for f in search_config:
        f = os.path.expanduser(f)
        f = os.path.abspath(f)
        d = os.path.dirname(f)
        if os.path.exists(d):
            if os.access(d, os.W_OK):
                w = f
            if os.path.exists(f):
                if os.access(f, os.W_OK):
                    return f
        elif os.access(os.path.dirname(d), os.W_OK):
            os.makedirs(d)
            w = f
    if w is None:
        print ("Cannot find suitable config path to write, create one in %s" % ' or '.join(search_config))
        raise Exception("No config file")
    return w

def send_command(name, command, args, config):
    if command == "on":
        ws = LGTVRemote(name, **config[name])
        ws.on()
        return
    else:
        try:
            args = parseargs(name, args)
        except Exception as e:
            usage(e.message)
            return
    try:
        ws = LGTVRemote(name, **config[name])
        ws.connect()
        if command is not None:
            ws.execute(command, args)
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()

def read_config_file(name, host):
    data = None
    config_file = name + "_" + host + ".json"
    if os.path.isfile(config) == True:
        with open(file) as f:
            data = json.load(f)
    return data

def pair_device(name, host):
    print("Start to authen device : %s - %s" % (name, host))
    workspace = os.path.join(os.path.expanduser("~"),".lgtv")
    filename = name + "_" + host + ".json"
    filename = os.path.join(workspace,filename)
    ws = LGTVAuth(name, host)
    ws.connect()
    ws.run_forever()
    sleep(1)
    config = ws.serialise()
    if filename is not None:
        with open(filename, 'w') as f:
            f.write(json.dumps(config))
        print ("Wrote config file: " + filename)

def read_devices_list(file):
    devices = None
    if os.path.isfile(file) == True:
        with open(file) as f:
            devices = json.load(f)
    return devices

def scan_devices(output_file):
    results = LGTVScan()
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
            data = []
            data.append({
                'uuid': it['uuid'],
                'model': it['model'],
                'address': it['address'],
            })
        with open(output_file, 'w+') as outfile:
            json.dump(data, outfile)
            
    else:
        print (json.dumps({
            "result": "failed",
            "count": len(results)
        }))
        return

# def main():
#     devices_list = os.path.join(workspace,'devices.json')
#     # Scan all devices
#     scan_devices(devices_list)

#     # Read devices list
#     devices = read_devices_list(devices_list)

#     # Pair devices
#     for item in devices:
#         pair_device(item['uuid'], item['address'])

#     # Send command
#     for item in devices:
#         config =  read_config_file(item['uuid'], item['address'])
#         name = item['uuid']
#         command = "off"
#         args = []
#         send_command(name, command, args, config)