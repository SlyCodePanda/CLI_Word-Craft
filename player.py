"""
File holds the Player class definition.
"""


class Player(object):

    def __init__(self, name):
        self.player_name = name
        self.word_list = []
        self.score = 0
        self.strikes = 0

    def add_word(self, word):
        """
        Adds passed word to the player's word list and increases score by 1.
        :param word: string to add to word_list
        :return: Nothing.
        """

        self.word_list.append(word)
        self.score += 1

    def add_strike(self):
        """
        Adds a strike to the player's strike counter.
        :return: True if player has reached 3 strikes, False otherwise.
        """

        self.strikes += 1

        if self.strikes == 3:
            return True
        else:
            return False

    def calc_score(self, gen_letter):
        """
        Calculates the score based on the number of words in the word_list.
        If gen_letter is one of the special letters (X, Z, U, Y, W) the final score gets a certain multiplier.
        :return: The final score.
        """

        # Add up score.
        for each in self.word_list:
            self.score += 1

        # Add multiplier if necessary.
        if gen_letter == 'Z':
            self.score = self.score * 4

        elif gen_letter == 'X':
            self.score = self.score * 4

        elif gen_letter == 'U':
            self.score = self.score * 2

        elif gen_letter == 'Y':
            self.score = self.score * 2

        elif gen_letter == 'W':
            self.score = self.score * 2

        return self.score

