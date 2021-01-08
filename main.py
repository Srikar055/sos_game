from time import sleep
player=0
points=[0,0]
player1=''
player2=''
def main() :
    global player1
    global player2
    board=[]
    for i in range(1,50):
        board.append(i)
    print('Welcome to the SOS game')

    sleep(0.5)
    print('The game is about to start')
    sleep(0.5)
    player1=input('Enter player 1 name ')
    player2=input('Enter player 2 name ')
    display_board(board)
    user_move(board)



def display_board(board):
    end = ' '
    for i in range(1,50):
        if i==1:end=''
        end+=''+str(board[i-1])
        if i <10 or board[i-1] in ('S','O'):
            end+=' '
        end+=' | '
        if i%7==0 and i!=49:
            end+='\n---------------------------------\n'
    print('',end=end)
    print('\n')

def can_win(board,pos,value):
    count=0
    global points
    global player
    if value=='O':
        #right/left
        if 48>=pos-2>=0 and 48>=pos>=0 and pos%7!=1 and pos%7!=0:
            if board[pos-2] == board[pos]:
                count+=1
        #up/down
        if 48>=pos-8>=0 and 48>=pos+6>=0 and pos>7 and pos<43:
            if board[pos-8] == board[pos+6]:
                count+=1
        #rightdiagnal
        if 48>=pos-9>=0 and 48>=pos+7>=0 and pos%7!=0 and pos<43:
            if board[pos - 9] == board[pos + 7]:
                count += 1
        #leftdiagnal
        if 48>=pos-7>=0 and 48>=pos+5>=0 and pos%7!=1 and pos<43:
            if board[pos - 7] == board[pos + 5]:
                count += 1

    if value=='S':
        # right
        if 48 >= pos - 1 >= 0 and 48 >= pos + 1 >= 0 and board[pos]=='O' and pos%7!=6 and pos%7!=0:
            if board[pos - 1] == board[pos + 1]:
                count+=1
        # left
        if 48 >= pos - 1 >=0 and 48 >= pos - 3 >= 0 and board[pos-2]=='O' and pos%7!=1 and pos%7!=2:
            if board[pos - 1] == board[pos - 3]:
                count+=1
        # up
        if 48 >= pos - 1 >= 0 and 48 >= pos - 15 >= 0 and board[pos-8]=='O':
            if board[pos - 1] == board[pos - 15]:
                count+=1
        # down
        if 48 >= pos - 1 >= 0 and 48 >= pos + 13 >= 0 and board[pos+6]=='O':
            if board[pos - 1] == board[pos + 13]:
                count+=1
        # rbd
        if 48 >= pos - 1 >= 0 and 48 >= pos + 15 >= 0 and board[pos+7]=='O' and pos%7!=6 and pos%7!=0 and pos<36:
            if board[pos - 1] == board[pos + 15]:
                count+=1
        # lbd
        if 48 >= pos - 1 >= 0 and 48 >= pos + 11 >= 0 and board[pos+5]=='O' and pos%7!=1 and pos%7!=2 and pos<36:
            if board[pos - 1] == board[pos + 11]:
                count+=1
        # rad
        if 48 >= pos - 1 >= 0 and 48 >= pos - 13 >= 0 and board[pos-7]=='O' and pos%7!=6 and pos%7!=0 and pos>14:
            if board[pos - 1] == board[pos - 13]:
                count+=1
        # lad
        if 48 >= pos - 1 >= 0 and 48 >= pos - 17 >= 0 and board[pos-9]=='O' and pos%7!=1 and pos%7!=2 and pos>14:
            if board[pos - 1] == board[pos - 17]:
                count+=1

    if count>0:
        points[player%2]+=count
        return True
    return False

def make_move (board, pos, value):
    global player
    print(board[pos-7],board[pos+5])
    if board[pos-1] == pos:
        board[pos-1] = value
        display_board(board)
        win = can_win(board , pos , value)
        if win:
            player = player
        else:
            player += 1
    else:
        print('already occupied,please select diff location')
        user_move(board)


def user_move(board):
    global player
    print(player1,"'s points : ",points[0])
    print(player2,"'s points : ",points[1])
    if player%2==0:
        print('Player ',player1,"'s turn,"'please enter the position and the key (S/O) \n')
    else:
        print('Player ', player2, "'s turn,"'please enter the position and the key (S/O) \n')
    try:
        pos = int(input())
        value = (input())
        if value in ('S','O') and 1<=pos<=49:
            make_move(board, pos, value)
            for i in board:
                if type(i) == int:
                    user_move(board)
    except ValueError as e:
        print('Invalid input')
    print('Invalid data')
    user_move(board)

def computer_move():
    return False

main()