import sys
import re

fileName = sys.argv[1]

# Read important values from file
f = open(fileName, 'r')
widthLine  = f.readline()
heightLine = f.readline()
byteLines  = f.read()

# Filter out the image name from the width field
imgName = re.split("_", re.split(" ", widthLine)[1])[0]
imgWidth = int(re.split(" ", widthLine)[2])
imgHeight = int(re.split(" ", heightLine)[2])

# Filter the byte values
byteLine = re.sub(r'\n',r'', byteLines)
byteValues = re.sub(r'.*{(.*)}.*', r'\1', byteLine)
byteValues = re.split(r',', byteValues)

# Borders :)
border = "+" + "-"*(imgWidth) + "+"

# Draw the image
print(imgName+ ":")
print(border)
for sb in byteValues:
    rowValue = int(sb, 16)
    sys.stdout.write("|")
    for i in range(imgWidth):
        pixelLoc = 2**i
        if (rowValue & pixelLoc) == pixelLoc:
            sys.stdout.write("+")
        else:
            sys.stdout.write(" ")
    print("|")
print(border)
