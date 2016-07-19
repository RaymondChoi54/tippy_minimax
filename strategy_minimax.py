from strategy import Strategy
from tippy_game_state import TippyGameState
from tippy_move import TippyMove


class StrategyMinimax(Strategy):
    '''
    Interface to suggest a move that will lead to the best position for the
    current player.
    '''

    def suggest_move(self, state, status=False):
        ''' (StrategyRandom, GameState) -> Move

        Return the strongest move from those available for state.
        Overrides Strategy.suggest_move

        >>> t1 = TippyGameState('p1', board_length=3, moves_p1 = [(2, 2), \
        (2, 3), (3, 2), (3, 3)], moves_p2 = [(2, 1), (1, 2), (1, 3), (1, 1)])
        >>> s1 = StrategyMinimax()
        >>> s1.suggest_move(t1)
        TippyMove((3, 1))
        >>> t2 = TippyGameState('p1', board_length=3, moves_p1 = [(2, 2), \
        (2, 3), (3, 2)], moves_p2 = [(2, 1), (1, 2), (1, 1)])
        >>> s2 = StrategyMinimax()
        >>> s2.suggest_move(t2)
        TippyMove((1, 3))
        '''

        if state.over:
            return self.score(state)
        scores = []
        moves = []
        for move in state.possible_next_moves():
            possible_game = state.apply_move(move)
            scores.append(self.suggest_move(possible_game, status=True))
            moves.append(move)
        if state.next_player == 'p2' and status:
            max_score_index = scores.index(max(scores))
            best_move = moves[max_score_index]
            return scores[max_score_index]
        elif status:
            min_score_index = scores.index(min(scores))
            best_move = moves[min_score_index]
            return scores[min_score_index]
        elif state.next_player == 'p2' and not status:
            max_score_index = scores.index(max(scores))
            best_move = moves[max_score_index]
            return best_move
        else:
            min_score_index = scores.index(min(scores))
            best_move = moves[min_score_index]
            return best_move

    def score(self, state):
        ''' (StrategyRandom, GameState) -> int

        Return -1 if the winner is p1, 1 if the winner is p2, and 0 if it is
        a tie
        '''

        if state.winner('p1'):
            return -1
        elif state.winner('p2'):
            return 1
        else:
            return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
