#!/bin/python
import websocket
import thread
import time
import pickle
from command import Command
from messages import GpioCommand


parameters = dict()

parameters['Par1'] = 1
parameters['Par2'] = 'dos'
com = GpioCommand(1,'this','GPIO1','HIGH')

serialized = pickle.dumps(com)

ip = 'ws://'
12
x = input("Enter ip: \n")
ip = ip + x
x = input("Enter port: \n")
ip = ip+':' + x




def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    def run(*args):

        time.sleep(1)
        ws.send(serialized)
        time.sleep(1)
        ws.close()
        print "thread terminating..."
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ip,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
