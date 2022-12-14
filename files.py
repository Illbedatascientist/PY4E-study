"""Exercise 1: Write a program to read through a file and print the contents 
of the file (line by line) all in upper case. """
#Let user choose a file name
fname = input('Enter a file name:')
fhand = open(fname)
for line in fhand:
    line = line.upper()
    print(line)

"""Exercise 2: Write a program to prompt for a file name, and then read through 
the file and look for lines of the form: X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the 
line to extract the floating-point number on the line. Count these lines and 
then compute the total of the spam confidence values from these lines. When you 
reach the end of the file, print out the average spam confidence."""

fname = input('Enter a file name:')
fhand = open(fname)
count=0
total=0
len = len('X-DSPAM-Confidence:')
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        value = float(line[len:])
        count+=1
        total+=value
Average = total/count
print('Average spam confidence:',Average)

"""Exercise 3: Sometimes when programmers get bored or want to have a bit of 
fun, they add a harmless Easter Egg to their program. Modify the program that 
prompts the user for the file name so that it prints a funny message when the 
user types in the exact file name “na na boo boo”. The program should behave 
normally for all other files which exist and don’t exist. Here is a sample 
execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt

python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt

python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!"""
fname = input('Enter a file name:')
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    count+=1
print('There were',count,'subject lines in',fname)