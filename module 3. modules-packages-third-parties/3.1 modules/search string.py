
import os
import mmap
# Example to search for a string in text file


def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if word in content:
            print('string exist in a file')
        else:
            print('string does not exist in a file')


print(search_str(r'/Users/carlosinfante/Desktop/winc-academy/backend-course/testing/modules-packages-third_parties/sales.txt', 'laptop'))


# string to search in file
word = 'laptop'
with open(r'/Users/carlosinfante/Desktop/winc-academy/backend-course/testing/modules-packages-third_parties/sales.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)


# Efficient way to search string in a large text file
'''
All above way read the entire file in memory. If the file is large, reading the whole file in memory is not ideal.

In this section, we’ll see the fastest and most memory-efficient way to search a string in a large text file.
'''
with open(r'/Users/carlosinfante/Desktop/winc-academy/backend-course/testing/modules-packages-third_parties/sales.txt', 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if 'laptop' in line:
            print('string found in a file')
            print('Line Number:', l_no)
            print('Line:', line)
            # don't look for next lines
            break


# mmap to search for a string in text file


with open(r'/Users/carlosinfante/Desktop/winc-academy/backend-course/testing/modules-packages-third_parties/sales.txt', 'rb', 0) as file:
    s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    if s.find(b'laptop') != -1:
        print('string exist in a file')


# Search string in multiple files

word = 'password'
dir_path = r'/Users/carlosinfante/Documents/Winc/files/cache'
# iterate each file in a directory
for file in os.listdir(dir_path):
    cur_path = os.path.join(dir_path, file)
    # check if it is a file
    if os.path.isfile(cur_path):
        with open(cur_path, 'r') as file:
            # read all content of a file and search string
            if word in file.read():
                print('string found', file)


# Search file for a list of strings

words = ['laptop', 'phone']
with open(r'/Users/carlosinfante/Desktop/winc-academy/backend-course/testing/modules-packages-third_parties/sales.txt', 'r') as f:
    content = f.read()
# Iterate list to find each word
for word in words:
    if word in content:
        print('string exist in a file', word)


# Assign thevariables
source_location = '/Users/carlosinfante/Documents/Winc/files/cache/'
search_string = 'password'

# list all the files in source location
direct = os.listdir(source_location)

# Create an empty list
file_list = ''

# For loop to search for the string

# Tutorial
# https://www.youtube.com/watch?v=XCyC44ktCA0
for file in direct:
    f = open(source_location + file, 'r')
    if search_string in f.read():
        file_list = file
        file_path = open(source_location + file, 'r')
        for l_no, line in enumerate(file_path):
            # search string
            if search_string in line:
                print('string found in a file')
                print('Line Number:', l_no)
                print('Line:', line)
                index_pass = line.find(':') + 2
                passd = line[index_pass:]
                print(passd)

                # don't look for next lines
                break

    f.close()

print('list of files with passwords:\n', file_list)
