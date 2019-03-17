#ICS32 Project 5
#logic.py
#
#Name: Ye Yuan
#ID: 49889946



BLACK=1
WHITE=-1
NONE=0

class game:

    def __init__(self,col:int,row:int,rule:str,board:list):
        #initialize some variables
        self.col_size=col
        self.row_size=row
        self.turn=None
        self.rule=rule
        self.board=board
        self.w=0
        self.b=0
        self.winner="NONE"
        self.count_number()
        
    def next(self):
        #move to next turn
        if self.turn==BLACK:
            self.turn=WHITE
        else:
            self.turn=BLACK

    
    def count_number(self):
        #count the number of dics of each player
        self.b=0
        self.w=0
        for i in self.board:
            for j in i:
                if j==BLACK:
                    self.b+=1
                if j==WHITE:
                    self.w+=1

    
    def get_winner(self):
        #display the winner
        
        if self.b==self.w:
            self.winner="NONE"
        if self.rule=="M":
            if self.b>self.w:
                self.winner="BLACK"
            elif self.b<self.w:
                self.winner="WHITE"
        if self.rule=="F":
            if self.b>self.w:
                self.winner="WHITE"
            elif self.b<self.w:
                self.winner="BLACK"
    

def get_move()->list:
    #get the move from input and return it as list
    i=input().split()
    move=[]
    for num in i:
        move.append(int(num)-1)
    return move

def eat_1(game:game,r:int,c:int,index:bool)->bool:
    #determine whether the left top is valid 
    if r-1>=0 and r-1<game.row_size and c-1>=0 and c-1<game.col_size:
        if game.board[r-1][c-1]==NONE:
            #print("r-1",r-1,"c-1",c-1)
            return False

        if game.board[r-1][c-1]==game.turn:
            if index==True:
                return False
            else:
                return True
        else:
            return eat_1(game,r-1,c-1,False)
    else:
        return False


def eat_2(game:game,r:int,c:int,index:bool)->bool:
    #determine whether the position of top is valid
    if r-1>=0 and r-1<game.row_size and c>=0 and c<game.col_size:
        if game.board[r-1][c]==NONE:
            return False

        if game.board[r-1][c]==game.turn:
            if index==True:
                return False
            else:
                return True
        else:
            return eat_2(game,r-1,c,False)
    else:
        return False    


def eat_3(game:game,r:int,c:int,index:bool)->bool:
    #determine whether the right top is valid
    if r-1>=0 and r-1<game.row_size and c+1>=0 and c+1<game.col_size:
        if game.board[r-1][c+1]==NONE:
            return False

        if game.board[r-1][c+1]==game.turn:
            if index==True:
                return False
            else:
                return True
        else:
            return eat_3(game,r-1,c+1,False)
    else:
        return False    

def eat_4(game:game,r:int,c:int,index:bool)->bool:

    if r>=0 and r<game.row_size and c-1>=0 and c-1<game.col_size:
        if game.board[r][c-1]==NONE:
            return False


        if game.board[r][c-1]==game.turn:
            
            if index==True:
                return False
            else:
                return True
        else:
            return eat_4(game,r,c-1,False)
    else:
        return False    

def eat_5(game:game,r:int,c:int,index:bool)->bool:
    if r>=0 and r<game.row_size and c+1>=0 and c+1<game.col_size:
        if game.board[r][c+1]==NONE:
            return False
        #print(game.board[r][c+1],game.board[r][c])

        if game.board[r][c+1]==game.turn:
            
            if index==True:
                return False
            else:
                return True
        else:
            return eat_5(game,r,c+1,False)
    else:
        return False    

def eat_6(game:game,r:int,c:int,index:bool)->bool:
    if r+1>=0 and r+1<game.row_size and c-1>=0 and c-1<game.col_size:
        if game.board[r+1][c-1]==NONE:
            return False

        if game.board[r+1][c-1]==game.turn:
            if index==True:
                return False
            else:
                return True
        else:
            return eat_6(game,r+1,c-1,False)
    else:
        return False    

def eat_7(game:game,r:int,c:int,index:bool)->bool:
    if r+1>=0 and r+1<game.row_size and c>=0 and c<game.col_size:
        if game.board[r+1][c]==NONE:
            return False

        if game.board[r+1][c]==game.turn:
            if index==True:
                return False
            else:
                return True
        else:
            return eat_7(game,r+1,c,False)
    else:
        return False    

def eat_8(game:game,r:int,c:int,index:bool)->bool:
    if r+1>=0 and r+1<game.row_size and c+1>=0 and c+1<game.col_size:
        if game.board[r+1][c+1]==NONE:
            return False
    
        if game.board[r+1][c+1]==game.turn:
            if index==True:
                return False
            else:
                return True
        else:
            return eat_8(game,r+1,c+1,False)
    else:
        return False    


def eat(game:game,r:int,c:int)->bool:
    #any funcs in below is true will return true
    if eat_1(game,r,c,True)==True:
        #print("eat_1 return true")
        return True
    elif eat_2(game,r,c,True)==True:
        #print("eat_2 return true")
        return True
    elif eat_3(game,r,c,True)==True:
        #print("eat_3 return true")
        return True
    elif eat_4(game,r,c,True)==True:
        #print("eat_4 return true")
        return True
    elif eat_5(game,r,c,True)==True:
        #print("eat_5 return true")
        return True
    elif eat_6(game,r,c,True)==True:
        #print("eat_6 return true")
        return True
    elif eat_7(game,r,c,True)==True:
        #print("eat_7 return true")
        return True
    elif eat_8(game,r,c,True)==True:
        #print("eat_8 return true")
        return True
    #print("false at eat")
    return False


