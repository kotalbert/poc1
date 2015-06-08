"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    _houses = []
    _config = []
    _houses_num = 0
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._config = list(configuration)
        self._houses_num = len(configuration)
        
        tmp_houses = list(configuration)
        tmp_houses.reverse()
        
        #assigning houses in reverse order
        for house in tmp_houses:
            self._houses.append(house)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        if self._houses_num == 0:
            return "[0]"
        
        out_str = "["
        
        for indx in range(self._houses_num):
            if indx == 0:
                out_str = "[%d," %(self._houses[indx])
            elif indx != self._houses_num -1:
                out_str = "%s %d," %(out_str, self._houses[indx])
            else:
                out_str = "%s %d]" %(out_str, self._houses[indx])
            
        return out_str
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        try:
            return self._config[house_num]
        except:
            return -1
        
    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        return True

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        pass

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        return []
 


