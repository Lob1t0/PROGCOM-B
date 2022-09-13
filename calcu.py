from tkinter import*
from math import*


ventana=Tk()
ventana.title("Caculadora Cientifica")
ventana.geometry("840x500")
ventana.configure(background="black")
color_boton=("silver")



def btnClik(num):
    global operador
    operador=operador+str(num)
    display.set(operador) 
def clear():
    global operador
    operador=("")
    display.set(operador)

def operacion():
    global operador
    try:
        opera=str(eval(operador))
    except:
        clear()
        opera=("ERROR")
    display.set(opera)

ancho_boton=5
alto_boton=2

display=StringVar()

pantalla_p=Entry(ventana, textvariable=display,fg="black",bg="silver",font=("arial",20,"bold"),width=22,bd=20,justify="right").place(x=37,y=50)
operador=""


def centigrados_farenheit():
                numero=int(grado.get())
                respuesta=((numero+40)*(9/5))-40
                Resultado_grados.set(respuesta)
def farenheit_centigrados():
                numero=int(grado.get())
                respuesta=((numero+40)*(5/9))-40
                Resultado_grados.set(respuesta)
def centigrados_kelvin():
                numero=int(grado.get())
                respuesta=273+numero
                Resultado_grados.set(respuesta)
def kelvin_centigrados():
                numero=int(grado.get())
                respuesta=numero-273
                Resultado_grados.set(respuesta)
def farentheit_kelvin():
                numero=int(grado.get())
                respuesta=((numero-32)*(5/9))+273
                Resultado_grados.set(respuesta)
def kelvin_farenheit():
                numero=numero=int(grado.get())
                respuesta=((numero-273)*(9/5))+32
                Resultado_grados.set(respuesta)


cen__faren=Button(ventana,text="° C--> °F",bg=color_boton,command=centigrados_farenheit,width=20).place(x=550,y=180)
faren__cen=Button(ventana,text="°F ---> °C",bg=color_boton,command=farenheit_centigrados,width=20).place(x=550,y=230)
cen__kel=Button(ventana,text="°C ---> °K",bg=color_boton,command=centigrados_kelvin,width=20).place(x=550,y=280)
kel__cen=Button(ventana,text="°K ---> °C",bg=color_boton,command=kelvin_centigrados,width=20).place(x=550,y=330)
faren__kel=Button(ventana,text="°F ---> °K",bg=color_boton,command=farentheit_kelvin,width=20).place(x=550,y=380)
kel__faren=Button(ventana,text="°K ---> °F",bg=color_boton,command=kelvin_farenheit,width=20).place(x=550,y=430)


grado=StringVar()
pantalla1=Entry(ventana,bg="silver",font=("arial",20,"bold"),width=10,bd=20,justify="right",textvariable=grado).place(x=420,y=50)



Resultado_grados=StringVar()
pantalla_resultado=Entry(ventana,fg="black",bg="silver",font=("arial",20,"bold"),width=11,bd=20,justify="right",textvariable=Resultado_grados).place(x=620,y=50)


B0=Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
B1=Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=63,y=180)
B2=Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=109,y=180)
B3=Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=155,y=180)
B4=Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=230)
B5=Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=63,y=230)
B6=Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=109,y=230)
B7=Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=155,y=230)
B8=Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=17,y=280)
B9=Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=63,y=280)


BC=Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=109,y=280)
BComa=Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=155,y=280)
BotonSuma=Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=17,y=330)
BResta=Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=63,y=330)
BMulti=Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=109,y=330)
BDiv=Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=155,y=330)
BSqrt=Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt")).place(x=17,y=380)
BParen1=Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=63,y=380)
BParen2=Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=109,y=380)
BResto=Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=155,y=380)
Bln=Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log")).place(x=17,y=430)
BC=Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=63,y=430)
BExp=Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=109,y=430)
BResul=Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=operacion).place(x=155,y=430)
bsen=Button(ventana,text="n!",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("factorial")).place(x=220,y=180)
bcos=Button(ventana,text="ABS",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("fabs")).place(x=266,y=180)


bsen=Button(ventana,text="sin",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sin")).place(x=312,y=180)
bcos=Button(ventana,text="cos",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("cos")).place(x=358,y=180)
btan=Button(ventana,text="tan",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("tan")).place(x=220,y=230)
barccot=Button(ventana,text="arccot",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("atan")).place(x=266,y=230)
barcsen=Button(ventana,text="arccos",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("acos")).place(x=312,y=230)
barcc=Button(ventana,text="arcsen",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("asin")).place(x=358,y=230)
bsenh=Button(ventana,text="senh",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sinh")).place(x=220,y=280)
bcosh=Button(ventana,text="cosh",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("cosh")).place(x=266,y=280)
btanh=Button(ventana,text="tanh",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("tanh")).place(x=312,y=280)
b_Salir=Button(ventana,text="EXIT",bg="yellow",fg="blue",command=exit,font=("Arial Black",5),width=20,relief=RIDGE).place(x=310,y=440)

 
etiqueta=Label(ventana,text="DISPLAY",fg="black",font=("Arial Black",10)).place(x=200,y=29)
etiqueta2=Label(ventana,text="Ingrese datos por teclado",fg="black",font=("Arial Black",10)).place(x=420,y=25)
etiqueta3=Label(ventana,text="Resultado",fg="black",font=("Arial Black",10)).place(x=670,y=25)
etiqueta4=Label(ventana,text="OPERACIONES ARITMETICAS Y GEOMETRICAS",fg="black",font=("Arial Black",10)).place(x=43,y=150)
etiqueta5=Label(ventana,text="CONVERSION DE TEMPERATURA",fg="black",font=("Arial Black",10)).place(x=500,y=150)



ventana.mainloop()
