import turtle

def drawSquare(tname,color,size):
    tname.fillcolor(color)
    tname.begin_fill()
    tname.speed(0)
    for i in range(4):
        tname.forward(size)
        tname.left(90)
    tname.end_fill()
    tname.forward(15)

def main():
    wn=turtle.Screen()
    character=turtle.Turtle()
    character.pensize(3)
    character.penup()
    character.goto(-200,-200)
    character.pendown()

#first row
    for i in range(24):
        drawSquare(character,"white",15)

#second row
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(7):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(6):
        drawSquare(character,"black",15)
    for i in range(9):
        drawSquare(character,"white",15)

#third row
    newRow(character,13,1)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(6):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(9):
        drawSquare(character,"white",15)

#fourth row
    newRow(character,13,1)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(9):
        drawSquare(character,"white",15)

#fifth row
    newRow(character,13,1)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"red",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"red",15)
    for i in range(4):
        drawSquare(character,"black",15)
    for i in range(9):
        drawSquare(character,"white",15)

#sixth row
    newRow(character,13,1)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(11):
        drawSquare(character,"white",15)

#seventh row
    newRow(character,13,1)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(10):
        drawSquare(character,"white",15)

#eigth row
    newRow(character,13,1)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(5):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(9):
        drawSquare(character,"white",15)

#ninth row
    newRow(character,13,1)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(2):
        for i in range(1):
            drawSquare(character,"white",15)
        for i in range(1):
            drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(5):
        drawSquare(character,"black",15)
    for i in range(6):
        drawSquare(character,"white",15)

#tenth row
    newRow(character,13,1)
    for i in range(2):
        for i in range(1):
            drawSquare(character,"white",15)
        for i in range(1):
            drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"green",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"white",15)

#eleventh row
    newRow(character,13,1)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(6):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"white",15)

#twelfth row
    newRow(character,13,1)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"white",15)

#thirteenth row
    newRow(character,13,1)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"white",15)

#fourteenth row
    newRow(character,13,1)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"green",15)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"white",15)

#fifteenth row
    newRow(character,13,1)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"red",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"green",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(6):
        drawSquare(character,"white",15)

#sixteenth row
    newRow(character,13,1)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(7):
        drawSquare(character,"white",15)

#seventeenth row
    newRow(character,13,1)
    for i in range(5):
        drawSquare(character,"white",15)
    for i in range(5):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(6):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"white",15)

#eighteenth row
    newRow(character,13,1)
    for i in range(7):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(4):
        drawSquare(character,"green",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"white",15)

#nineteenth row
    newRow(character,13,1)
    for i in range(7):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(7):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)

#twentieth row
    newRow(character,13,1)
    for i in range(6):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(8):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)

#twenty-first row
    newRow(character,13,1)
    for i in range(6):
        drawSquare(character,"white",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(8):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)

#twenty-second row
    newRow(character,13,1)
    for i in range(5):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(9):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)

#twenty-third row
    newRow(character,13,1)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(9):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)

#twenty-four row
    newRow(character,13,1)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"green",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(5):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)

#twenty-five row
    newRow(character,13,1)
    for i in range(5):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(14):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"white",15)

#twenty-six row
    newRow(character,13,1)
    for i in range(6):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"green",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"white",15)

#twenty-seven row
    newRow(character,13,1)
    for i in range(6):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"red",15)
    for i in range(2):
        drawSquare(character,"black",15)
    for i in range(7):
        drawSquare(character,"white",15)
    for i in range(3):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"white",15)

#twenty-eight row
    newRow(character,13,1)
    for i in range(6):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"red",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(3):
        drawSquare(character,"white",15)
    for i in range(3):
        for i in range(1):
            drawSquare(character,"black",15)
        for i in range(1):
            drawSquare(character,"white",15)
    for i in range(4):
        drawSquare(character,"white",15)

#twenty ninth row
    newRow(character,13,1)
    for i in range(7):
        drawSquare(character,"white",15)
    for i in range(4):
        drawSquare(character,"black",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(2):
        drawSquare(character,"white",15)
    for i in range(3):
        for i in range(1):
            drawSquare(character,"black",15)
        for i in range(1):
            drawSquare(character,"white",15)
    for i in range(4):
        drawSquare(character,"white",15)

#thirteeth row
    newRow(character,13,1)
    for i in range(10):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(2):
        drawSquare(character,"green",15)
    for i in range(4):
        drawSquare(character,"white",15)
    for i in range(1):
        drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(5):
        drawSquare(character,"white",15)

#thirty first row
    newRow(character,13,1)
    for i in range(11):
        drawSquare(character,"white",15)
    for i in range(2):
        for i in range(1):
            drawSquare(character,"black",15)
        for i in range(2):
            drawSquare(character,"green",15)
    for i in range(1):
        drawSquare(character,"black",15)
    for i in range(6):
        drawSquare(character,"white",15)

#thirty second row
    newRow(character,13,1)
    for i in range(12):
        drawSquare(character,"white",15)
    for i in range(2):
        for i in range(2):
            drawSquare(character,"black",15)
        for i in range(1):
            drawSquare(character,"white",15)
    for i in range(6):
        drawSquare(character,"white",15)




def newRow(tname,size,num):
    tname.left(90)
    tname.forward(15)
    tname.left(90)
    tname.forward(360)
    tname.right(180)

main()
