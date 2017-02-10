"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random
import time
import sample_players
"""

class Tree(object):
    def __init__(parent,game,):



    def get_next_child():

    def get_parent():
"""

MAX_DEPTH = 25
class Timeout(Exception):
    """Subclass base exception for code clarity.
    
    As Timeout() exception trigger, we will return the best action could be.

    """
    
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    ----------
    float
        The heuristic value of the current game state to the specified player.
    """
    # Assuming the terminated State will be check in Iterative deepening serach
    # I can safely return only value only the node between root and terminted state node
    # First option for evaluation function: my_move - 1.3*my_opponent_move
    #return len(game.get_legal_move(player))-1.3*len(game.get_legal_moves(game.get_opponent(player)))
    # Second option for evaluation function: my_move - 1.5*my_opponent_move
    return len(game.get_legal_moves(player))-1.3*len(game.get_legal_moves(game.get_opponent(player)))
    #print (value)
    #return len(game.get_legal_moves(player))
    #return 1.
    #return value
    # Third option for evaluation function: my_move - 2*my_opponent_move
    #return len(game.get_legal_moves(player))-len(game.get_legal_moves(game.get_opponent(player)))

    #raise NotImplementedError


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    MAX_DEPTH = 1

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=5.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        ----------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        #raise NotImplementedError

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        
        #if not legal_moves:
            # Return immediately if there are no legal moves
        #    return (-1,-1)
        #elif game.move_count == 0:
        #    return (3,3)
            # Remove the reflected action
        # Use depth for iterative depeening
        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
            best_action = None
            depth = 0
            if (self.iterative):
                if (self.method == "minimax"):
                    # if Iterative Deepeening is true
                    while (True):
                        try:
                            depth = depth + 1
                            best_action = self.minimax(game, depth)[1]
                        except Timeout:
                            return best_action
                elif (self.method == "alphabeta"):
                    while (True):
                        try:
                            depth = depth + 1
                            best_action = self.alphabeta(game, depth)[1]
                        except Timeout:
                            return best_action

            else:
                # if Iterative deepeening is not set to use
                if (self.method == "minimax"):
                    #sprint("MiniMax")
                    best_action = self.minimax(game, 1)[1]
                elif (self.method == "alphabeta"):
                    best_action = self.alphabeta(game, 1)[1]
        except Timeout:
            # Handle any actions required at timeout, if necessary
            #pass
            #print("You are out of time. Your agent forfeits the game")
            return best_action
            
        return best_action

        # Return the best move from the last completed search iteration
        #raise NotImplementedError
    #def remove_refelection_move(self,game):

        """
        input: list of turple with all legal moves

        output: list of turple with all legal moves without allowing opponent to reflect
        """

    #def remove_reflection_position(self,game):

        """
        input: list of turple with all legal moves

        output: list of turple with all legal moves without reflection moves

        """

    #def remove_rotation_position(self,game):

        """
        input: list of turple with all legal moves

        output: list of turple with all legal move without rotation duplication moves
        """
        # Remove rotation 90

        # Remove rotation 180

        # Remove ratation 270
    
    #def sort_legal_moves():


    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        ----------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves
        """

        """
        Minimax algorithm implementation
        """

        
        
        if self.time_left() < (self.TIMER_THRESHOLD ):
            raise Timeout()  

        if(maximizing_player):
            try:
                list_move = game.get_legal_moves(game.active_player)
                if (depth == 0 or (not list_move)):
                    return (self.score(game,game.active_player), (-1, -1))

                best_max = float("-inf")
                action_max = None
                for action in list_move:
                    current_max = self.minimax(game.forecast_move(action),depth-1,False)[0]

                    if (best_max < current_max):    
                        best_max = current_max
                        action_max = action
                        #print(action_max)
            except Timeout:
                return (best_max,action_max)

            return (best_max,action_max)

        else:
            # Minimum selection layer
            try:
                list_move = game.get_legal_moves(game.active_player)
                best_min = float("inf")
                action_min = None

                if (depth == 0 or (not list_move)):
                    return (self.score(game,game.inactive_player), (-1, -1))

                for action in list_move:

                    current_min = self.minimax(game.forecast_move(action),depth-1,True)[0]
                    if(best_min > current_min):
                        best_min = current_min
                        action_min = action

            except Timeout:
                return (best_min,action_min)

            return (best_min,action_min)
        
        #raise NotImplementedError

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        ----------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves
        """
        #raise NotImplementedError

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        list_move = game.get_legal_moves(game.active_player)
        """
        AlphaBeta Implementation Starting

        alpha will be store the best possible score that max player can do

        beta will be store the best possible score that min player can do

        Algorithm Intuition:

        we break the loop whenever we ecounter alpha >= beta as max player would take 
        any less than alpha and min would take anything more than beta
        
        """

        if(maximizing_player):
            # Maximum selection layer
            action_max = None
            best_max = float("-inf")
            current_max = float("-inf")

            if (depth == 0 or (not list_move)):
                return (self.score(game,game.active_player), (-1, -1))

            for action in list_move:
                # copy game information indepth as we want to roll back later which
                # not affect the original state
                # Max action and current max value
                current_max = self.alphabeta(game.forecast_move(action),depth-1,alpha,beta,False)[0];
                #print(action)
                #print(current_max)
                if (best_max < current_max):
                    #print("Assigning Alpha")
                    best_max = current_max
                    action_max = action
                if (current_max >= beta):
                    #print("Break at max")
                    return (current_max,action)
                alpha = max(alpha, current_max)

            return (best_max,action_max)

        else:
            # Minimum selection layer
            #best_min = float("inf")
            action_min = None
            best_min = float("inf")
            current_min = float("inf")
            if (depth == 0 or (not list_move)):
                return (self.score(game,game.inactive_player), (-1, -1))

            for action in list_move:
                # The same as above loop
                current_min = self.alphabeta(game.forecast_move(action),depth-1,alpha,beta,True)[0]
                if(best_min > current_min):
                    #print("Assiging Beta")
                    best_min = current_min
                    action_min = action
                if (current_min <= alpha):
                    #print("Break at min")
                    return (current_min,action)
                beta = min(beta,current_min)
            return (best_min,action_min)

        #raise NotImplementedError
