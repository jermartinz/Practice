#3.1

from asyncio import transports
from email import message
from unicodedata import name


names = ["Hector", "Seba", "Pablo"]

print(names[0])
print(names[1])
print(names[2])

#3.2

print(f"My friend {names[0]}")

#3.3
transports = ["car", "airplane", "motorcyle"]

message = f"I would like to own a Tesla {transports[0]}"

print(message)
