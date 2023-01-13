import argparse
import struct
import time
import pygame
import distutils.util
import sys
import os
from PyNTR.PyNTR import PyNTR



def main():

    parser = argparse.ArgumentParser(description='Input display for NTR connected 3DS')
    parser.add_argument('ip', metavar='IP', help='Local IP of your 3DS')
    args = parser.parse_args()
    print(args)

    client = PyNTR(args.ip)
    client.start_connection()
    client.send_hello_packet()
    pid = client.set_game_name('sound')

    addr = 0x1EC0340C
    leng = addr + 0x4

    closed = False

    while not closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
        
        client.send_read_memory_packet(addr, leng)
