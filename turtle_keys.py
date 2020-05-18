import turtle

def turtle_table():
    array = ["Encryption : 1","Decryption : 2"]
    array2 = ["Ceasar cypher : 1","Baconian cypher : 2","Atbash cypher : 3","ROT 47 cypher : 4","Text FIle : 5","Image file : 6"]
    p = turtle.Turtle()#creates tutle
    s = turtle.Screen()#to control screen
    s.title("Error Check")
    s.setworldcoordinates(-2,-2,9,9)#sets the size of the Screen
    s.bgcolor("black")
    p.color("yellow")
    p.hideturtle()#hides the turtle
    p.speed(10)#sets turtle speed
    #writes heading on turtle_table
    p.up()
    p.goto(0,8)
    p.write("The Table Shows the Keys to the Encyption and Decryption Methods",font = ("Times New Roman",16))
    #writes error text below Table and array syntax
    p.goto(-1,-1)
    p.write("Look through table to ensure you type in the right key",font = ("Times New Roman",16))
    p.goto(-2,7)
    p.write("array = [Encryption or decryption key,Encryption or decryption type,Text file or image for encryption or decryption,Key used for encryption(when needed.)]",font = ("Times New Roman",12))
    p.goto(0,0)
    p.down()
    #draw table
    for i in range(4):
        p.forward(7)
        p.left(90)
    p.up()
    y = 6
    for i in range(6):
        p.goto(0,y)
        p.down()
        p.goto(7,y)
        p.up()
        y = y - 1
    p.goto(3.5,0)
    p.down()
    p.goto(3.5,7)
    p.up()
    p.goto(0,6)
    #Writes keys to various encryption and dercyption methods
    p.write(array[0],font = ("Times New Roman",16,"bold"))
    p.goto(3.5,6)
    p.write(array[1],font = ("Times New Roman",16,"bold"))
    y = 5
    for i in array2:
        p.goto(0,y)
        p.write(i,font = ("Helvitica",14))
        p.goto(3.5,y)
        p.write(i,font = ("Helvitica",14))
        y = y - 1
    #prevents the turtle window from closing unless user clicks
    s.exitonclick()
    return "complete"
