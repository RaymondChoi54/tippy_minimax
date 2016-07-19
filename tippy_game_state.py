from game_state import GameState
from tippy_move import TippyMove


class TippyGameState(GameState):
    ''' The state of a Tippy game.
    
    board_length: int   --- dimension of the board
    '''

    def __init__(self, p, interactive=False, 
                 board_length=0, moves_p1=[], moves_p2=[]):
        ''' (TippyGameState, str, bool, str) -> NoneType

        Initialize TippyGameState self with board_length as the dimension of
        the board

        Assume:  3 <= board_length is an int
                        p in {'p1', 'p2'}
        '''
        if interactive:
            board_length = int(input('What board size do you want? '))
        GameState.__init__(self, p)
        self.board_length = board_length
        self.instructions = ('Tippy is a variation of tic-tac-toe. '+
        'Win the game by forming a z shape in four grids.')
        self.moves_p1 = moves_p1
        self.moves_p2 = moves_p2
        if (self.winner('p1')
                or self.winner('p2')
                or self.possible_next_moves() == []):
            self.over = True

    def __repr__(self):
        ''' (TippyGameState) -> str

        Return a string representation of TippyGameState self
        that evaluates to an equivalent TippyGameState

        >>> s = TippyGameState('p1', board_length=4, moves_p1 = [(2, 2)],\
        moves_p2 = [(3, 2)])
        >>> s
        TippyGameState(4*4 board, p1, p1:[(2, 2)], p2:[(3, 2)])
        '''
        return 'TippyGameState({}, {}, {}, {})'.format(
            (str(self.board_length) + '*' + str(self.board_length) + ' board'), 
            (self.next_player), 
            ('p1:' + str(self.moves_p1)),
            ('p2:' + str(self.moves_p2)))

    def __str__(self):
        ''' (TippyGameState) -> str

        Return a convenient string representation of TippyGameState self.

        >>> s = TippyGameState('p1', board_length=4, \
        moves_p1 = [(2, 2)], moves_p2 = [])
        >>> print(s)
        Board Length: 4; p1 squares [(2, 2)], p2 squares []; next player: p1
        '''
        return (
            'Board Length: {}; p1 squares {}, p2 squares {}; next player: {}'
            .format(str(self.board_length), str(self.moves_p1),
                    str(self.moves_p2), str(self.next_player)))

    def __eq__(self, other):
        ''' (TippyGameState, TippyGameState) -> bool

        Return True iff this TippyGameState equivalent to other.

        >>> s1 = TippyGameState('p1', board_length=4, moves_p1 = [(2, 2)],\
        moves_p2 = [(3, 2)])
        >>> s2 = TippyGameState('p1', board_length=4, moves_p1 = [(2, 2)],\
        moves_p2 = [(3, 2)])
        >>> s1 == s2
        True
        '''
        return (isinstance(other, TippyGameState) and
                self.board_length == other.board_length and
                self.next_player == other.next_player and
                self.moves_p1 == other.moves_p1 and
                self.moves_p2 == other.moves_p2)
    
    def possible_next_coords(self):
        ''' (TippyGameState) -> list of tuples

        Return a list of legal moves (as coordinates) of the present state.

        >>> t1 = TippyGameState('p1', board_length = 3)
        >>> t1.moves_p1 = [(2, 2), (1, 2)]
        >>> t1.moves_p2 = [(3, 2), (3, 1)]
        >>> L1 = t1.possible_next_coords()
        >>> L2 = [(1, 1), (1, 3), (2, 1), (2, 3),(3, 3)]
        >>> len(L1) == len(L2) and all([m in L2 for m in L1])
        True
        '''
            
        all_list = []
        if self.winner('p1') or self.winner('p2'):
            return all_list
            
        for x in range(1, self.board_length + 1):
            for y in range(1, self.board_length + 1):
                all_list.append(tuple((x, y)))
                    
        for coord in self.moves_p1:
            all_list.remove(coord)
            
        for coord in self.moves_p2:
            all_list.remove(coord)        
            
        return all_list   

    def possible_next_moves(self):
        ''' (TippyGameState) -> list of TippyMove

        Return a list of legal moves (as TippyMove) of the present state.

        >>> t1 = TippyGameState('p1', board_length = 3)
        >>> t1.moves_p1 = [(2, 2), (1, 2)]
        >>> t1.moves_p2 = [(3, 2), (3, 1)]
        >>> L1 = t1.possible_next_moves()
        >>> L2 = [TippyMove((1, 1)), TippyMove((1, 3)), TippyMove((2, 1)),\
        TippyMove((2, 3)), TippyMove((3, 3))]
        >>> len(L1) == len(L2) and all([m in L2 for m in L1])
        True
        '''
        
        all_list = self.possible_next_coords()      
        
        return [TippyMove(c)
                for c in all_list]
    
    def get_move(self):
        '''(TippyGameState) -> TippyMove

        Prompt user for x and y coordinate of a move and return move.
        '''
        x = int(input
                ('What is the x coordniate of the square you want to play? ')
                )
        y = int(input
                ('What is the y coordniate of the square you want to play? ')
                )
        move = TippyMove((x, y))
        return move
    
    def apply_move(self, move):
        ''' (TippyGameState, TippyMove) -> TippyGameState
    
        Return the new TippyGameState reached by applying move to self.
    
        >>> t1 = TippyGameState('p1', board_length=5, moves_p1 = [], \
        moves_p2 = [])
        >>> t2 = t1.apply_move(TippyMove((1, 2)))
        >>> print(t2)
        Board Length: 5; p1 squares [(1, 2)], p2 squares []; next player: p2
        '''
        if move in self.possible_next_moves():
            if self.next_player == "p1":
                copy = []
                for c in self.moves_p1:
                    copy.append(c)
                copy.append(move.coord)                
                return TippyGameState(self.opponent(), 
                                      board_length=self.board_length, 
                                      moves_p1=copy, 
                                      moves_p2=self.moves_p2
                                      )
            else:
                copy = []
                for c in self.moves_p2:
                    copy.append(c)
                copy.append(move.coord)                   
                return TippyGameState(self.opponent(), 
                                      board_length=self.board_length,
                                      moves_p1=self.moves_p1,
                                      moves_p2=copy
                                      )
        else:
            return None

    def rough_outcome(self):
    
        '''(TippyGameState) -> float

        Return an estimate in interval [LOSE, WIN] of best outcome next_player
        can guarantee from state self.

        >>> TippyGameState('p1', board_length=5, \
        moves_p1 = [(3, 3), (4, 3), (3, 2)], \
        moves_p2 = [(1, 1), (1, 2), (1, 3)]).rough_outcome()
        1.0
        >>> TippyGameState('p1', board_length=5, \
        moves_p1 = [(1, 1), (1, 2), (1, 3)], \
        moves_p2 = [(3, 3), (4, 3), (3, 2)]).rough_outcome()
        -1.0
        >>> TippyGameState('p2', board_length=5, \
        moves_p1 = [(3, 3), (4, 3), (3, 2)], \
        moves_p2 = [(1, 1), (1, 2), (1, 3)]).rough_outcome()
        -1.0
        >>> TippyGameState('p2', board_length=5, \
        moves_p1 = [(1, 1), (1, 2), (1, 3)], \
        moves_p2 = [(3, 3), (4, 3), (3, 2)]).rough_outcome()
        1.0
        '''
        
        if self.next_player == 'p1':
            for x in self.moves_p1:
                if 1 and self.board_length not in x:
                    row_1 = (x[0] + 1, x[1])
                    row_2 = (x[0] - 1, x[1])
                    col_1 = (x[0], x[1] + 1)
                    col_2 = (x[0], x[1] - 1)
                    diag_1 = (x[0] - 1, x[1] + 1)
                    diag_2 = (x[0] + 1, x[1] + 1)
                    diag_3 = (x[0] + 1, x[1] - 1)
                    diag_4 = (x[0] - 1, x[1] - 1)
                    if ((row_1 in self.moves_p1 and col_1 in self.moves_p1) and
                        (diag_1 in self.possible_next_coords() or 
                         diag_3 in self.possible_next_coords())) or\
                       ((row_1 in self.moves_p1 and col_2 in self.moves_p1) and 
                        (diag_2 in self.possible_next_coords() or 
                         diag_4 in self.possible_next_coords())) or\
                       ((row_2 in self.moves_p1 and col_2 in self.moves_p1) and 
                        (diag_1 in self.possible_next_coords() or 
                         diag_3 in self.possible_next_coords())) or\
                       ((row_2 in self.moves_p1 and col_1 in self.moves_p1) and 
                        (diag_2 in self.possible_next_coords() or 
                         diag_4 in self.possible_next_coords())):
                        return TippyGameState.WIN
            for x in self.moves_p2:
                if 1 and self.board_length not in x:
                    row_1 = (x[0] + 1, x[1])
                    row_2 = (x[0] - 1, x[1])
                    col_1 = (x[0], x[1] + 1)
                    col_2 = (x[0], x[1] - 1)
                    diag_1 = (x[0] - 1, x[1] + 1)
                    diag_2 = (x[0] + 1, x[1] + 1)
                    diag_3 = (x[0] + 1, x[1] - 1)
                    diag_4 = (x[0] - 1, x[1] - 1)
                    if ((row_1 in self.moves_p2 and col_1 in self.moves_p2) and
                        (diag_1 in self.possible_next_coords() and
                         diag_3 in self.possible_next_coords())) or\
                       ((row_1 in self.moves_p2 and col_2 in self.moves_p2) and
                        (diag_2 in self.possible_next_coords() and
                         diag_4 in self.possible_next_coords())) or\
                       ((row_2 in self.moves_p2 and col_2 in self.moves_p2) and
                        (diag_1 in self.possible_next_coords() and
                         diag_3 in self.possible_next_coords())) or\
                       ((row_2 in self.moves_p2 and col_1 in self.moves_p2) and
                        (diag_2 in self.possible_next_coords() and
                         diag_4 in self.possible_next_coords())):
                        return TippyGameState.LOSE 
            return TippyGameState.DRAW
            
        elif self.next_player == 'p2':
            for x in self.moves_p2:
                if 1 and self.board_length not in x:
                    row_1 = (x[0] + 1, x[1])
                    row_2 = (x[0] - 1, x[1])
                    col_1 = (x[0], x[1] + 1)
                    col_2 = (x[0], x[1] - 1)
                    diag_1 = (x[0] - 1, x[1] + 1)
                    diag_2 = (x[0] + 1, x[1] + 1)
                    diag_3 = (x[0] + 1, x[1] - 1)
                    diag_4 = (x[0] - 1, x[1] - 1)
                    if ((row_1 in self.moves_p2 and col_1 in self.moves_p2) and
                        (diag_1 in self.possible_next_coords() or 
                         diag_3 in self.possible_next_coords())) or\
                       ((row_1 in self.moves_p2 and col_2 in self.moves_p2) and 
                        (diag_2 in self.possible_next_coords() or 
                         diag_4 in self.possible_next_coords())) or\
                       ((row_2 in self.moves_p2 and col_2 in self.moves_p2) and 
                        (diag_1 in self.possible_next_coords() or 
                         diag_3 in self.possible_next_coords())) or\
                       ((row_2 in self.moves_p2 and col_1 in self.moves_p2) and 
                        (diag_2 in self.possible_next_coords() or 
                         diag_4 in self.possible_next_coords())):
                        return TippyGameState.WIN
            for x in self.moves_p1:
                if 1 and self.board_length not in x:
                    row_1 = (x[0] + 1, x[1])
                    row_2 = (x[0] - 1, x[1])
                    col_1 = (x[0], x[1] + 1)
                    col_2 = (x[0], x[1] - 1)
                    diag_1 = (x[0] - 1, x[1] + 1)
                    diag_2 = (x[0] + 1, x[1] + 1)
                    diag_3 = (x[0] + 1, x[1] - 1)
                    diag_4 = (x[0] - 1, x[1] - 1)
                    if ((row_1 in self.moves_p1 and col_1 in self.moves_p1) and
                        (diag_1 in self.possible_next_coords() and 
                         diag_3 in self.possible_next_coords())) or\
                       ((row_1 in self.moves_p1 and col_2 in self.moves_p1) and 
                        (diag_2 in self.possible_next_coords() and 
                         diag_4 in self.possible_next_coords())) or\
                       ((row_2 in self.moves_p1 and col_2 in self.moves_p1) and 
                        (diag_1 in self.possible_next_coords() and 
                         diag_3 in self.possible_next_coords())) or\
                       ((row_2 in self.moves_p1 and col_1 in self.moves_p1) and 
                        (diag_2 in self.possible_next_coords() and 
                         diag_4 in self.possible_next_coords())):
                        return TippyGameState.LOSE
            return TippyGameState.DRAW

    def winner(self, player):
        ''' (TippyGameState, str) -> bool

        Return True iff the game is over and player has won.

        >>> t1 = TippyGameState('p1', board_length = 4, \
        moves_p1 = [(2, 2), (1, 2)], moves_p2 = [(3, 2), (4, 4)])
        >>> t2 = t1.apply_move(TippyMove((1, 1)))  # p1's move
        >>> t3 = t2.apply_move(TippyMove((3, 3)))  # p2's move
        >>> t4 = t3.apply_move(TippyMove((2, 3)))  # p1's move
        >>> t4.winner('p1')
        True

        Preconditions: player is either 'p1' or 'p2'
        '''
    
        if player == 'p1':
            for x in self.moves_p1:
                if 1 and self.board_length not in x:
                    row_1 = (x[0] + 1, x[1])
                    row_2 = (x[0] - 1, x[1])
                    col_1 = (x[0], x[1] + 1)
                    col_2 = (x[0], x[1] - 1)
                    diag_1 = (x[0] - 1, x[1] + 1)
                    diag_2 = (x[0] + 1, x[1] + 1)
                    diag_3 = (x[0] + 1, x[1] - 1)
                    diag_4 = (x[0] - 1, x[1] - 1)
                    if (row_1 in self.moves_p1 and col_1 in self.moves_p1) and\
                       (diag_1 in self.moves_p1 or diag_3 in self.moves_p1) or\
                       (row_1 in self.moves_p1 and col_2 in self.moves_p1) and\
                       (diag_2 in self.moves_p1 or diag_4 in self.moves_p1) or\
                       (row_2 in self.moves_p1 and col_2 in self.moves_p1) and\
                       (diag_1 in self.moves_p1 or diag_3 in self.moves_p1) or\
                       (row_2 in self.moves_p1 and col_1 in self.moves_p1) and\
                       (diag_2 in self.moves_p1 or diag_4 in self.moves_p1):
                        return True
        elif player == 'p2':
            for x in self.moves_p2:
                if 1 and self.board_length not in x:
                    row_1 = (x[0] + 1, x[1])
                    row_2 = (x[0] - 1, x[1])
                    col_1 = (x[0], x[1] + 1)
                    col_2 = (x[0], x[1] - 1)
                    diag_1 = (x[0] - 1, x[1] + 1)
                    diag_2 = (x[0] + 1, x[1] + 1)
                    diag_3 = (x[0] + 1, x[1] - 1)
                    diag_4 = (x[0] - 1, x[1] - 1)
                    if (row_1 in self.moves_p2 and col_1 in self.moves_p2) and\
                       (diag_1 in self.moves_p2 or diag_3 in self.moves_p2) or\
                       (row_1 in self.moves_p2 and col_2 in self.moves_p2) and\
                       (diag_2 in self.moves_p2 or diag_4 in self.moves_p2) or\
                       (row_2 in self.moves_p2 and col_2 in self.moves_p2) and\
                       (diag_1 in self.moves_p2 or diag_3 in self.moves_p2) or\
                       (row_2 in self.moves_p2 and col_1 in self.moves_p2) and\
                       (diag_2 in self.moves_p2 or diag_4 in self.moves_p2):
                        return True
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()