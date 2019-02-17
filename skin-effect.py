import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
 
 
from tkinter import *
import tkinter as tk
from tkinter import ttk
 
LARGE_FONT=("Verdana", 12)
MIDDLE_FONT=("Verdana", 10)
FONT = ("Verdana", 8)
FONT_MENU=("Comic Sans MS", 15)
style.use("ggplot")
 
f=Figure(figsize=(5,5), dpi=100)
f1=Figure(figsize=(5,5), dpi=100)
f2=Figure(figsize=(5,5), dpi=100)
graph1 = f.add_subplot(111)
graph2 = f1.add_subplot(111)
graph3 = f2.add_subplot(111)
 
 
def animate(a=0,b=0,c=0,d=0,e=False):
    global clear
    t = numpy.arange(c, d, 10)
    s = (503*numpy.sqrt(a/(b*t*1000)))*1000
    if e==True:
        graph1.clear()
        clear=False
    graph1.plot(t,s)
    graph1.set_title('Skin Effect vs Frequência')
    graph1.set_xlabel('f(kHz)')
    graph1.set_ylabel('δ(mm)')
    graph1.set_yscale('log')
    graph1.set_xscale('log')
   
   
 
def animated(j=0,k=0,l=0,m=False):
    global clear
    sd = numpy.arange((l/2)/1000, (l/2)/1e-4, 1e-1)
    s1 = ((j*k)/(numpy.pi*l*((l/2)/sd)))/(j*k/(numpy.pi*(l/2)*(l/2)))
   
    if (m==True):
        graph2.clear()
        clear=False
    graph2.plot(sd,s1)
    graph2.set_title('Resistência AC/Resistência DC vs Raio do fio/δ(skin depth)')
    graph2.set_ylabel('Rac/Rdc')
    graph2.set_xlabel('R/δ')
   
def animates(j=0,k=0,l=0,m=False):
    global clear
    sd = numpy.arange(1e-6, 1e-2, 1e-8)
    s1 = (j*k)/(numpy.pi*l*sd)
    if (m==True):
        graph3.clear()
        clear=False
    graph3.plot(s1,sd)
    graph3.set_title('Resistência AC vs δ(skin depth)')
    graph3.set_yscale('log')
    graph3.set_xlabel('Rac(Ω)')
    graph3.set_ylabel('δ(m)')
       
