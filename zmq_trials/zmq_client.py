import os, sys
import zmq

port = "9001"
'''
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)
'''

context = zmq.Context()
print "connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)

'''
if len(sys.argv) > 2:
    socket.connect("tcp://localhost: %s" % port1)
'''

socket.send("This is a trial string to check if the socket works or not")
message = socket.recv()
print("Recived reply: " , message)

'''
for request in range(1,10):
    print("sending request", request, "...")
    socket.send("Hello")
    message = socket.recv()
    print("Received reply ", request, "[", message, "]")
'''


