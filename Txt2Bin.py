import binascii
import time
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
file_path = tkFileDialog.askopenfilename()

of = open('outputfile.bin', 'wb')
start_time = time.time()
with open(file_path, "r") as f:
    data = ""
    lines = f.readlines()
    for line in lines:
        data = data + line.strip()
    of.write(bin(int(binascii.hexlify(data), 16)))
    of.flush()
of.close()
end_time = time.time()
print("Total execution time: " + str(start_time-end_time))
