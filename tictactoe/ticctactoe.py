#importing the message boxes 
import tkinter.messagebox
#***********************
#--------------------------------------------#
#importing everything from the tkinter toolkit
from tkinter import*
from PIL import Image,ImageTk
#********************
#----------------------------------------------#
#making of the event loop  
root = Tk()
root.geometry("1350x750")
root.title("Tic Tac Toe")
root.configure(bg="sky blue")
root.wm_iconbitmap("2.ico")
#******************************
#-----------------------------------------------#
# printing the value on the buttons using booleans 
b = IntVar()
bclick = True
def checker(b):
    global bclick
    if b["text"] == " " and bclick == True:
        b["text"] = "X"
        bclick = False
        score()
    elif b['text'] == ' ' and bclick == False:
        b["text"] = "0"
        bclick = True
        score()
#**********************************************
#----------------------------------------------------------------------------------------------------------------------#        
# conditions for the winning of player_X in all 3 rows , 3 cloumns as well as the 2 diagnals and then updating the score
def score():
    if (b3["text"]=="X") and (b4["text"]=="X") and (b5["text"]=="X"):
        b3.configure(bg="blue")
        b4.configure(bg="blue")
        b5.configure(bg="blue")
        n = float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_X is the winner !!")

    elif (b6["text"]=="X") and (b7["text"]=="X") and (b8["text"]=="X"):
        b6.configure(bg="blue")
        b7.configure(bg="blue")
        b8.configure(bg="blue")
        n = float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_X is the winner !!")  
        
    elif (b9["text"]=="X") and (b10["text"]=="X") and (b11["text"]=="X"):
        b9.configure(bg="blue")
        b10.configure(bg="blue")
        b11.configure(bg="blue")
        n = float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_X is the winner !!")     
   
    elif (b3["text"]=="X") and (b6["text"]=="X") and (b9["text"]=="X"):
        b3.configure(bg="blue")
        b6.configure(bg="blue")
        b9.configure(bg="blue")
        n = float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_X is the winner !!")
           
    elif (b4["text"]=="X") and (b7["text"]=="X") and (b10["text"]=="X"):
        b4.configure(bg="blue")
        b7.configure(bg="blue")
        b10.configure(bg="blue")
        n = float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_X is the winner !!")
   
    elif (b5["text"]=="X") and (b8["text"]=="X") and (b11["text"]=="X"):
        b5.configure(bg="blue")
        b8.configure(bg="blue")
        b11.configure(bg="blue")
        n = float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_X is the winner !!")

    elif (b3["text"]=="X") and (b7["text"]=="X") and (b11["text"]=="X"):
        b3.configure(bg="blue")
        b7.configure(bg="blue")
        b11.configure(bg="blue")
        n = float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_X is the winner !!")
   
    elif (b5["text"]=="X") and (b7["text"]=="X") and (b9["text"]=="X"):
        b5.configure(bg="blue")
        b7.configure(bg="blue")
        b9.configure(bg="blue")
        n = float(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_X is the winner !!")
#******************************************************************************************        
#---------------------------------------------------------------------------------------------------------------------#
# conditions for the winning of player_0 in all 3 rows , 3 cloumns as well as the 2 diagnals and then updating the score
    elif (b3["text"]=="0") and (b4["text"]=="0") and (b5["text"]=="0"):
        b3.configure(bg="sky blue")
        b4.configure(bg="sky blue")
        b5.configure(bg="sky blue")
        n = float(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_0 is the winner !!")

    elif (b6["text"]=="0") and (b7["text"]=="0") and (b8["text"]=="0"):
        b6.configure(bg="sky blue")
        b7.configure(bg="sky blue")
        b8.configure(bg="sky blue")
        n = float(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_0 is the winner !!")  
        
    elif (b9["text"]=="0") and (b10["text"]=="0") and (b11["text"]=="0"):
        b9.configure(bg="sky blue")
        b10.configure(bg="sky blue")
        b11.configure(bg="sky blue")
        n = float(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_0 is the winner !!")     
   
    elif (b3["text"]=="0") and (b6["text"]=="0") and (b9["text"]=="0"):
        b3.configure(bg="sky blue")
        b6.configure(bg="sky blue")
        b9.configure(bg="sky blue")
        n = float(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_0 is the winner !!")
           
    elif (b4["text"]=="0") and (b7["text"]=="0") and (b10["text"]=="0"):
        b4.configure(bg="sky blue")
        b7.configure(bg="sky blue")
        b10.configure(bg="sky blue")
        n = float(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_0 is the winner !!")
   
    elif (b5["text"]=="0") and (b8["text"]=="0") and (b11["text"]=="0"):
        b5.configure(bg="sky blue")
        b8.configure(bg="sky blue")
        b11.configure(bg="sky blue")
        n = float(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_0 is the winner !!")

    elif (b3["text"]=="0") and (b7["text"]=="0") and (b11["text"]=="0"):
        b3.configure(bg="sky blue")
        b7.configure(bg="sky blue")
        b11.configure(bg="sky blue")
        n = float(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_0 is the winner !!")
   
    elif (b5["text"]=="0") and (b7["text"]=="0") and (b9["text"]=="0"):
        b5.configure(bg="sky blue")
        b7.configure(bg="sky blue")
        b9.configure(bg="sky blue")
        n = float(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner","PLAYER_0 is the winner !!")        
#**************************************************************************
#---------------------------------------------------------------------------------------------------------------------------------#
#Making of the frames       
top = Frame(root,bg="cadet blue",pady=2,borderwidth=10,width=1350,height=100,relief=RIDGE)
top.grid(row=0,column=0) 
lbtitle = Label(top,font="arial 35 bold",text="TIC TAC TOE",bg="powder blue",padx=513,fg="gold",justify=CENTER).grid(row=0,column=0)
main = Frame(root,bg="cadet blue",borderwidth=10,relief=RIDGE)
main.place(x=12,y=90)
leftframe = Frame(main,bg="cadet blue",width=700,height=620).pack(side=LEFT)
rightframe = Frame(main,bg="cadet blue",padx=5,width=600,height=200).pack(side=RIGHT)
rightframe1 = Frame(rightframe,bg="powder blue",width=550,height=300,borderwidth=8,relief=RIDGE)
rightframe1.place(x=752,y=110)
rightframe2 = Frame(rightframe,bg="powder blue",width=550,height=300,borderwidth=8,relief=RIDGE)
rightframe2.place(x=752,y=410)
#importing jpg images
image1 = Image.open("images\\tic.jpg")
image1 = image1.resize((200,200),Image.BOX)
pic1 = ImageTk.PhotoImage(image1)
label1 = Label(leftframe,borderwidth=6,relief=RIDGE,image=pic1).place(x=533,y=310)

image2 = Image.open("images\\tic2.jpg")
image2 = image2.resize((410,80),Image.BOX)
pic2 = ImageTk.PhotoImage(image2)
label2 = Label(leftframe,borderwidth=6,relief=RIDGE,image=pic2).place(x=97,y=105)
#*************************************************************************************************************************************
#---------------------------------------#
# entry widget datatype and initial value
PlayerX = IntVar()
Player0 = IntVar()
PlayerX.set(0)
Player0.set(0)
#****************
#--------------------------------------------------------------------------------------------------#
# defining of the reset button by making the text blank and restoring the original color on the board
def reset():
    b3['text']=" "
    b4['text']=" "
    b5['text']=" "
    b6['text']=" "
    b7['text']=" "
    b8['text']=" "
    b9['text']= " "
    b10['text']= " "
    b11['text']= " "
    b3.configure(bg="grey")
    b4.configure(bg="grey")
    b5.configure(bg="grey")
    b6.configure(bg="grey")
    b7.configure(bg="grey")
    b8.configure(bg="grey")
    b9.configure(bg="grey")
    b10.configure(bg="grey")
    b11.configure(bg="grey")
#******************************
#-----------------------------------------------------------#
#defining new game as reset all value (score as well as board)
def newgm():
    reset()    
    Player0.set(0)
    PlayerX.set(0)
#*************************************************************
#-------------------------------------------------------------------------------------------------------------------#
#making of label and entry widget in the right upper frame
lbplx = Label(rightframe,font="arial 30 bold",text="Player_X :",bg="grey",fg="gold",borderwidth=7,relief=RIDGE)
lbplx.place(x=770,y=180)
e1 = Entry(rightframe,borderwidth=7,relief=RIDGE,width=13,textvariable=PlayerX,font="arial 30 bold").place(x=985,y=180)
lbpl0 = Label(rightframe,padx=4,font="arial 30 bold",text="Player_0 :",borderwidth=7,relief=RIDGE,bg="grey",fg="gold")
lbpl0.place(x=770,y=260)
e1 = Entry(rightframe,width=13,textvariable=Player0,font="arial 30 bold",borderwidth=7,relief=RIDGE).place(x=985,y=260)
#*********************************************************************************************************************
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#all the buttons in the frame
b1=Button(rightframe,bg="purple",text="RESET",foreground="spring green",font="lucida 35 bold italic",padx=155,borderwidth=7,command=reset,relief=RIDGE).place(x=770,y=450)
b2=Button(rightframe,bg="purple",text="NEW GAME",foreground="spring green",font="lucida 35 bold italic",command=newgm,borderwidth=7,relief=RIDGE).place(x=770,y=555)
b3=Button(root,text=" ",font="lucida 50 bold",width=3,borderwidth=6,bg="grey",command=lambda:checker(b3))
b3.place(x=100,y=200)
b4=Button(leftframe,text=" ",font="lucida 50 bold",width=3,borderwidth=6,bg="grey",command=lambda:checker(b4))
b4.place(x=240,y=200)
b5=Button(leftframe,text=" ",font="lucida 50 bold",width=3,borderwidth=6,bg="grey",command=lambda:checker(b5))
b5.place(x=380,y=200)
b6=Button(leftframe,text=" ",font="lucida 50 bold",bg="grey",width=3,borderwidth=6,command=lambda:checker(b6))
b6.place(x=100,y=341)
b7=Button(leftframe,text=" ",font="lucida 50 bold",bg="grey",width=3,borderwidth=6,command=lambda:checker(b7))
b7.place(x=240,y=341)
b8=Button(leftframe,text=" ",font="lucida 50 bold",bg="grey",width=3,borderwidth=6,command=lambda:checker(b8))
b8.place(x=380,y=341)
b9=Button(leftframe,text=" ",font="lucida 50 bold",bg="grey",width=3,borderwidth=6,command=lambda:checker(b9))
b9.place(x=100,y=482)
b10=Button(leftframe,text=" ",font="lucida 50 bold",bg="grey",width=3,borderwidth=6,command=lambda:checker(b10))
b10.place(x=240,y=482)
b11=Button(leftframe,text=" ",font="lucida 50 bold",bg="grey",width=3,borderwidth=6,command=lambda:checker(b11))
b11.place(x=380,y=482)
def click():
    a = tkinter.messagebox.askquestion("Exit","Do you really want to exit",icon="warning")
    if a == "yes":
        root.destroy()
    else:
        tkinter.messagebox.showinfo("Return","You are returned to the window")
        return(root) 
   
b12=Button(rightframe,bg="purple",text="Exit",foreground="spring green",font="lucida 35 bold italic",command=click,padx=35,borderwidth=7,relief=RIDGE).place(x=1082,y=555)
#******************************************************************************************************************************************************************************
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Closing of the event loop
root.mainloop()
#*************************