class SeaofBTCapp (tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
       
        #tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Software (Data analysis)")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
       
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
       
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(pady=30,row=0, column = 0, sticky="nsew")
        self.show_frame(StartPage)
   
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
 
def qf():
    print("Hamne kar dikhaya")
 
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Skin Effect", font=FONT_MENU)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text="Avaliação de Condutores com base no Skin Effect", font=FONT_MENU)
        label.pack(pady=10, padx=10)
       
        button = ttk.Button(self, text="Skin depth (δ)", command=lambda :controller.show_frame(PageOne))
        button.pack(pady=20)
        buttona = ttk.Button(self, text="Inserção de dados", command=lambda :controller.show_frame(PageTwo))
        buttona.pack(pady=20)
        buttonb = ttk.Button(self, text="Gráfico (skin depth vs frequência)", command=lambda :controller.show_frame(PageThree))
        buttonb.pack(pady=20)
        buttond = ttk.Button(self, text="Gráfico (Resistência AC vs δ(skin depth))", command=lambda :controller.show_frame(PageFive))
        buttond.pack(pady=20)
        buttonc = ttk.Button(self, text="Gráfico (Resistência AC/Resistência DC vs Raio do fio/δ)", command=lambda :controller.show_frame(PageFour))
        buttonc.pack(pady=20)
       
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Insira o valor dos parâmetros abaixo (SI):", font=MIDDLE_FONT)
        label.grid(row=1,column=1,columnspan=2,sticky=W,pady=3)
        label = tk.Label(self, text="Resistividade (ρ): ", font=FONT)
        label.grid(row=2,column=1,sticky=W,pady=5)
        self.nome1=Entry(self,width=10, font=FONT)
        self.nome1.grid(row=2,column=2,sticky=W)
        label = tk.Label(self, text="Frequência angular da corrente (ω): ", font=FONT)
        label.grid(row=3,column=1,sticky=W,pady=5)
        self.nome2=Entry(self,width=10, font=FONT)
        self.nome2.grid(row=3,column=2,sticky=W)
        label = tk.Label(self, text="Permeabilidade magnética (μ): ", font=FONT)
        label.grid(row=4,column=1,sticky=W,pady=5)
        self.nome3=Entry(self,width=10, font=FONT)
        self.nome3.grid(row=4,column=2,sticky=W)
        label = tk.Label(self, text="Permissividade elétrica (ε): ", font=FONT)
        label.grid(row=5,column=1,sticky=W,pady=5)
        self.nome4=Entry(self,width=10, font=FONT)  
        self.nome4.grid(row=5,column=2,sticky=W)
        button1_1 = ttk.Button(self, text="Calcular", command=self.calculo)
        button1_1.grid(row=6,column=1,sticky=W)
        self.canvas=Canvas(self, height=400, width=500, takefocus=1, bg='deepskyblue', highlightthickness=0)
        self.canvas.focus_force()
        self.canvas.grid(row=7,column=1,columnspan=2,sticky=W)
     
        button1 = ttk.Button(self, text="Voltar", command=lambda :controller.show_frame(StartPage))
        button1.grid(row=6, column=1, padx = 30)
       
       
    def calculo(self):
        NOME1=self.nome1.get()
        NOME2=self.nome2.get()
        NOME3=self.nome3.get()
        NOME4=self.nome4.get()
        h1=float(NOME1)
        h2=float(NOME2)
        h3=float(NOME3)
        h4=float(NOME4)
        h=math.sqrt((2*h1)/(h2*h3))*math.sqrt(math.sqrt(1+(h1*h2*h4)**2)+(h1*h2*h4))
        h1=str(round(h,4))
        label = tk.Label(self, text=h1, font=FONT)
        label.grid(row=6,column=2,sticky=W)
        self.canvas.create_oval(140,50,340,250,fill='red')
        if 7381*h >= 100:
            h=100/7381
       
        self.canvas.create_oval(140+7381*h,50+7381*h,340-7381*h,250-7381*h,fill='black')
       
global DADO1
global DADO2
global DADO3
global DADO4
global DADO5
global DADO6
global clear
clear = False
DADO1 = 0
DADO2 = 0
DADO3 = 0
DADO4 = 0
DADO5 = 0
DADO6 = 0
       
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Insira o valor dos parâmetros abaixo (temperatura ambiente e conforme o SI):", font=MIDDLE_FONT)
        label.grid(row=1,column=1,columnspan=2,sticky=W,pady=3)
        label = tk.Label(self, text="Resistividade (ρ): ", font=FONT)
        label.grid(row=2,column=1,sticky=W,pady=5)
        self.nome1=Entry(self,width=10, font=FONT)
        self.nome1.grid(row=2,column=2,sticky=W)
        label = tk.Label(self, text="Permeabilidade magnética relativa (μr): ", font=FONT)
        label.grid(row=4,column=1,sticky=W,pady=5)
        self.nome2=Entry(self,width=10, font=FONT)
        self.nome2.grid(row=4,column=2,sticky=W)
        label = tk.Label(self, text="Comprimento do fio: ", font=FONT)
        label.grid(row=6,column=1,sticky=W,pady=5)
        self.nome5=Entry(self,width=10, font=FONT)
        self.nome5.grid(row=6,column=2,sticky=W)
        label = tk.Label(self, text="Diâmetro do fio: ", font=FONT)
        label.grid(row=8,column=1,sticky=W,pady=5)
        self.nome6=Entry(self,width=10, font=FONT)
        self.nome6.grid(row=8,column=2,sticky=W)
        label = tk.Label(self, text="Frequência inicial (kHz): ", font=FONT)
        label.grid(row=10,column=1,sticky=W,pady=5)
        self.nome3=Entry(self,width=10, font=FONT)
        self.nome3.grid(row=10,column=2,sticky=W)
        label = tk.Label(self, text="Frequência final (kHz): ", font=FONT)
        label.grid(row=12,column=1,sticky=W,pady=5)
        self.nome4=Entry(self,width=10, font=FONT)
        self.nome4.grid(row=12,column=2,sticky=W)
        button1_2 = ttk.Button(self, text="Cobre", command=self.cobre)
        button1_2.grid(row=13,column=1,sticky=W)
        button1_2 = ttk.Button(self, text="Alumínio", command=self.aluminio)
        button1_2.grid(row=14,column=1,sticky=W)
        button1_2 = ttk.Button(self, text="Fe-Si", command=self.feSi)
        button1_2.grid(row=15,column=1,sticky=W)
        button1_2 = ttk.Button(self, text="Fe-Ni", command=self.feNi)
        button1_2.grid(row=16,column=1,sticky=W)
        button1_3 = ttk.Button(self, text="Clear", command=self.clear)
        button1_3.grid(row=17,column=1,sticky=W)
        button1_1 = ttk.Button(self, text="Coletar dados", command=self.coletar)
        button1_1.grid(row=18,column=1,sticky=W)
        button1 = ttk.Button(self, text="Voltar", command=lambda :controller.show_frame(StartPage))
        button1.grid(row=18, column=2)
    def clear(self):
        global clear
        clear = True
    def cobre(self):
        global DADO1
        global DADO2
        global DADO3
        global DADO4
        global DADO5
        global DADO6
        DADO1 = 1.68e-8
        DADO2 = 1.0
        DADO3=self.nome3.get()
        DADO4=self.nome4.get()
        DADO5=self.nome5.get()
        DADO6=self.nome6.get()
    def aluminio(self):
        global DADO1
        global DADO2
        global DADO3
        global DADO4
        global DADO5
        global DADO6
        DADO1 = 2.98e-8
        DADO2 = 1.0
        DADO3=self.nome3.get()
        DADO4=self.nome4.get()
        DADO5=self.nome5.get()
        DADO6=self.nome6.get()
    def feSi(self):
        global DADO1
        global DADO2
        global DADO3
        global DADO4
        global DADO5
        global DADO6        
        DADO1 = 47.2e-8
        DADO2 = 2325
        DADO3=self.nome3.get()
        DADO4=self.nome4.get()
        DADO5=self.nome5.get()
        DADO6=self.nome6.get()        
    def feNi(self):
        global DADO1
        global DADO2
        global DADO3
        global DADO4
        global DADO5
        global DADO6
        DADO1 = 0.55e-6
        DADO2 = 8000
        DADO3=self.nome3.get()
        DADO4=self.nome4.get()
        DADO5=self.nome5.get()
        DADO6=self.nome6.get()
    def coletar(self):
        global DADO1
        global DADO2
        global DADO3
        global DADO4
        global DADO5
        global DADO6        
        DADO1=self.nome1.get()
        DADO2=self.nome2.get()
        DADO3=self.nome3.get()
        DADO4=self.nome4.get()
        DADO5=self.nome5.get()
        DADO6=self.nome6.get()
       
global z
global z1
global z2
z = 0
z1 = 0
z2 = 0
i = 1    
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Gráfico referente ao skin depth", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button11 = ttk.Button(self, text="Fazer gráfico", command=self.grafico)
        button11.pack()
        button1 = ttk.Button(self, text="Voltar", command=lambda :controller.show_frame(StartPage))
        button1.pack()
   
    def grafico(self):
        global z
        animate(float(DADO1),float(DADO2),float(DADO3),float(DADO4),clear)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.show()
        if z==0:
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            toolbar = NavigationToolbar2TkAgg(canvas, self)
            toolbar.update()
            z=1
        if z==0:
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            z=1
class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Gráfico para análise da resistência AC", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button11 = ttk.Button(self, text="Fazer gráfico", command=self.grafico3)
        button11.pack()
        button1 = ttk.Button(self, text="Voltar", command=lambda :controller.show_frame(StartPage))
        button1.pack()
       
    def grafico3(self):
        global z1
        animated(float(DADO1),float(DADO5),float(DADO6),clear)
        canvas = FigureCanvasTkAgg(f1,self)
        canvas.show()
        if z1==0:
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            toolbar = NavigationToolbar2TkAgg(canvas, self)
            toolbar.update()
            z1=1
        if z1==0:
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            z1=1
 
class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Gráfico para análise da resistência AC", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button11 = ttk.Button(self, text="Fazer gráfico", command=self.grafico2)
        button11.pack()
        button1 = ttk.Button(self, text="Voltar", command=lambda :controller.show_frame(StartPage))
        button1.pack()
       
    def grafico2(self):
        global z2
        animates(float(DADO1),float(DADO5),float(DADO6),clear)
        canvas = FigureCanvasTkAgg(f2,self)
        canvas.show()
        if z2==0:
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            toolbar = NavigationToolbar2TkAgg(canvas, self)
            toolbar.update()
            z2=1
        if z2==0:
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            z2=1
   
       
 
app= SeaofBTCapp()
#ani = animation.FuncAnimation(f,animate, interval=1000)
#animate(i)
app.mainloop()
