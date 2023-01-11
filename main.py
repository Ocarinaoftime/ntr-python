import argparse
import struct
import time
import pygame
import distutils.util
import sys
import os
from PyNTR.PyNTR import PyNTR

from pygame.locals import *

class n3ds:

    def __init__(self, client):
        self.client = client
    
    def update(self):
        base = 0x10400000

        combined_state = self.client.ReadU16(base + 0x60)
        [
            screen_state
        ] = (struct.unpack('hhhh', combined_state.to_bytes(4, 'little')))

        [
            self.isConsoleOpen
        ] = map(distutils.util.strtobool, list(format(screen_state, '016b'))[::-1])
    
    def p(self):
        print('=======================')
        print('screen on',     self.isConsoleOpen)
        print('=======================')




def color(s):
	try:
		(r,g,b) = map(int, s.split(','))
		return r,g,b
	except:
		raise argparse.ArgumentTypeError('Color must be r,g,b')


def main():
    parser = argparse.ArgumentParser(description='Input display for NTR connected 3DS')
    parser.add_argument('ip', metavar='IP', help='Local IP of your 3DS')
    parser.add_argument('-bg', '--background-color', metavar='COLOR', type=color, default='255,255,255', help='background color as 3 values, e.g. 255,255,255')
    args = parser.parse_args()
    print(args)

    pygame.init()

    client = PyNTR(args.ip)
    client.start_connection()
    client.send_hello_packet()
    pid = client.set_game_name('screen')

    display_width = 400
    display_height = 240

    new3ds_display = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()

    closed = False

    while not closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True


        new3ds_display.fill(args.background_color)


if __name__ == "__main__": main()