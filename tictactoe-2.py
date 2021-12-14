from graphics import *
import re
import time

def isBetween(point1, point2, point3):
    return (point1.getX() >= point2.getX() and point1.getX() <= point3.getX()) and (point1.getY() >= point2.getY() and point1.getY() <= point3.getY())

def isWin(selections, value):
    winningIndex = []
    winningIndex.append([0, 1, 2])
    winningIndex.append([3, 4, 5])
    winningIndex.append([6, 7, 8])
    winningIndex.append([0, 3, 6])
    winningIndex.append([1, 4, 7])
    winningIndex.append([2, 5, 8])
    winningIndex.append([0, 4, 8])
    winningIndex.append([2, 4, 6])
    for indexes in winningIndex:
        count = 0
        for index in indexes:
            if selections[index] == value:
                count += 1
        if count == 3:
            return True
    return False

def isAllFilled(selections):
    result = True
    for selection in selections:
        if selection == 0:
            result = False
            break
    return result
    
def findAIPosition(selections):
    winningIndex = []
    winningIndex.append([0, 1, 2])
    winningIndex.append([3, 4, 5])
    winningIndex.append([6, 7, 8])
    winningIndex.append([0, 3, 6])
    winningIndex.append([1, 4, 7])
    winningIndex.append([2, 5, 8])
    winningIndex.append([0, 4, 8])
    winningIndex.append([2, 5, 8])
    winningIndex.append([2, 4, 6])

    pos = -1
    for indexes in winningIndex:
        pos = -1
        count = 0
        zeroCount = 0
        for index in indexes:
            if selections[index] == 2:
                count += 1
            elif selections[index] == 0:
                pos = index
                zeroCount += 1
        if pos != -1 and zeroCount == 1 and count == 2:
            return pos

    pos = -1
    for indexes in winningIndex:
        pos = -1
        count = 0
        zeroCount = 0
        for index in indexes:
            if selections[index] == 1:
                count += 1
            elif selections[index] == 0:
                pos = index                
                zeroCount += 1
        if pos != -1 and zeroCount == 1 and count == 2:
            return pos
            

    
    pos = -1
    index = 0
    for value in selections:
        if value == 0:
            pos = index
            break
        index += 1
    return pos
        
           

def main():
    win = GraphWin('TicTacToe Game', 300, 400)
    
    # Rectangles
    rectangles = []
    rectangles.append(Rectangle(Point(2, 2), Point(100, 100)))
    rectangles.append(Rectangle(Point(100, 2), Point(198, 100)))
    rectangles.append(Rectangle(Point(198, 2), Point(298, 100)))
    rectangles.append(Rectangle(Point(2, 100), Point(100, 198)))
    rectangles.append(Rectangle(Point(100, 100), Point(198, 198)))
    rectangles.append(Rectangle(Point(198, 100), Point(298, 198)))
    rectangles.append(Rectangle(Point(2, 198), Point(100, 296)))
    rectangles.append(Rectangle(Point(100, 198), Point(198, 296)))
    rectangles.append(Rectangle(Point(198, 198), Point(298, 296)))
    
    selections = [0,0,0,0,0,0,0,0,0]
    
    for rect in rectangles:
        rect.setWidth(2)
        rect.setOutline('green')
        rect.draw(win)
        
    rectForText = Rectangle(Point(50,340),Point(250,370))
    rectForText.setWidth(2)
    rectForText.setOutline('Cyan')
    rectForText.draw(win)
    textMessage = Text(Point(140,355),'Your Turn')
    textMessage.setTextColor('brown')
    textMessage.setSize(15)
    textMessage.draw(win)
    
    pt = win.getMouse()
    
    your_turn = True
        
    while True:
        if isAllFilled(selections):
            break
        if your_turn:
            found = False
            rectangle = None
            pos = 0
            for rect in rectangles:
                if isBetween(pt, rect.p1, rect.p2):
                    found = True
                    rectangle = rect
                    break
                pos += 1
            if found:
                if selections[pos] == 0:
                    x = (rectangle.p1.x + rectangle.p2.x) / 2
                    y = (rectangle.p1.y + rectangle.p2.y) / 2
                    img = Image(Point(x,y), 'you.png')
                    img.draw(win)
                    selections[pos] = 1
                    your_turn = False
                    if isWin(selections , 1):
                        textMessage.setText("You Win!!!")
                        time.sleep(2)
                        textMessage.setText('Exiting')
                        time.sleep(3)
                        win.close()
                    else:
                        textMessage.setText("Computer Turn")
                else:
                    pt = win.getMouse()                    
            else:
                pt = win.getMouse()
        else:
            pos = findAIPosition(selections)
            if pos != -1:
                x = (rectangles[pos].p1.x + rectangles[pos].p2.x) / 2
                y = (rectangles[pos].p1.y + rectangles[pos].p2.y) / 2
                time.sleep(0.5)
                img = Image(Point(x, y), 'comp.png')
                img.draw(win)
                selections[pos] = 2
                your_turn = True
                if isWin(selections, 2):
                    textMessage.setText("Computer Win!!!")
                    time.sleep(2)
                    textMessage.setText('Exiting')
                    time.sleep(3)
                    win.close()

                else:
                    textMessage.setText("Your Turn")
                pt = win.getMouse()
            
    win.close()
    
    
main()