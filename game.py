import customtkinter as ctk
from random import sample
from PIL import Image, ImageTk

ctk.set_appearance_mode('light')
score = {'Win':0,'Loss':0,'Tie':0,'Round':0}


def on_click(pchoice):
    pstatus.configure(text=f"Your choice: {pchoice.title()}")
    oppchoice=c_choice()
    Result=game(pchoice,oppchoice,score)
    status.configure(text="Tie" if Result=="Tie" else f"You {Result}")
    pscore.configure(text=f"Your Score: {score['Win']}")
    cscore.configure(text=f"Computer's Score: {score['Loss']}")
    round.configure(text=f"Round: {score['Round']}")

def c_choice():
    imgs = {'rock':rockimg,'paper':paperimg,'scissors':scissorsimg}
    choices=('rock','paper','scissors')
    choice = sample(choices,1)
    clabel.configure(text='',image=imgs[choice[0]])
    cstatus.configure(text=f"Opponent selected: {choice[0].title()}")
    return choice[0]

def game(ch,opp,score):
    score['Round']+=1
    if ch==opp:
        score['Tie']+=1
        res="Tie"
    elif ch=='rock':
        if opp=='scissors':
            score['Win']+=1
            res="Won"
        else:
            score['Loss']+=1
            res='Lost'
    elif ch=='paper':
        if opp=='rock':
            score['Win']+=1
            res="Won"
        else:
            score['Loss']+=1
            res='Lost'
    elif ch=='scissors':
        if opp=='paper':
            score['Win']+=1
            res="Won"
        else:
            score['Loss']+=1
            res='Lost'
    return res

root =ctk.CTk()
root.title("Rock Paper Scissors GUI")
root.geometry('900x480')
root.resizable(0,0)

rock = Image.open('icons/rock.png')
r_rock = rock.resize((80,80))
paper = Image.open('icons/paper.png')
r_paper = paper.resize((80,80))
scissors = Image.open('icons/scissors.png')
r_scissors = scissors.resize((80,80))

rockimg = ImageTk.PhotoImage(r_rock)
paperimg = ImageTk.PhotoImage(r_paper)
scissorsimg = ImageTk.PhotoImage(r_scissors)

frame = ctk.CTkFrame(root,fg_color='#0d7dd6')
frame.pack(fill='both',expand=1)
title = ctk.CTkLabel(frame,text='Rock Paper Scissors!',fg_color='#0d7dd6',text_color='white',text_font=('Century Gothic',24,'bold'))
title.place(relx=0.5,rely=0.05,anchor="n")
round = ctk.CTkLabel(root,text="Select your choice to start the game",text_color='white',fg_color='#0d7dd6',text_font=('Tahoma',16,'bold'))
round.place(relx=0.5,rely=0.2,anchor='n')


pframe = ctk.CTkFrame(frame,width=300,height=200,fg_color="white")
pframe.place(relx=0.05,rely=0.5,anchor="w")

ptitle = ctk.CTkLabel(pframe,text="Player 1",text_font=('Calibri',18))
ptitle.place(relx=0.5,rely=0.05,anchor="n")

rockbtn = ctk.CTkButton(pframe,text='',image=rockimg,fg_color="white",hover_color='#f2f2f2',width=80,height=80,border_width=0,command= lambda:on_click("rock"))
rockbtn.place(relx=0.05,rely=0.5,anchor="w")
paperbtn = ctk.CTkButton(pframe,text='',image=paperimg,fg_color="white",hover_color='#f2f2f2',width=80,height=80,border_width=0,command= lambda:on_click("paper"))
paperbtn.place(relx=0.5,rely=0.5,anchor="center")
scissorsbtn = ctk.CTkButton(pframe,text='',image=scissorsimg,fg_color="white",hover_color='#f2f2f2',width=80,height=80,border_width=0,command= lambda:on_click("scissors"))
scissorsbtn.place(relx=0.95,rely=0.5,anchor="e")

pstatus = ctk.CTkLabel(pframe,text="Your Choice: ",text_font=('Calibri',14))
pstatus.place(relx=0.5,rely=0.95,anchor="s")

pscore = ctk.CTkLabel(frame,text='Your Score: 0',text_color='white',text_font=('Calibri',16))
pscore.place(relx=0.125,rely=0.8,anchor="w")


cframe = ctk.CTkFrame(frame,width=300,height=200,fg_color="white")
cframe.place(relx=0.95,rely=0.5,anchor="e")

ctitle = ctk.CTkLabel(cframe,text="Computer",text_font=('Calibri',18))
ctitle.place(relx=0.5,rely=0.05,anchor="n")

clabel = ctk.CTkLabel(cframe,text="Waiting for your selection...",text_font=('Calibri',12))
clabel.place(relx=0.5,rely=0.5,anchor="center")

cstatus = ctk.CTkLabel(cframe,text="Opponent's Choice: ",text_font=('Calibri',14))
cstatus.place(relx=0.5,rely=0.95,anchor="s")

cscore = ctk.CTkLabel(frame,text="Computer's Score: 0",text_color='white',text_font=('Calibri',16))
cscore.place(relx=0.875,rely=0.8,anchor="e")


status = ctk.CTkLabel(frame,text="vs",text_color='white',text_font=('Calibri',18))
status.place(relx=0.5,rely=0.5,anchor="center")


root.mainloop()