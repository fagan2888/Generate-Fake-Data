import binascii
import time
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
file_path = tkFileDialog.askopenfilename()

of = open('Addresses.txt', 'wb')
start_time = time.time()
with open(file_path, "r") as f:
    data = ""
    lines = f.read()
    n = int(lines, 2)
    of.write(binascii.unhexlify('%x' % n))
    of.flush()
of.close()
end_time = time.time()
print("Total execution time: " + str(start_time-end_time))