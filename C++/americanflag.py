import sys

def printOut(a):
        sys.stdout.write(a)
        
for i in range(15):
    if (i <= 9):
        if i % 2 == 0 or i == 0:
            for j in range(30):
                if j <= 11:
                    if j % 2 == 0 or j == 0:
                        printOut("*")
                        j += 1
                    else:
                        printOut(" ")
                        j += 1
                else:
                    printOut("=")
            sys.stdout.flush()
        else:
            for j in range(30):
                if j <= 11:
                    if j % 2 == 0 or j == 0:
                        printOut(" ")
                        j += 1
                    else:
                        printOut("*")
                        j += 1
                else:
                    printOut("=")
    else:
        for j in range(30):
            printOut("=")
            j += 1
    sys.stdout.flush()
    printOut("\n")
        
            

