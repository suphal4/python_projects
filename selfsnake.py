from tkinter import *
import random
run=True
cheat=False
cheat2=False
boss=False
width = 1280 
height = 720
def leftKey(event):
    global direction
    direction = "left"
def rightKey(event):
    global direction
    direction = "right"
def upKey(event):
    global direction
    direction = "up"
def downKey(event):
    global direction
    direction = "down"
def setWindowDimensions(w,h):
    window = Tk()
    window.title("Snake Game")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2) 
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window
window = setWindowDimensions(width, height)
root=Frame(window)
root.pack(expand=True,fill="both")
game=Frame(window)
canvas = Canvas(game, bg="grey", width=width, height=height)
picture=PhotoImage(file="bosskey.png")

snake = []

snakeSize = 15
snake.append(canvas.create_rectangle(snakeSize,snakeSize, snakeSize *
2, snakeSize * 2, fill="white" ))
score = 0
txt = "Score:" + str(score)
scoreText = canvas.create_text( width/2 , 10 , fill="white" ,font="Trajan 20  bold", text=txt)

direction = "right"

def placeFood():
    global food, foodX, foodY
    food = canvas.create_rectangle(0,0, snakeSize, snakeSize, fill="steel blue" )


    foodX = random.randint(0,width-snakeSize)
    foodY = random.randint(0,height-snakeSize)
    canvas.move(food, foodX, foodY)
def moveSnake():
    global run,positions
    canvas.pack()
    positions = []
    positions.append(canvas.coords(snake[0]))
    if run:
        
        if positions[0][0] < 0:
            canvas.coords(snake[0],width,positions[0][1],width-snakeSize,positions[0][3])
        elif positions[0][2] > width:
            canvas.coords(snake[0],0-snakeSize,positions[0][1],0,positions[0][3])
        elif positions[0][3] > height:
            canvas.coords(snake[0],positions[0][0],0-snakeSize,positions[0][2],0)
        elif positions[0][1] < 0:
            canvas.coords(snake[0],positions[0][0],height,positions[0][2],height-snakeSize)
        positions.clear()
        positions.append(canvas.coords(snake[0]))
        if direction == "left":
            canvas.move(snake[0], -snakeSize,0)
        elif direction == "right":
            canvas.move(snake[0], snakeSize,0)
        elif direction == "up":
            canvas.move(snake[0], 0,-snakeSize)
        elif direction == "down":
            canvas.move(snake[0], 0,snakeSize)
        sHeadPos = canvas.coords(snake[0])
        foodPos = canvas.coords(food)
        if overlapping(sHeadPos, foodPos):
            moveFood()


            growSnake()
        
        for i in range(1,len(snake)):
            if overlapping(sHeadPos, canvas.coords(snake[i])):
                gameOver = True

                
        for i in range(1,len(snake)):
            positions.append(canvas.coords(snake[i]))

        for i in range(len(snake)-1):
            canvas.coords(snake[i+1],positions[i][0], positions[i][1],positions[i][2],positions[i][3])
        if not cheat2:
            
            if 'gameOver' not in locals():
                window.after(90, moveSnake)
            else:
                canvas.create_text(width/2,height/2,fill="white",font="Trajan 20  bold", text="Game Over!")
                file=open("snakeleaderboard.txt","a+")

        else:
            window.after(90,moveSnake)
        
def overlapping(a,b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True

        return False
def moveFood():
    global food, foodX, foodY
    canvas.move(food, (foodX*(-1)), (foodY*(-1)))
    foodX = random.randint(0,width-snakeSize)
    foodY = random.randint(0,height-snakeSize)
    canvas.move(food, foodX, foodY)

def growSnake():
    lastElement = len(snake)-1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_rectangle(0,0, snakeSize,snakeSize,fill="#FDF3F3"))
    if (direction == "left"):
        canvas.coords(snake[lastElement+1],lastElementPos[0]+snakeSize,lastElementPos[1],lastElementPos[2]+snakeSize,lastElementPos[3])
    elif (direction == "right"):
        canvas.coords(snake[lastElement+1],lastElementPos[0] -snakeSize,lastElementPos[1],lastElementPos[2] -snakeSize,lastElementPos[3])
    elif (direction == "up"):
        canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]+snakeSize,lastElementPos[2],lastElementPos[3]+snakeSize)
    else:
        canvas.coords(snake[lastElement+1],lastElementPos[0],lastElementPos[1]-snakeSize,lastElementPos[2],lastElementPos[3]-snakeSize)
    global score,cheat
    if cheat:
        score += 20
    else:
        score += 10
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)
def space(event):
    global run
    if run:
        run=False
    else:
        run=True
        
        moveSnake()

def double(event):
    global cheat
    if not cheat:
        cheat=True
def neverdie(event):
    global cheat2
    if not cheat2:
        cheat2=True
    else:
        cheat2=False
def bosskey(event):
    global boss
    if boss:
        boss=False
    else:
        boss=True
        canvas.create_image(0,0,image=picture,anchor="nw")

def start():
    game.pack(expand=True,fill="both")
    root.forget()
    canvas.bind("<Left>", leftKey)
    canvas.bind("<Right>", rightKey)
    canvas.bind("<Up>", upKey)
    canvas.bind("<Down>", downKey)
    canvas.focus_set()
         
    canvas.bind("<space>",space)
    canvas.bind("<Return>",bosskey)
    canvas.bind("<Control-x>",double)
    canvas.bind("<Control-a>",neverdie)
    placeFood()
    moveSnake()
def main():
    canvasi = Canvas(root, bg="grey", width=width, height=height)
    canvasi.pack()
    title=canvasi.create_text(625,200,text="THE SNAKE GAME!",font="Trajan 25 ")
    
    root.pack(expand=True,fill="both")
    game.forget()
    button=Button(root,text="start",bd="5",command=start,width=30,height=2)
    button.place(x=520, y=330)
    button2=Button(root,text="exit",bd="5",command=window.destroy,width=30,height=2)
    button2.place(x=520, y=390)
    
main()
window.mainloop()

