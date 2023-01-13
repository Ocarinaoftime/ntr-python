import argparse
import struct
import pygame
import distutils.util
from PyNTR.PyNTR import PyNTR

class SoundState:

	def __init__(self, client):
		self.client = client

	def update(self):
		base = 0x1EC03000

		combined_state = self.client.ReadU64(base + 0x40C)
		[
            sound_state
		] = (struct.unpack('hhhh', combined_state.tobytes(8, 'little')))

		[
			self.volume_level,
			_,_,_,_,
		] = map(distutils.util.strtobool, list(format(sound_state, '016b'))[::-1])

	def p(self):
		print('=======================')
		print('button_a',     self.volume_level)
		print('=======================')

def main():

    parser = argparse.ArgumentParser(description='Input display for NTR connected 3DS')
    parser.add_argument('ip', metavar='IP', help='Local IP of your 3DS')
    args = parser.parse_args()
    print(args)

    pygame.init()

    client = PyNTR(args.ip)
    client.start_connection()
    client.send_hello_packet()
    pid = client.set_game_name('hid')

    sound_state = SoundState(client)

    addr = 0x1EC0340C
    leng = addr + 0x4

    closed = False

    clock = pygame.time.Clock()

    while not closed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True

        sound_state.update()
        sound_state.p()

        client.send_read_memory_packet(addr, 8)
        clock.tick(60)
    




if __name__ == "__main__": main()