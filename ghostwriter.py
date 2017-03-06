import ssl

from PIL import Image
import websocket


img = Image.open('img.jpg')
data = img.getdata()

height = 256
width = 256

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
ws.connect("wss://ghost.life/")

for index in range(height*width):
    i = int(index / width)
    j = index % width
    color = data[index]

    color = int(sum(color) / 3.)
    ws.send(bytes([j,i, color]), opcode=websocket.ABNF.OPCODE_BINARY)

ws.close()
