import turtle

turtle.pensize(2)
turtle.delay(-100)
turtle.color("orange")
for cember in range(24):
    turtle.left(15)
    turtle.circle(100)
for cember in range(200):
    turtle.left(500)
    turtle.forward(cember)      
    
turtle.mainloop()    