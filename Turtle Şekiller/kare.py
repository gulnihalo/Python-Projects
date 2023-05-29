import turtle

turtle.shape("circle")
turtle.shapesize(3)

for kenar in range(4):
    turtle.dot()
    turtle.write("Köşe: "+str(kenar))
    turtle.forward(100)
    turtle.right(90)

turtle.shapesize(1)    

turtle.mainloop()