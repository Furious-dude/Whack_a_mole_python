import tkinter as tk
import random
import time

mainwindow = tk.Tk()
mainwindow.title('Main')
mainwindow.geometry('500x500')
mainwindow.configure(background='aquamarine4')

highscore_1 = 0
timer_list = ["##########","#########","########","#######","######","#####","####","###","##","#"," "]


def move():#this randomizes the position the next button will be in
    val2 = random.randrange(0,500,20)
    val1 = random.randrange(0,500,20)
    
    Button1.place(x=val1,y=val2)

def back_to_place():#this sets the button1 to the original place
    Button1.place(x=125,y=0)
    global highscore_1
    highscore_1 = 0
    highscore_label.config(text='Your highscore:' + str(highscore_1))
    highscore_label.pack()

def highscore():
    global highscore_1
    #this declaration is needed so i can access the global variable
    highscore_1 +=1
    highscore_label.config(text='Your highscore:' + str(highscore_1))
    highscore_label.pack()
    





#this is a workaround solution, as tk.button doesnt take more than one command, i have to make do with this way
def combination():

    highscore()
    move()
    
highscore_label = tk.Label(mainwindow)
time_lable = tk.Label(mainwindow)



Button1 = tk.Button(mainwindow,text='No',padx=20,pady=20,width=2,bg='blue',activebackground='red',command=combination)
Button1.place(x=125,y=0)

Button2 = tk.Button(mainwindow,text='Replay',padx=20,pady=20,width=2,activebackground='green',command=back_to_place)
Button2.place(x=0,y=0)

# quit_button = tk.Button(mainwindow,text='X',bg = 'red',command=mainwindow.destroy,padx=5)
# quit_button.place(x=480,y=0)

#showing decreasing  '#' on the screen as time closes by,11 seconds
# for i in range(11):
    
#     i-=1
#     # time_lable.config(text=timer_list[i])
#     # time_lable.pack()
#     time_lable.config(text='you have '+str(i)+' seconds remaining')
#     time_lable.pack()
    
#this timer function is too buggy rightnow

mainwindow.resizable(False,False)#so that it cannot be resized, no one can cheat
mainwindow.mainloop()