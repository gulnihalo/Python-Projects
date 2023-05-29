import turtle

turtle.delay(-50)
benimfont="Times", "50", "bold italic"
turtle.penup()
turtle.goto(-200,300)
turtle.pendown()
turtle.write("Türk Bayrağı",font=benimfont)

turtle.screensize(bg="red", canvheight=420, canvwidth=720)


turtle.up()   
turtle.goto(-100,-100)
turtle.color("white") 
turtle.begin_fill()
turtle.circle(120)
turtle.end_fill()

turtle.goto(-70,-80)
turtle.color("red")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
  



turtle.goto(0,35)
turtle.fillcolor("white")
turtle.begin_fill()
for yildiz in range(5):   
    turtle.forward(150)
    turtle.right(144)   
turtle.end_fill()
turtle.goto(-130,-190)    
turtle.color("white")
turtle.goto(-999,0)

turtle.done()  
