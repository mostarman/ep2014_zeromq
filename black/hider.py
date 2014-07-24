#!/usr/bin/env python
import argparse
import zmq
from zmq.eventloop import ioloop, zmqstream
import json


io_loop = ioloop.IOLoop()

context = zmq.Context()

socket = context.socket(zmq.ROUTER)
stream = zmqstream.ZMQStream(socket, io_loop=io_loop)

def handle_guess(stream, message):
    id, guess = message
    reply = 'CORRECT' if guess == args.city else 'INCORRECT'
    stream.send_multipart([id, json.dumps(reply)])

stream.on_recv_stream(handle_guess)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bind-address', default='tcp://0.0.0.0:5555')
parser.add_argument('-c', '--city')

args = parser.parse_args()

socket.bind(args.bind_address)
io_loop.start()
