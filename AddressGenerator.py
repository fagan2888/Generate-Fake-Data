import pip
pip.main(['install', 'faker'])
import os
from faker import Factory
from datetime import datetime

fake = Factory.create()
record_size = raw_input("Enter how many records of addresses this program should generate: ")

print("Propagating " + record_size + " addresses...")
startTime = datetime.now()
record_size = int(record_size)
text_file = open("PropagatedAddresses.txt", "w")
index = 0
bad = ["FPO", "DPO", "AP", "-"]  # removing military bases from data
while index <= record_size:
    badAddress = False
    address = fake.address()
    address = str(address).replace("\n", " ")
    for i in bad:
        if i in address:
            badAddress = True
    if badAddress:
        continue
    else:
        text_file.write(address)
        text_file.write("\n")
        text_file.flush()
        index += 1
text_file.close()
print("")
print("Your data has been created at: " + os.path.abspath("PropagatedAddresses.txt"))
print ("Total execution time: " + str((datetime.now() - startTime)))
