
import socket
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import urllib.request
import io
import binascii

def twoscomplement_to_unsigned(i):
    return i % 256

HOST = "192.168.0.27"  # Standard loopback interface address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)


print("Server is running on IP: " + HOST + " and port: " + str(PORT))

# while(True):
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(999999999)
            # if not data:
            #     break
            sizeOfPacket = int.from_bytes(data[:4].decode('utf-8'), byteorder='big')

            bytesRead = 0
            data = data[4:]
            while(bytesRead < sizeOfPacket):
                newdata = conn.recv(999999999)
                data += newdata[:sizeOfPacket - bytesRead]
                bytesRead += data.__sizeof__()
                dataBytesIO = io.BytesIO(data)
                image = Image.open(dataBytesIO)
                image.show()
                # while(True):
                #     print("Waiting for data...")
            # stream = io.BytesIO(r_data)
            # img = Image.open(stream)
            # draw = ImageDraw.Draw(img)

            
            

