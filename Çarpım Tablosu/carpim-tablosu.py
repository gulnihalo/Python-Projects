import turtle

##çarpım tablosu işlemi

benimfont="Comic Sans MS","24"
turtle.penup()
turtle.goto(-100,300)
turtle.pendown()
turtle.write("Çarpım Tablosu",font=benimfont)
for d in range(1,11):
    for i in range(1,11):
        turtle.penup() #kalemi kaldır
        turtle.goto(-300+d*50,-100+i*30)
        turtle.pendown()
        turtle.write(str(d)+"x"+str(i)+"="+str(d*i))
        
turtle.mainloop()