def check_available(game:game)->list:
    #check the available position for the current player and return it as list
    available=[]
    for r in range(game.row_size):
        for c in range(game.col_size):
            
            if r<0 or r>=game.row_size or c<0 or c>=game.col_size:
                continue
            if game.board[r][c] != NONE:
                
                continue
            if eat(game,r,c)==False:
                
                continue
            else:
                
                available.append([r,c])
    
    return available

def return_move(game:game)->list:
    #return the available move list
    while True:
        move=get_move()
        if move in check_available(game):
            print("VALID")
            return move
        else:
            print("INVALID")


def move_1(game:game,r:int,c:int,index:bool)->bool:
    #move the dics in left top direction 
    if r-1>=0 and r-1<game.row_size and c-1>=0 and c-1<game.col_size:
        if game.board[r-1][c-1]==NONE:
            return game.board
    
        if game.board[r-1][c-1]==game.turn:
            if index==True:
                return game.board
            else:
                game.board[r][c]=game.turn
                while game.board[r+1][c+1]==0-game.turn:
                    game.board[r+1][c+1]=game.turn
                    r+=1
                    c+=1                
                return True
        else:
            return move_1(game,r-1,c-1,False)
    else:
        return game.board    
        
def move_2(game:game,r:int,c:int,index:bool)->bool:
    #move the dics in top direction
    if r-1>=0 and r-1<game.row_size and c>=0 and c<game.col_size:
        if game.board[r-1][c]==NONE:
            return game.board
    
        if game.board[r-1][c]==game.turn:
            if index==True:
                return game.board
            else:
                game.board[r][c]=game.turn
                while game.board[r+1][c]==0-game.turn:
                    game.board[r+1][c]=game.turn
                    r+=1
                                    
                return True
        else:
            return move_2(game,r-1,c,False)
    else:
        return game.board    

def move_3(game:game,r:int,c:int,index:bool)->bool:
    if r-1>=0 and r-1<game.row_size and c+1>=0 and c+1<game.col_size:
        if game.board[r-1][c+1]==NONE:
            return game.board
    
        if game.board[r-1][c+1]==game.turn:
            if index==True:
                return game.board
            else:
                game.board[r][c]=game.turn
                while game.board[r+1][c-1]==0-game.turn:
                    game.board[r+1][c-1]=game.turn
                    r+=1
                    c-=1                
                return True
        else:
            return move_3(game,r-1,c+1,False)
    else:
        return game.board    

def move_4(game:game,r:int,c:int,index:bool)->bool:
    if r>=0 and r<game.row_size and c-1>=0 and c-1<game.col_size:
        if game.board[r][c-1]==NONE:
            return game.board
    
        if game.board[r][c-1]==game.turn:
            if index==True:
                return game.board
            else:
                game.board[r][c]=game.turn
                while game.board[r][c+1]==0-game.turn:
                    game.board[r][c+1]=game.turn
                    
                    c+=1                
                return True
        else:
            return move_4(game,r,c-1,False)
    else:
        return game.board    

def move_5(game:game,r:int,c:int,index:bool)->bool:
    if r>=0 and r<game.row_size and c+1>=0 and c+1<game.col_size:
        if game.board[r][c+1]==NONE:
            return game.board
    
        if game.board[r][c+1]==game.turn:
            if index==True:
                return game.board
            else:
                game.board[r][c]=game.turn
                while game.board[r][c-1]==0-game.turn:
                    game.board[r][c-1]=game.turn
                    
                    c-=1                
                return True
        else:
            return move_5(game,r,c+1,False)
    else:
        return game.board    

def move_6(game:game,r:int,c:int,index:bool)->bool:
    if r+1>=0 and r+1<game.row_size and c-1>=0 and c-1<game.col_size:
        if game.board[r+1][c-1]==NONE:
            return game.board
    
        if game.board[r+1][c-1]==game.turn:
            if index==True:
                return game.board
            else:
                game.board[r][c]=game.turn
                while game.board[r-1][c+1]==0-game.turn:
                    game.board[r-1][c+1]=game.turn
                    r-=1
                    c+=1                
                return True
        else:
            return move_6(game,r+1,c-1,False)
    else:
        return game.board    

def move_7(game:game,r:int,c:int,index:bool)->bool:
    if r+1>=0 and r+1<game.row_size and c>=0 and c<game.col_size:
        if game.board[r+1][c]==NONE:
            return game.board
    
        if game.board[r+1][c]==game.turn:
            if index==True:
                return game.board
            else:
                game.board[r][c]=game.turn
                while game.board[r-1][c]==0-game.turn:
                    game.board[r-1][c]=game.turn
                    r-=1
                                   
                return True
        else:
            return move_7(game,r+1,c,False)
    else:
        return game.board    


def move_8(game:game,r:int,c:int,index:bool)->bool:
    if r+1>=0 and r+1<game.row_size and c+1>=0 and c+1<game.col_size:
        if game.board[r+1][c+1]==NONE:
            return game.board
    
        if game.board[r+1][c+1]==game.turn:
            if index==True:
                return game.board
            else:
                game.board[r][c]=game.turn
                while game.board[r-1][c-1]==0-game.turn:
                    game.board[r-1][c-1]=game.turn
                    r-=1
                    c-=1                
                return True
        else:
            return move_8(game,r+1,c+1,False)
    else:
        return game.board    



def move(game:game,move:list):
    #move all the directions
    game.board[move[0]][move[1]]=game.turn
    board=move_1(game,move[0],move[1],True)
    board=move_2(game,move[0],move[1],True)
    board=move_3(game,move[0],move[1],True)
    board=move_4(game,move[0],move[1],True)
    board=move_5(game,move[0],move[1],True)
    board=move_6(game,move[0],move[1],True)
    board=move_7(game,move[0],move[1],True)
    board=move_8(game,move[0],move[1],True)
    return game.board






    

    
    

