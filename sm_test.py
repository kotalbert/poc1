""" 
Testing the Solitaire Mancala implementation

"""
import sm

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = sm.SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    # add more tests here


test_mancala()





# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())