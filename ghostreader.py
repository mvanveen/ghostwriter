import ssl
import sys

import pygame
import websocket

pygame.init()

size = width, height = 256, 256

screen = pygame.display.set_mode(size)
info = pygame.display.Info()


def on_open(ws):
    pass
def on_message(ws, message):
    #img = bytes(message)
    i = 0;

    while i < len(message):
        pixel = message[i:i+3]
        pixel_height = pixel[0]
        pixel_width = pixel[1]
        pixel_color = pixel[2]
        #print(i)
        i += 3
        pixel_color = pygame.Color(pixel_color, pixel_color, pixel_color, 255)
        screen.set_at((pixel_height, pixel_width), pixel_color)
        #print("drew pixel %s %s %s" % (pixel_height, pixel_width, pixel_color))
        pygame.display.update()

websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://ghost.life/", on_message=on_message)
ws.on_open = on_open
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


print(info)
while True:
   pass
