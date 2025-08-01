
# import required modules
import turtle
import time
import random


delay = 0.1
score = 0
hight_score = 0

# create a window screen
wn = turtle.Screen()
wn.title("Snake game Elmohandes Academy")
wn.bgcolor("#2aec62")
wn.setup(width = 600 , height=600)
wn.cv._rootwindow.resizable(False,False)
wn.tracer(0)


# create head of snake

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.speed(0)
head.goto(0,0)
head.direction = 'Stop'



# create food

food = turtle.Turtle()
colors = random.choice(['red','black','green','yellow','orange'])
shapes = random.choice(['square','circle'])
food.color(colors)
food.shape(shapes)
food.penup()
food.speed()
food.goto(0,100)


# create pen
pen = turtle.Turtle()
pen.shape("square")
pen.color('white')
pen.penup()
pen.speed(0)
pen.goto(0,250)
pen.hideturtle()
pen.write("Score: 0   High Score: 0",align="center" , font=("Arial",24,"bold"))


# assigning direction

def goup():
    if head.direction != 'down':
        head.direction = 'up'

def godown():
    if head.direction != 'up':
        head.direction = 'down'

def goright():
    if head.direction != 'left':
        head.direction = 'right'

def goleft():
    if head.direction != 'right':
        head.direction = 'left'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


# key listen
wn.listen()
wn.onkeypress(goup,'w')
wn.onkeypress(godown,'s')
wn.onkeypress(goright,'d')
wn.onkeypress(goleft,'a')

segments = []




# Function to update the screen
def update_screen():
    wn.update()
    time.sleep(delay)


# Main loop
while True:
    update_screen()



    # when snake touch border
    if(
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290):

        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        colors = random.choice(['red','black','green','yellow','orange'])
        shapes = random.choice(['square','circle'])
        food.color(colors)
        food.shape(shapes)
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        score =0
        delay = 0.1
        pen.clear()
        pen.write(
            f"Score: {score}   High Score: {hight_score}",
            align="center" ,
            font=("Arial",24,"bold"))


    # if head touch food
    if head.distance(food) < 20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.color('orange')
        new_segment.speed(0)
        new_segment.penup()

        segments.append(new_segment)
        delay -= 0.001
        score += 10

        if score > hight_score:
            hight_score = score

        pen.clear()
        pen.write(
            f"Score: {score}  High Score: {hight_score}",
            align='center',
            font=('Arial',24 , 'bold')

            )
    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()   


    #snake touch body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            colors = random.choice(['red','black','green','yellow','orange'])
            shapes = random.choice(['square','circle'])
            food.color(colors)
            food.shape(shapes)
            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(
                f"Score: {score}   High Score: {hight_score}",
                align="center" ,
                font=("Arial",24,"bold"))
            

  

   





















