#ICS32 Project 5
#othello_gui.py
#
#Name: Ye Yuan
#ID: 49889946

import tkinter
import tkinter.messagebox
import logic
import math

BIG_FONT = ('Helvetica', 20)
SMALL_FONT=('Helvetica', 15)
CELL_WIDTH = 65
LINE_COLOR="white"
CANVAS_COLOR="pink"


class othello:
    def __init__(self):
        #initialize the default data
        self.begin=False
        self.col=0
        self.row=0
        
        self.window=tkinter.Tk()
        self.window.title("Othello Game Full Rules")

        self.label1=tkinter.Label(
            master=self.window, text="Welcome to the Othello game!",
            font=BIG_FONT)
        self.label1.grid(
            row = 0, column=0, padx= 10 ,pady=10, sticky= tkinter.S)
            
        self.label2=tkinter.Label(
            master=self.window, text="Before we start the game, let's do the configuration first.",
            font=('Helvetica', 15))
        self.label2.grid(
            row = 1, column=0, padx= 10, pady=10, sticky= tkinter.S)
        
        self.setting=tkinter.Button(
            master=self.window,text= "Setting",
            font=BIG_FONT,
            command=self.start_setting)
        self.setting.grid(
            row = 2, column=0, padx= 10, pady=10, sticky= tkinter.S)

        self.window.rowconfigure(0,weight=1)
        self.window.rowconfigure(1,weight=1)
        self.window.rowconfigure(2,weight=1)
        self.window.columnconfigure(0,weight=1)
        


    def run(self):
        #run the main window
        self.window.mainloop()


    def start_setting(self):
        #show the setting page of the game
        self.setting.grid_forget()
        self.label1.grid_forget()
        self.label2.grid_forget()
        self.window.title("Setting Page")

        self.l_welcome=tkinter.Label(
            master=self.window, text="Setting",
            font=('Helvetica', 30))
        self.l_welcome.grid(
            row = 0, column=0, padx= 10, pady=5, sticky= tkinter.S+ tkinter.W)

        self.l_row=tkinter.Label(
            master=self.window, text="Please enter the number of rows:",
            font=('Helvetica', 20))
        self.l_row.grid(
            row = 1, column=0, padx= 10,pady=5, sticky= tkinter.S+tkinter.W)

        self.e_row=tkinter.Entry(master= self.window,width=33, font=BIG_FONT)
        self.e_row.insert(0,"Enter an even integer between 4 and 16.")
        self.e_row.bind("<FocusIn>",lambda x:self._on_entry_click(self.e_row,'Enter an even integer between 4 and 16.'))
        self.e_row.grid(row = 2, column=0, padx= 10, sticky= tkinter.S+tkinter.W)
        
        self.l_col=tkinter.Label(
            master=self.window, text="Please enter the number of columns:",
            font=('Helvetica', 20))
        self.l_col.grid(
            row = 3, column=0, padx= 10,pady=5, sticky= tkinter.S+tkinter.W)

        self.e_col=tkinter.Entry(master= self.window,width=33, font=BIG_FONT)
        self.e_col.insert(0,"Enter an even integer between 4 and 16.")
        self.e_col.bind("<FocusIn>",lambda x:self._on_entry_click(self.e_col,'Enter an even integer between 4 and 16.'))
        self.e_col.grid(row = 4, column=0, padx= 10,   sticky= tkinter.S+tkinter.W)                


        self.l_first=tkinter.Label(
            master=self.window, text="Please choose who moves first:",
            font=('Helvetica', 20))
        self.l_first.grid(
            row = 5, column=0, padx= 10,pady=10, sticky= tkinter.S+tkinter.W)



        self.first=tkinter.StringVar()
        self.first.set("B")
        self.r_black=tkinter.Radiobutton(master= self.window,text="BLACK", value="B",variable=self.first,font=BIG_FONT)
        self.r_white=tkinter.Radiobutton(master= self.window,text="WHITE", value="W",variable=self.first,font=BIG_FONT)
        self.r_black.grid(row = 6, column=0, padx= 10,   sticky= tkinter.S+tkinter.W)
        self.r_white.grid(row = 7, column=0, padx= 10,   sticky= tkinter.S+tkinter.W)


        self.l_win=tkinter.Label(
            master=self.window, text="The player with more discs or fewer discs will win:",
            font=('Helvetica', 15))
        self.l_win.grid(
            row = 8, column=0, padx= 10,pady=10, sticky= tkinter.S+tkinter.W)

        self.win=tkinter.StringVar()
        self.win.set("M")
        self.r_more=tkinter.Radiobutton(master= self.window,text="MORE", value="M",variable=self.win,font=BIG_FONT)
        self.r_fewer=tkinter.Radiobutton(master= self.window,text="FEWER", value="F",variable=self.win,font=BIG_FONT)
        self.r_more.grid(row = 9, column=0, padx= 10,   sticky= tkinter.S+tkinter.W)
        self.r_fewer.grid(row = 10, column=0, padx= 10,   sticky= tkinter.S+tkinter.W)

        self.setting_frame=tkinter.Frame(master=self.window)
        self.setting_frame.grid(row=11,column=0, sticky=tkinter.S+tkinter.W,padx=20,pady=20)


        self.reset=tkinter.Button(
            master=self.setting_frame,text= "Reset",
            font=BIG_FONT,
            command=self.start_setting)
        self.reset.grid(
            row = 0, column=0, padx= 50, pady=10, sticky= tkinter.S)
        
        self.ok=tkinter.Button(
            master=self.setting_frame,text= "OK!",
            font=BIG_FONT,
            command=self.check_valid)
        self.ok.grid(
            row = 0, column=1, padx= 50, pady=10, sticky= tkinter.S)
        
    def _on_entry_click(self,entry:tkinter.Entry, line:str):
        #delete the default content of the entry
        if entry.get()==line:
            entry.delete(0,"end")
    def check_valid(self):
        try:
            self.col=int(self.e_col.get())
            self.row=int(self.e_row.get())
            self.turn=self.first.get()
            self.rule=self.win.get()
            self.init_board()
        except:
            tkinter.messagebox.showinfo("ERROR","Please enter valid column or row number!")
            

    def init_board(self):
        #get the initial board
        if self.col==0 and self.row==0:
            
        
        
            self.col=int(self.e_col.get())
            self.row=int(self.e_row.get())
            self.turn=self.first.get()
            self.rule=self.win.get()
            
        self.window.destroy()

        self.init_list=[]
        for i in range(self.row):
            col_list=[]
            for j in range(self.col):
                col_list.append(logic.NONE)
            self.init_list.append(col_list)
            
                
        self.window=tkinter.Tk()
        self.window.title("Othello Game Full Rules")
  
        
        self.board_canvas=tkinter.Canvas(master=self.window,
                                         width=CELL_WIDTH*self.col,
                                         height=CELL_WIDTH*self.row,
                                         background=CANVAS_COLOR)
        self.board_canvas.grid(row=0,column=0,sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self.board_canvas.bind('<Configure>',self.re_draw_board)

        self.place_frame=tkinter.Frame(master=self.window)

        self.l_ins1=tkinter.Label(
            master=self.place_frame,
            text="Please initialize the board!",
            font=BIG_FONT)
        self.l_ins2=tkinter.Label(
            master=self.place_frame,
            text="Click left mouse button to place Black dics.",
            font=('Helvetica', 15))
        self.l_ins3=tkinter.Label(
            master=self.place_frame,
            text="Click right mouse button to place White dics.",
            font=('Helvetica', 15))
        
        self.l_ins1.grid(row=0,column=0,sticky=tkinter.N + tkinter.S + tkinter.W ,padx=10,pady=5)
        self.l_ins2.grid(row=1,column=0,sticky=tkinter.N + tkinter.S + tkinter.W ,padx=10,pady=5)
        self.l_ins3.grid(row=2,column=0,sticky=tkinter.N + tkinter.S + tkinter.W ,padx=10,pady=5)
        self.place_frame.grid(row=0,column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E,padx=10,pady=0)
        self.board_canvas.grid(row=1,column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E,padx=20,pady=0)

        self.ok_frame=tkinter.Frame(master=self.window)
        self.ok_frame.grid(row=2,column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E,padx=5,pady=5)
        self.reset=tkinter.Button(
            master=self.ok_frame,text= "RESET",
            font=BIG_FONT,
            command=self.init_board)
        self.reset.grid(
            row = 0, column=0, padx= 50, pady=0, sticky= tkinter.S)
        
        self.ok=tkinter.Button(
            master=self.ok_frame,text= "START!",
            font=BIG_FONT,
            command=self.start)
        self.ok.grid(
            row = 0, column=1, padx= 50, pady=0, sticky= tkinter.S)

        self.board_canvas.bind('<Button-1>', self._left_canvas_clicked)
        self.board_canvas.bind('<Button-3>', self._right_canvas_clicked)
        
        
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)


    def re_draw_board(self,event:tkinter.Event):
        #redraw both board and dics
        self.draw_board()
        self.redraw_all_dics()


    def draw_board(self):
        #draw the board flexiblely
        self.board_canvas.delete(tkinter.ALL)
        self.height=self.board_canvas.winfo_height()
        self.width=self.board_canvas.winfo_width()
        
        for i in range(self.row):
            self.board_canvas.create_line(0,i*self.height/self.row,self.width,i*self.height/self.row,fill=LINE_COLOR)
        for j in range(self.col):
            self.board_canvas.create_line(j*self.width/self.col,0,j*self.width/self.col,self.height,fill=LINE_COLOR)
        

    def _left_canvas_clicked(self,event:tkinter.Event):
        #place a black dice
        dic_x=math.floor(event.x*self.col/self.width)
        dic_y=math.floor(event.y*self.row/self.height)
        if self.init_list[dic_y][dic_x]!=logic.NONE:
            return
        self.init_list[dic_y][dic_x]=logic.BLACK
        self.redraw_all_dics()

    def _right_canvas_clicked(self,event:tkinter.Event):
        #place a white dice
        dic_x=math.floor(event.x*self.col/self.width)
        dic_y=math.floor(event.y*self.row/self.height)
        if self.init_list[dic_y][dic_x]!=logic.NONE:
            return
        self.init_list[dic_y][dic_x]=logic.WHITE
        self.redraw_all_dics()
    
    def redraw_all_dics(self):
        #draw all the dics
        c_i=0
        for i in self.init_list:
            c_j=0
            for j in i:
                
                if j==logic.BLACK:
                    
                    self.board_canvas.create_oval(c_j*self.width/self.col,
                                                  c_i*self.height/self.row,
                                                  (c_j+1)*self.width/self.col,
                                                  (c_i+1)*self.height/self.row,
                                                  fill="black")                    
                if j==logic.WHITE:
                    self.board_canvas.create_oval(c_j*self.width/self.col,
                                                  c_i*self.height/self.row,
                                                  (c_j+1)*self.width/self.col,
                                                  (c_i+1)*self.height/self.row,
                                                  fill="white",outline="white")
                c_j+=1
            c_i+=1

        if self.begin:
            
            
            available=logic.check_available(self.game)
            
            for i in available:
                
                self.board_canvas.create_rectangle(i[1]*self.width/self.col,
                                                  i[0]*self.height/self.row,
                                                  (i[1]+1)*self.width/self.col,
                                                  (i[0]+1)*self.height/self.row,
                                                  fill="sandy brown",outline="white")

    def start(self):
        #start the main game
        self.place_frame.grid_forget()
        self.board_canvas.grid_forget()
        self.ok_frame.grid_forget()
        self.board_canvas.config(width=self.col*CELL_WIDTH,height=self.row*CELL_WIDTH)
        self.board_canvas.unbind('<Button-1>')
        self.board_canvas.unbind('<Button-3>')
        self.game=logic.game(self.col,self.row,self.rule,self.init_list)
        if self.turn=="B":
            self.game.turn=logic.BLACK
        if self.turn=="W":
            self.game.turn=logic.WHITE
        self.begin=True

        self.rule_frame=tkinter.Frame(master=self.window)
        self.l_turn_ins=tkinter.Label(
            master=self.rule_frame,
            text="Turn:",
            font=SMALL_FONT)
        self.turntext=tkinter.StringVar()
        if self.game.turn==logic.BLACK:
            self.turntext.set("BLACK")
        else:   
            self.turntext.set("WHITE")
        self.l_turn=tkinter.Label(
            master=self.rule_frame,
            textvariable=self.turntext,
            font=SMALL_FONT)

        self.l_black=tkinter.Label(
            master=self.rule_frame,
            text="Black:",
            font=SMALL_FONT)
        self.blacktext=tkinter.StringVar()
        self.blacktext.set(self.game.b)

        self.l_black_n=tkinter.Label(
            master=self.rule_frame,
            textvariable=self.blacktext,
            font=SMALL_FONT)

        self.l_white=tkinter.Label(
            master=self.rule_frame,
            text="White:",
            font=SMALL_FONT)
        self.whitetext=tkinter.StringVar()
        self.whitetext.set(self.game.w)
        self.l_white_n=tkinter.Label(
            master=self.rule_frame,
            textvariable=self.whitetext,
            font=SMALL_FONT)

        self.l_win=tkinter.Label(
            master=self.rule_frame,
            text="Winner:",
            font=SMALL_FONT)
        self.winnertext=tkinter.StringVar()
        self.winnertext.set(self.game.winner)
        self.l_winner=tkinter.Label(
            master=self.rule_frame,
            textvariable=self.winnertext,
            font=SMALL_FONT)

        self.l_turn_ins.grid(row=0,column=0,
                             sticky=tkinter.N + tkinter.S + tkinter.W ,
                             padx=10,pady=5)
        self.l_turn.grid(row=1,column=0,
                             sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E,
                             padx=10,pady=5)

        self.l_black.grid(row=2,column=0,
                             sticky=tkinter.N + tkinter.S + tkinter.W ,
                             padx=10,pady=5)
        self.l_black_n.grid(row=3,column=0,
                             sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E,
                             padx=10,pady=5)
        self.l_white.grid(row=4,column=0,
                             sticky=tkinter.N + tkinter.S + tkinter.W ,
                             padx=10,pady=5)
        self.l_white_n.grid(row=5,column=0,
                             sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E,
                             padx=10,pady=5)
        self.l_win.grid(row=6,column=0,
                             sticky=tkinter.N + tkinter.S + tkinter.W ,
                             padx=10,pady=5)
        self.l_winner.grid(row=7,column=0,
                             sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E,
                             padx=10,pady=5)
        self.board_canvas.grid(row=0,column=0,padx=0,pady=0,
                               sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self.rule_frame.grid(row=0,column=1,padx=0,pady=10,
                               sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self.board_canvas.bind('<Button-1>',self.hundle_click)

        
        self.window.rowconfigure(0,weight=1)
        self.window.columnconfigure(0,weight=1)

    def hundle_click(self,event:tkinter.Event):
        #this function can hundle all posible event 
        dic_x=math.floor(event.x*self.col/self.width)
        dic_y=math.floor(event.y*self.row/self.height)
        if [dic_y,dic_x] not in logic.check_available(self.game):
            return
        self.init_list=logic.move(self.game,[dic_y,dic_x])
        self.game.next()
        self.game.count_number()
        if self.game.turn==logic.BLACK:
            self.turntext.set("BLACK")
        else:   
            self.turntext.set("WHITE")        
        
        self.blacktext.set(self.game.b)
        self.whitetext.set(self.game.w)
        if logic.check_available(self.game)==[]:
            self.game.next()
            self.game.count_number()
            if self.game.turn==logic.BLACK:
                self.turntext.set("BLACK")
            else:   
                self.turntext.set("WHITE")        
        
            self.blacktext.set(self.game.b)
            self.whitetext.set(self.game.w)
        
        
        self.draw_board()
        self.redraw_all_dics()

        if logic.check_available(self.game)==[]:
            self.game.get_winner()
            self.winnertext.set(self.game.winner)
        




def main():
    game=othello()
    game.run()


if __name__=="__main__":
    main()
