
'''with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)'''

filename = 'txt_files/pi_digits.txt'
'''with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())'''

with open(filename) as file_object:
    lines = file_object.readlines() #storing file content in a list --> lines

pi_string = '' #hold the content for later

for line in lines:
    pi_string += line.strip() #adding each line of the filename to pi_string 

print(pi_string)
print(len(pi_string))
