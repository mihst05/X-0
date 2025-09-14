import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x250")
root.config(bg="#54C7A8")
entry1 = tk.Entry(root, width=30)
entry1.place(x=95,y=35)
entry2 = tk.Entry(root, width=30)
entry2.place(x=95,y=65)


label_nume1 = tk.Label(root, text="Player 1:", font=("Arial", 12))
label_nume1.place(x=20,y=30)
label_nume2 = tk.Label(root, text="Player 2:", font=("Arial", 12))
label_nume2.place(x=20,y=60)

k=0
scor_p1=0
scor_p2=0

def fereastra_secundara():
   
    #root.withdraw()
    root.lower()
    second = tk.Toplevel(root)
    second.overrideredirect(True)
    #second.iconbitmap(default='')        
    second.title("X & 0")
   
    tabla = [["" for _ in range(3)] for _ in range(3)]

    tabla_verificare_x=[["" for _ in range(3)] for _ in range(3)]
    tabla_verificare_0=[["" for _ in range(3)] for _ in range(3)]

    second.geometry("1000x500")
    left_frame = tk.Frame(second, bg="lightblue", width=200, height=200)
    left_frame.pack(side="left", fill="both", expand=True)

    
    right_frame = tk.Frame(second, bg="lightgreen", width=200, height=200)
    right_frame.pack(side="right", fill="both", expand=True)
    text_p1=entry1.get()
    text_p2=entry2.get()

    scor_label1=tk.Label(right_frame,text=f"{scor_p1}",font=("Arial", 20, "bold"), fg="yellow",borderwidth=0,    #afiseaza doar text nu si widget-ul
                    highlightthickness=0,bg="lightgreen"  )   
    scor_label1.place(x=290,y=100)

    scor_label2=tk.Label(right_frame,text=f"{scor_p2}",font=("Arial", 20, "bold"), fg="yellow",borderwidth=0,    #afiseaza doar text nu si widget-ul
                    highlightthickness=0,bg="lightgreen"  )   
    scor_label2.place(x=290,y=200)               
    player_label = tk.Label(right_frame, 
                    text=text_p1, 
                bg="lightgreen",
                    height=1,              
                    width=10,              
                    #bd=1,                
                    font=("Arial", 20, "bold"), 
                    fg="yellow",             
                    #padx=10,               
                    #pady=10, 
                    borderwidth=0,    #afiseaza doar text nu si widget-ul
                    highlightthickness=0 ,             
                    #justify=tk.RIGHT,    
                    #relief=tk.RAISED,               
                    #wraplength=250         
                    )
    player_label.place(x=100,y=100)

    player_label2 = tk.Label(right_frame, 
                    text=text_p2, 
                bg="lightgreen",
                    height=1,              
                    width=10,              
                    #bd=1,                
                    font=("Arial", 20, "bold"), 
                    fg="yellow",             
                    #padx=10,               
                    #pady=10, 
                    borderwidth=0,    #afiseaza doar text nu si widget-ul
                    highlightthickness=0 ,             
                    # justify=tk.RIGHT,    
                    # relief=tk.RAISED,               
                    # wraplength=250         
                    )
    player_label2.place(x=100,y=200)


    def afiseaza_litera(i,j):
        global k
        k=k+1
        if k % 2==1:
            tabla[i][j].config(text="X")
            tabla_verificare_x[i][j]="X"

            if(verificare_castigator(tabla_verificare_x)):
               root.lower()
               #messagebox.showinfo("Felicitari!", "X a câștigat jocul!")
               global scor_p1
               scor_p1=scor_p1+1
               scor_label1.config(text=scor_p1)
               
            
        else:
            tabla[i][j].config(text="O")
            tabla_verificare_0[i][j]="X"
        #tabla_verificare[i][j].append(0)

            if(verificare_castigator(tabla_verificare_0)):
                root.lower()
                #messagebox.showinfo("Felicitari!", "O a câștigat jocul!")
                
                global scor_p2
                scor_p2=scor_p2+1
                scor_label2.config(text=scor_p2)
    def verificare_castigator( tabla_verificare_x):
        verif =tabla_verificare_x
        for i in range(3):
                if verif[i][0] == verif[i][1] == verif[i][2] != "":
                    tabla[i][0].config(bg="#1BBF85")
                    tabla[i][1].config(bg="#1BBF85")
                    tabla[i][2].config(bg="#1BBF85")
                    return True
                if verif[0][i] == verif[1][i] == verif[2][i] != "":
                    tabla[0][i].config(bg="#1BBF85")
                    tabla[1][i].config(bg="#1BBF85")
                    tabla[2][i].config(bg="#1BBF85")
                    return True
        if verif[0][0]==verif[1][1]==verif[2][2]!="":
            tabla[0][0].config(bg="#1BBF85")
            tabla[1][1].config(bg="#1BBF85")
            tabla[2][2].config(bg="#1BBF85")
            return True
        if verif[0][2]==verif[1][1]==verif[2][0]!="":
            tabla[0][2].config(bg="#1BBF85")
            tabla[1][1].config(bg="#1BBF85")
            tabla[2][0].config(bg="#1BBF85")
            return True
        for i in range(3):
         for j in range(3):
            if(verif[i][j]!=""):
                return False
                

    def afiseaza_butoane():
        global button
        for i in range(3):
            for j in range(3):
                button = tk.Button(left_frame,bg="#DBB620", text="", font=("Arial", 24), width=5, height=2,command=lambda i=i, j=j,: afiseaza_litera(i,j)) 
                button.place(x=120*(i+1),y=120*(j+1))
                tabla[i][j]=button
                #button.config(bg="red")
 # afisare label-uri nume
    


    #button = tk.Button(second, text="", font=("Arial", 24), width=5, height=2,command=lambda: afiseaza_litera(button))
    #button.pack(pady=20)
    def restart():
         
         for i in range(3):
            for j in range(3):
                button.config(text="")
                #button = tk.Button(left_frame, text="", font=("Arial", 24), width=5, height=2) 
                tabla[i][j].config(text="",bg="#DBB620")
                tabla_verificare_x[i][j]=""
                tabla_verificare_0[i][j]=""
                scor_label1.config(text=scor_p1)
                scor_label2.config(text=scor_p2)
    buton_restart=tk.Button(right_frame, text="Restart", command=restart)
    buton_restart.place(x=200,y=400)

    
    afiseaza_butoane()
    buton_inchidere=tk.Button(right_frame, text="Close", command=root.destroy)
    buton_inchidere.place(x=290,y=400)
    def back_function():
        second.destroy()
        global scor_p1
        global scor_p2
        scor_p1=0
        scor_p2=0
    buton_back=tk.Button(right_frame, text="Back", command=back_function)
    buton_back.place(x=110,y=400)
    
    second.mainloop()
    

    
def function_for_play():
    fereastra_secundara()
      
btn = tk.Button(root, text="Play", command=function_for_play,bg="#DBB620")
btn.pack(pady=5)
btn.place(x=190,y=175)

root.mainloop()
