#!/usr/bin/env python

import argparse
import zmq

context = zmq.Context()

socket = context.socket(zmq.DEALER)

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--connect-address', default='tcp://127.0.0.1:5555')
parser.add_argument('-i', '--city')

args = parser.parse_args()

socket.connect(args.connect_address)

# First just register to the server
socket.send_multipart([args.city])
print socket.recv_json()
