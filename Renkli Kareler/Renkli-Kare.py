import turtle as trt

renkler=["red","green","blue","yellow"]
trt.pensize(2)
trt.bgcolor("dodgerblue")
for cizgi in range(1,300,3):
    renk=cizgi%4
    trt.pencolor(renkler[renk])
    trt.backward(cizgi)
    trt.left(92)   
    
trt.mainloop()    
    
