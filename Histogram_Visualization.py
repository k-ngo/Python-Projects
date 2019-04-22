# By Khoa Ngo
# This program performs the following functions:
# 1. Prompt user to enter the names for the title, column 1 header, and column 2 header.
# 2. Prompt user to enter data points in the format 'string, integer'.
#    The string will be stored in column 1, the integer will be stored in column 2.
# 3. Check the data entries to see if the following conditions are met:
# 	  I. There is one and only one comma in the entry.
# 	  II. The value after the comma must be an integer.
# 4. If the conditions are met, the data will be presented in a table.
# 5. A simple histogram will be made to visualize the data.

title = input('Enter a title for the data:\n')
print('You entered:', title)

header1 = input('\nEnter the column 1 header:\n')
print('You entered:', header1)
header2 = input('\nEnter the column 2 header:\n')
print('You entered:', header2)

data = input('\nEnter a data point (-1 to stop input):\n')
string = []
integer = []

while data != '-1':
    if ',' in data:
        split_data = data.split(',')
        split_data[1] = split_data[1].replace(' ', '')
        if len(split_data) > 2:
            print('Error: Too many commas in input.')
        elif split_data[1].isdigit() == False:
            print('Error: Comma not followed by an integer.')
        else:
            print('Data string:', split_data[0])
            print('Data integer:', split_data[1])
            string.append(split_data[0])
            integer.append(int(split_data[1]))
    else:
        print('Error: No comma in string.')
    data = input('\nEnter a data point (-1 to stop input):\n')

print()
print(title.rjust(33))
print(header1.ljust(19), '|', header2.rjust(22))
print('--------------------------------------------')
for count in range(len(string)):
    print(string[count].ljust(19), '|', str(integer[count]).rjust(22))
    count += 1
print()
for count in range(len(string)):
    print(string[count].rjust(20), '*'*integer[count])
    count += 1
