import argparse
import struct
import time
import pygame
import distutils.util
import sys
import os
from PyNTR.PyNTR import PyNTR

ip = "10.7.41.10"

def main():

    client = PyNTR(ip)
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
