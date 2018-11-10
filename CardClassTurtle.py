# code by Ms. Harris with pieces from various students work AND
# original Turtle Card Class developed by ICS3U Nov 2018 group collaboration
import random
import turtle

# set up two turtles, use t convention and turtle
t = turtle.Turtle()
t.ht()
t.speed(0)
t.up()
t.goto(30, 0)
turtle.speed(0)
turtle.ht()

class Card:
    #SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    #RANKS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
     #        '8', '9', '10', 'Jack', 'Queen', 'King')

    #def __init__(self, suit, rank):
    def __init__(self, suit=None, rank=None): # account for something going wrong, nothing assigned
        # add in none possibility
            if suit is None:
                suit = random.choice (['Clubs', 'Diamonds', 'Hearts', 'Spades'])
                rank = random.choice (['Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
                                      )
                print( "suit is: ", suit)
                print("rank is: ", rank)
                # need to add calls to these definitions.

                if rank in ['King', 'Queen', 'Jack']:
                    rank = [rank, 10]
                else:
                    rank = [rank, rank]
                # original code resumes
            self.suit = suit
            self.rank = rank

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank[1]

    def writing(self, x, y):
        # proof of concept, replace with correct graphics
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.write(self.rank[0])
        turtle.up()
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.write(self.suit)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)

    def ace(self):
        if 'Ace' in self.rank:
            valace = int(input("Would you like your ace to equal 11 or 1? "))
            if valace ==11:
                self.rank[1] = 11
            elif valace == 1:
                self.rank[1] = 1
            else:
                ace(self)

# spaces to make obvious where my code ended

    def two(self):
    #if self.rank == '2':
        t.penup()
        t.setpos(-200, 250)
        t.pendown()
        t.write("2", font=("Times New Roman", 12, "normal"))
        t.penup()
        t.setpos(200, -250)
        t.pendown()
        t.write("2", font=["Times New Roman", 12, "normal"])  # number left, not upside down

    def three(self):
    #if self.rank == '3':
        t.penup()
        t.setpos(-200, 250)
        t.pendown()
        t.write("3", font=("Times New Roman", 12, "normal"))
        t.penup()
        t.setpos(200, -250)
        t.pendown()
        t.write("3", font=["Times New Roman", 12, "normal"])  # number left, not upside down

    def four(self):
    #if self.rank == '4':
        t.penup()
        t.setpos(-200, 250)
        t.pendown()
        t.write("4", font=("Times New Roman", 12, "normal"))
        t.penup()
        t.setpos(200, -250)
        t.pendown()
        t.write("4", font=["Times New Roman", 12, "normal"])  # number left, not upside down

    def five():
    #if self.rank == '5':
        t.up()
        t.setpos(-250, 250)
        t.down()
        t.write('5', font=("Arial", 20, "normal"))
        t.up()
        t.setpos(250, -250)
        t.left(30)
        t.down()
        t.write('5', font=("Arial", 20, "normal"))

    def six():
    #elif self.rank == '6':
        t.up()
        t.setpos(-250, 250)
        t.down()
        t.write('6', font=("Arial", 20, "normal"))
        t.up()
        t.setpos(250, -250)
        t.left(30)
        t.down()
        t.write('6', font=("Arial", 20, "normal"))


    def seven():
    #elif self.rank == '7':
        t.up()
        t.setpos(-250, 250)
        t.down()
        t.write('7', font=("Arial", 20, "normal"))
        t.up()
        t.setpos(250, -250)
        t.left(30)
        t.down()
        t.write('7', font=("Arial", 20, "normal"))

    def eight():
    #elif self.rank == '8':
        t.up()
        t.setpos(-250, 250)
        t.down()
        t.write('8', font=("Arial", 20, "normal"))
        t.up()
        t.setpos(250, -250)
        t.left(30)
        t.down()
        t.write('8', font=("Arial", 20, "normal"))

