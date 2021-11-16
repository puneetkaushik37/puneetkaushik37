#Author: Puneet Kaushik
#Version: 1.0
#Adding code for unit testing Python
#Author: Puneet Kaushik

import unittest
import WarGameSimulation
from WarGameSimulation import Player

class testPlayerClassFunction(unittest.TestCase):
    ## @test__PlayerName()
    ## Author: Puneet Kaushik
    ## Date: 16/11/2021
    ## This test case is to test name attribute of the class 
    def test__PlayerName(self):
        m_Player_one = Player("Puneet Kaushik")
        self.assertEqual(m_Player_one.name, 'Puneet Kaushik')
    
    
    ## @test_add_cards()
    ## Author: Puneet Kaushik
    ## Date: 16/11/2021
    ## This test case is to test add_cards() function of player class
    def test_add_cards(self):
        m_Player_one = Player("Puneet Kaushik")
        m_Player_one.add_cards(WarGameSimulation.Card("Hearts","Two"))
        m_allCards = m_Player_one.all_cards
        self.assertEqual(m_allCards[0].suit,"Hearts")
        self.assertEqual(m_allCards[0].rank,"Two")
        


def suite():
    suite = unittest.TestSuite()
    suite.addTest(testPlayerClassFunction('test__PlayerName'))
    suite.addTest(testPlayerClassFunction('test_add_cards'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
    