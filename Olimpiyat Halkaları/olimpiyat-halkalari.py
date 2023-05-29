import turtle

def halka(x,y,renk):
    turtle.penup()
    turtle.pensize(5)
    turtle.pencolor(renk)    
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(100)
    
    

def main():
    halka(-200, 50, "blue")
    halka(10, 50, "black")
    halka(220, 50, "red")
    halka(-105, -70, "yellow")
    halka(110, -70, "green")
    
    turtle.mainloop()
    
main()    
    
    