#    def draw(self):
        #if self.rank == '9':
    def nine():
          t.setheading(0)
          t.penup()
          t.setpos(-210, 170)
          t.pendown()
          t.write("9", align="center", font=("Arial", 40, "normal"))
          t.penup()
          t.setpos(210, -230)
          t.pendown()
          t.right(180)
          t.write("6", align="center", font=("Arial", 40, "normal"))

 #       if self.rank == '10':
    def ten():
            t.setheading(0)
            t.penup()
            t.setpos(-210, 170)
            t.pendown()
            t.write("I0", align="center", font=("Arial", 40, "normal"))
            t.penup()
            t.setpos(210, -230)
            t.pendown()
            t.right(180)
            t.write("0Ɩ", align="center", font=("Arial", 40, "normal"))

#        if self.rank == 'Jack':
    def Jack():
            t.setheading(0)
            t.penup()
            t.setpos(-210, 170)
            t.pendown()
            t.write("J", align="center", font=("Arial", 40, "normal"))
            t.penup()
            t.setpos(210, -230)
            t.pendown()
            t.write("ſ", align="center", font=("Arial", 40, "normal"))


    def Hearts():
            t.setheading(0)
            t.penup()
            t.setpos(0, -150)
            t.pendown()
            t.color('red')
            t.write("❤", align="center", font=("Arial", 200, "normal"))
            t.penup()
            t.hideturtle()
            # call number here

    def Spades():
        print("put code here for Spades")
        t.penup()
        t.setpos(0, -100)
        t.write("♠", align="center", font=("Arial", 200, "normal"))

        # call number here

    def Clubs():
        print("put code here for Clubs")
        # if self.rank == 'Clubs'
        t.left(90)
        t.forward(100)
        t.dot(150, "black")
        t.right(180)
        t.forward(100)
        t.right(90)
        t.back(50)
        t.dot(150, "black")
        t.forward(100)
        t.dot(150, "black")
        t.back(50)
        t.left(70)
        t.begin_fill()
        t.width(20)
        t.forward(150)
        t.left(110)
        t.forward(100)
        t.left(110)
        t.forward(100)
        t.end_fill()
        # call number here

    def Diamonds():
        print("put code here for Diamonds")
        t.color("red", "red")
        t.speed(3)
        t.penup()
        t.begin_fill()
        t.setpos(-200, 0)
        t.pendown()
        t.setpos(0, 300)
        t.setpos(200, 0)
        t.setpos(0, -300)
        t.setpos(-200, 0)
        t.end_fill()
        t.hideturtle()
        #t.done()
        # call number here

# Program variables
#screen_width = 500
#screen_height = 500

# Sets up screen
screen = turtle.Screen()  # Creates screen object
#screen.setup(screen_width, screen_height)  # Sets screen size
screen.colormode(255)  # Allows RGB values to be used as colours
#screen.bgcolor([255, 255, 255])

# Sets up turtle
t = turtle.Turtle()  # Creates turtle object
t.pensize(2)
t.pencolor([0, 0, 0])
t.speed(0)

#card = Card("Hearts","1243")
#card.draw()


# Ms. Harris code here - proof of concept - a variant of this should be in your program
# that calls this class.
def setup(x, y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    for _ in range(2):
        for _ in range(2):
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)

def drawcard(x, y):
    turtle.up()
    turtle.goto(x-25, y+30)
    turtle.down()
    for _ in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

def PlaycardUpdate(x):# LOGIC ERROR - it's not clearing between cards
    t.clear()   # won't be using this anyway, will be calling appropriate graphics
    t.goto(30,20)   # served purpose to ensure correct cards were being called and OK placement on screen.
    t.write("Player card is: " + str(x))


def play_round():
    Card1 = Card()
    Card1.writing(-75, 100)

    # check to see if card is an Ace
    Card1.ace()
    print("You should have a value printed if you have an ace") # continue as required using graphic


while True:
    playGame = play_round()
    ask = input("Would you like to quit?")
    while ask.lower() not in ['yes', 'no']:
        print ("Sorry try again.")
        ask = input("Would you like to quit? Please answer yes or no ")
    if ask.lower() == 'yes':
        print (" bye ")
        break
    elif ask.lower() == 'no':
        print ("OK")
    t.clear()

screen.exitonclick()  # Keeps screen open until mouse is clicked
