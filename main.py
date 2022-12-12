# This is the pong Game using turtle library
# OLD School Programing

import turtle
from time import sleep
import winsound
import time


def main():
    windows = turtle.Screen()
    windows.bgpic('new.png')
    windows.title("Pong by @NayanBastola")
    #windows.bgcolor("black")
    windows.setup(width=800, height=600)
    windows.tracer(0) #it stops windows from updating

    Player_1 = ""
    Player_2 = ""
    Player = ""
    Ai = "Computer"
    ballscount = ""
    verses = ""
    
    

    while True:
        winsound.PlaySound("openingscene.wav", winsound.SND_ASYNC)
        try:
            verses = str(windows.textinput("Game Type", "Enter (Ai | Player) for Gamemode: ")).lower()
            Player_1 = str(windows.textinput("Player 1", "Name of the player 1: "))
            if verses == "ai":
                Player = Ai
                Player_2 = Ai
            else:
                Player_2 = str(windows.textinput("Player 2", "Name of the player 2: "))
                Player = Player_2
            ballscount = int(windows.textinput("Balls Count", "Select Number of Balls (1 - 5): "))
        
        except ValueError:
            continue
        else:

            if Player_1 and Player_2 and (ballscount>=1 and ballscount<=5) and (verses == 'ai' or verses == 'player'):
                # Paddle A
                windows.bgpic('new2.png')
                paddleA = turtle.Turtle()
                paddleA.speed(0) #sets the speed for paddle to move
                paddleA.shape("square")
                paddleA.color("blue")
                paddleA.shapesize(stretch_wid=5, stretch_len=1)
                paddleA.penup()
                paddleA.goto(-350, 0)

                # Paddle B
                paddleB = turtle.Turtle()
                paddleB.speed(0) #sets the speed for paddle to move
                paddleB.shape("square")
                paddleB.color("red")
                paddleB.shapesize(stretch_wid=5, stretch_len=1)
                paddleB.penup()
                paddleB.goto(350, 0)

                # Ball 1
                ball1 = turtle.Turtle()
                ball1.speed(0) #sets the speed for paddle to move
                ball1.shape("circle")
                ball1.color("white")
                ball1.penup()
                ball1.goto(0, 0)
                    #ball 1 movement
                ball1.dx = 5 #delta X movement
                ball1.dy = -5 #movement of ball by 2px
                
                    #Ball 2
                ball2 = turtle.Turtle()
                ball2.speed(0) #sets the speed for paddle to move
                ball2.shape("circle")
                ball2.color("purple")
                ball2.penup()
                ball2.goto(0, 0)

                #ball 2 movement
                ball2.dx = -5 #delta X movement
                ball2.dy = -5 #movement of ball by 2px

                #Ball 3
                ball3 = turtle.Turtle()
                ball3.speed(0) #sets the speed for paddle to move
                ball3.shape("circle")
                ball3.color("green")
                ball3.penup()
                ball3.goto(0, 0)

                #ball 3 movement
                ball3.dx = 3 #delta X movement
                ball3.dy = 3 #movement of ball by 2px


                #Ball 4
                ball4 = turtle.Turtle()
                ball4.speed(0) #sets the speed for paddle to move
                ball4.shape("circle")
                ball4.color("yellow")
                ball4.penup()
                ball4.goto(0, 0)

                #ball 4 movement
                ball4.dx = -6 #delta X movement
                ball4.dy = 6 #movement of ball by 2px
               
                #Ball 5
                ball5 = turtle.Turtle()
                ball5.speed(0) #sets the speed for paddle to move
                ball5.shape("circle")
                ball5.color("magenta")
                ball5.penup()
                ball5.goto(0, 0)

                #ball 4 movement
                ball5.dx = -4 #delta X movement
                ball5.dy = 4 #movement of ball by 2px
                
                if ballscount == 1:
                    balls = [ball1]
                    ball2.hideturtle()
                    ball3.hideturtle()
                    ball4.hideturtle()
                    ball5.hideturtle()

                    # ball2.shape("None")
                    # ball3.shape("None")
                    # ball4.shape("None")
                    # ball5.shape("None")

                elif ballscount == 2:
                    balls = [ball1, ball2]
                    ball3.hideturtle()
                    ball4.hideturtle()
                    ball5.hideturtle()

                elif ballscount == 3:
                    balls = [ball1, ball2, ball3]
                    ball4.hideturtle()
                    ball5.hideturtle()

                elif ballscount == 4:
                    balls = [ball1, ball2, ball3, ball4]
                    ball5.hideturtle()
                else:
                    balls = [ball1, ball2, ball3, ball4, ball5]
                # Function

                def paddle_a_up():
                    y = paddleA.ycor() #getting the Y coordinate
                    y += 20 #adding 20px to Y coordinate
                    paddleA.sety(y)

                def paddle_a_down():
                    y = paddleA.ycor() #getting the Y coordinate
                    y -= 20 #Subtracting 20px to Y coordinate
                    paddleA.sety(y)

                def paddle_b_up():
                    y = paddleB.ycor() #getting the Y coordinate
                    y += 20 #adding 20px to Y coordinate
                    paddleB.sety(y)

                def paddle_b_down():
                    y = paddleB.ycor() #getting the Y coordinate
                    y -= 20 #Subtracting 20px to Y coordinate
                    paddleB.sety(y)

                #keyboard binding For Paddels   
                windows.listen() #listening to keyboard key press
                windows.onkeypress(paddle_a_up,"w")    
                windows.onkeypress(paddle_a_down,"s")
                windows.onkeypress(paddle_b_up,"Up")    
                windows.onkeypress(paddle_b_down,"Down")

                # Drawing Score on screen

                pen = turtle.Turtle()
                pen.speed(0) #animation Speed
                pen.color("White")
                pen.penup() #dont want line on screen
                pen.hideturtle()
                pen.goto(0, 260)
                pen.write("Player A ("+str(Player_1)+f"): 0  | Player B ("+ str(Player)+"): 0", align="center", font = ("Courier", 19, "bold"))

                pen2 = turtle.Turtle()
                pen2.speed(0) #animation Speed
                pen2.color("red")
                pen2.penup() #dont want line on screen
                pen2.hideturtle()
                pen2.goto(0, 230)
                pen2.write("Win at : 10 points", align="center", font = ("Courier", 14, "italic"))

                
                time_limit = 5
                start_time = time.time()
                timer = turtle.Turtle()
                timer.speed(0) #animation Speed
                timer.color("cyan")
                timer.penup() #dont want line on screen
                timer.hideturtle()
                timer.goto(300, 230)
                timer.write("Time : 0", align="right", font = ("Courier", 10, "normal"))

                # keeping Score
                scoreA = 0
                scoreB = 0


                # Main Game Loop
            
                while True:
                    sleep(0.03)
                    windows.update()
                    elasped_time = int(time.time() - start_time)
                    timer.clear()
                    timer.write("Time : {}".format(elasped_time), align="right", font = ("Courier", 10, "normal"))
            
                    for ball in balls:
                        #ball movement
                        ball.setx(ball.xcor() + ball.dx)
                        ball.sety(ball.ycor() + ball.dy)

                        #what happens if ball touch the border

                        if ball.ycor() > 290:
                            ball.sety(290)
                            ball.dy *= -1 #reverse the direction.
                            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

                        if ball.ycor() < -290:
                            ball.sety(-290)
                            ball.dy *= -1 #reverse the direction
                            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

                        if ball.xcor() > 390:
                            ball.goto(0,0)
                            ball.dx *= -1 #reverse the direction.
                            scoreA += 1
                            pen.clear()
                            pen.write("Player A ("+str(Player_1)+f"): {scoreA}  | Player B ("+ str(Player)+"): {}".format(scoreB), align="center", font = ("Courier", 19, "bold"))
                            winsound.PlaySound("score.wav", winsound.SND_ASYNC)

                        if ball.xcor() < -390:
                            ball.goto(0,0)
                            ball.dx *= -1 #reverse the direction
                            scoreB += 1
                            pen.clear()
                            pen.write("Player A ("+str(Player_1)+f"): {scoreA}  | Player B ("+ str(Player)+"): {}".format(scoreB), align="center", font = ("Courier", 19, "bold"))
                            winsound.PlaySound("score.wav", winsound.SND_ASYNC)

                        #bouncing the ball on paddle

                        if (ball.xcor() > 325 and ball.xcor() < 345) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
                            ball.setx(325)
                            ball.dx *= -1
                            winsound.PlaySound("touch.wav", winsound.SND_ASYNC)

                        if (ball.xcor() < -325 and ball.xcor() > -345) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
                            ball.setx(-325)
                            ball.dx *= -1
                            winsound.PlaySound("touch.wav", winsound.SND_ASYNC)
                        
                    
                        # FOR AI MODE

                        if verses == 'ai':
                            closest_ball = balls[0] #looking which one is the closest to the paddle
                            for ball in balls:
                                if ball.xcor() > closest_ball.xcor():
                                    closest_ball = ball

                            if paddleB.ycor() < closest_ball.ycor() and abs(paddleB.ycor() - closest_ball.ycor()) > 10:
                                paddle_b_up()
                            elif paddleB.ycor() > closest_ball.ycor()and abs(paddleB.ycor() - closest_ball.ycor()) > 10:
                                paddle_b_down()

                        if scoreA >= 10:
                            winsound.PlaySound("winner.wav", winsound.SND_ASYNC)
                            restart = windows.textinput("🍾🎉 Congratulations! 🎉🎊", Player_1 + ", You won ! \nDo you want to restart ? (y/n)").lower()
                            if restart == "y":
                                windows.clearscreen()
                                main()
                            else:
                                break
                        if scoreB >= 10:
                            winsound.PlaySound("winner.wav", winsound.SND_ASYNC)
                            restart = windows.textinput("🍾🎉 Congratulations! 🎉🎊", Player_2 + ", You won ! \nDo you want to restart ? (y/n)").lower()
                            if restart == "y":
                                windows.clearscreen()
                                main()
                            else:
                                break
                break
main()