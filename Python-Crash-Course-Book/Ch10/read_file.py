
#10.1
file_name = 'txt_files/learning_python.txt'

'''with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())'''

with open(file_name) as file_object:
    lines = file_object.readlines()
    print(lines)

file_string = ''

for line in lines:
    file_string += line



print(file_string.replace('Python', 'C'))

#10.2
