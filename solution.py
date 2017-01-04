class Space:
    def __init__(self):
        self.value = -1;
        self.mutable = True

    def setImmutable(self, value):
        self.value = value;
        self.mutable = False;

def printboard(board):
    print """
   %d     %d      %d     %d
    %d      %d   %d     %d
 %d        %d     %d       %d
 %d  %d  %d  %d     %d  %d  %d  %d
 %d  %d  %d  %d     %d  %d  %d  %d
 %d        %d     %d       %d
    %d      %d   %d     %d
   %d     %d      %d     %d
    """ % tuple([x.value for x in board])

board = [Space() for _ in xrange(40)]

def valid(board):

    def checkRange(quad):
        count = [2 for _ in xrange(10)]
        for i in quad:
            if board[i].value >= 0:
                count[board[i].value] -= 1
                if count[board[i].value] < 0:
                    return False

        count = [2 for _ in xrange(10)]
        for i in [x for x in xrange(40) if x not in quad]:
            if board[i].value >= 0:
                count[board[i].value] -= 1
                if count[board[i].value] < 0:
                    return False

        return True

    def isPrime(a, b):
        if board[a].value == -1 or board[b].value == -1: 
            return True
        return (board[a].value*10 + board[b].value) in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    if not (isPrime(0, 1) and  \
           isPrime(2, 3) and  \
           isPrime(8, 12) and \
           isPrime(11, 19) and \
           isPrime(20, 28) and  \
           isPrime(27, 31) and \
           isPrime(36, 37) and \
           isPrime(38, 39)):
        return False

    vertical = [0, 1, 4, 5, 8, 9,
                12, 13, 14, 15,
                20, 21, 22, 23,
                28, 29, 32, 33, 36, 37]
    if not checkRange(vertical): return False

    hoizontal = range(20)
    if not checkRange(hoizontal): return False

    topleftbottomright = [4, 8, 9,
                          12, 13, 14, 15, 16, 17, 18,
                          21, 22, 23, 24, 25, 26, 27,
                          30, 31, 35]
    if not checkRange(topleftbottomright): return False


    bottomlefttopright = [7, 10, 11,
                          13, 14, 15, 16, 17, 18, 19,
                          21, 22, 23, 24, 25, 26, 27,
                          30, 31, 35]
    if not checkRange(bottomlefttopright): return False


    topleftbottomrightv = [0, 1, 4, 5, 6, 9, 10,
                           14, 15, 16,
                           23, 24, 25, 
                           29, 30, 33, 34, 35, 38, 39]
    if not checkRange(topleftbottomrightv): return False


    bottomlefttoprightv = [2, 3, 5, 6, 7, 9, 10,
                          15, 16, 17,
                          22, 23, 24,
                          29, 30, 32, 33, 34, 36, 37]
    if not checkRange(bottomlefttoprightv): return False

    return True


path = [0, 1, 2, 3, 8, 12, 11, 19, 20, 28, 27, 31, 36, 37, 38, 39,
        15, 16, 23, 24,
        9, 10, 14, 22, 17, 25, 29, 30,
        4, 5, 6, 7,
        13, 21, 18, 26,
        32, 33, 34, 35]
        
def prevState(state, board):
    state -= 1
    while not board[path[state]].mutable:
        state -= 1
    return state

def nextState(state, board):
    state += 1
    while not board[path[state]].mutable:
        state += 1
    return state

board[10].setImmutable(7);
board[15].setImmutable(0);
board[21].setImmutable(6);
board[23].setImmutable(5);
board[29].setImmutable(3);
board[33].setImmutable(6);
board[36].setImmutable(2);

solved = False
state = 0
maxState = -1

while not solved:
    if maxState < state:
        print state
        maxState = state
    board[path[state]].value += 1
    while board[path[state]].value < 10 and not valid(board):
        board[path[state]].value += 1;
    if board[path[state]].value == 10:
        board[path[state]].value = -1
        state = prevState(state, board);
    elif state == 39:
        solved = True
    else:
        state = nextState(state, board);

printboard(board)