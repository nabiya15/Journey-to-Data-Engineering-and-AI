fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('Invalid file name')
    quit()

for line in fh:
    print(line.upper().rstrip())

