f = open('inputFile.txt', 'r')
#print(f.read()) reads all

#find only passers
#count = 0

for line in f:
    #print(str(count) + line)
    #count = count + 1
    line_split = line.split()
    if line_split[2] == "P":
        print(line)
        
f.close()