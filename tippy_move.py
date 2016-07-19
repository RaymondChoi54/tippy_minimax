from move import Move


class TippyMove(Move):
    ''' A move in the game of Tippy.
    '''

    def __init__(self, coord):
        ''' (TippyMove, int) -> NoneType

        Initialize a new TippyMove for playing on square coord on the board.

        Assume: coord is a tuple with two integers.
        '''

        self.coord = tuple(coord)

    def __repr__(self):
        ''' (TippyMove) -> str

        Return a string representation of this TippyMove.

        >>> m1 = TippyMove((2, 2))
        >>> m1
        TippyMove((2, 2))
        '''

        return 'TippyMove({})'.format(str(self.coord))

    def __str__(self):
        ''' (TippyMove) -> str

        Return a string representation of this TippyMove
        that is suitable for users to read.

        >>> m1 = TippyMove((2, 2))
        >>> print(m1)
        Move placed on coordinate (2, 2)
        '''

        return 'Move placed on coordinate {}'.format(str(self.coord))

    def __eq__(self, other):
        ''' (TippyMove, TippyMove) -> bool

        Return True iff this TippyMovee is the same as other.

        >>> m1 = TippyMove((2, 2))
        >>> m2 = TippyMove((2, 2))
        >>> print(m1 == m2)
        True
        '''

        return (isinstance(other, TippyMove) and self.coord == other.coord)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
