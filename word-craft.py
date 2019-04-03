import json
import argparse
import random
import string
from colorama import init, Fore, Back, Style

# Player class
from player import Player


def display_rules():
    """
    Prints the rules for the game.
    :return: Nothing.
    """
    with open("word-craft-rules.txt") as f:
        rules = f.read()
        print(Fore.GREEN + rules)


def save_player_score(player_name, score):
    """
    Saves the player's score to a text file score board.
    :return: Nothing.
    """
    print(Fore.GREEN + "Saving score...")
    print(Style.RESET_ALL)
    # TODO: Save player name and score to a "high score" text file.
    print("Thanks for playing! Quitting game...")
    exit()


def end_of_game(scenario, score, player):
    """
    Plays the end of game scenario based on whether the player quit or lost.
    :return:
    """

    if scenario == 'quit':
        print(Fore.RED + "Quitting game. Your final score was %s. " % str(score))
        print(Style.RESET_ALL)
        print("Would you like to save your score? y/n")
        while True:
            save_score = input()
            if save_score == 'y':
                save_player_score(player, score)
                exit()
            elif save_score == 'n':
                print("Thanks for playing! Quitting game...")
                exit()
    elif scenario == 'loss':
        print(Fore.RED + "You have gained 3 strikes. GAME OVER.")
        print(Style.RESET_ALL)
        print("Would you like to save your score? y/n")
        while True:
            save_score = input()
            if save_score == 'y':
                save_player_score(player, score)
                return
            elif save_score == 'n':
                print("Thanks for playing! Quitting game...")
                exit()


def check_new_word(word, gen_letter, player_obj):
    """
     Checks the word entered in the following order:
        1. Does the word start with the gen_letter?
        2. Is it a real word?
        3. Has it already been added to the player's list?
        If the word passes all these checks, add it to the player's word_list.
     :param word: Word that needs checking.
     :param gen_letter: The generated letter for the game.
     :param player_obj: The list of words that have already been checked and added.
     :return: Nothing
    """

    # Using PyDictionary to create a english dictionary to check for words.

    if word[0] == gen_letter:
        print("%s starts with %s" % (word, gen_letter))
        if word in dictionary:
            print('%s is a word' % word)
            if word not in player_obj.word_list:
                print("%s is not already in you list of words." % word)
                print(Fore.GREEN + "WORD IS VALID!!")
                player_obj.word_list.append(word)
            else:
                print(Fore.RED + "%s is already in your list. Adding strike" % word)
                print(Style.RESET_ALL)
                striker = player_obj.add_strike()
                # If player has reached 3 strikes.
                if striker is True:
                    end_of_game('loss', player_obj.score, player_obj.player_name)
        else:
            print(Fore.RED + "%s is not a word. Adding strike" % word)
            print(Style.RESET_ALL)
            striker = player_obj.add_strike()
            # If player has reached 3 strikes.
            if striker is True:
                end_of_game('loss', player_obj.score, player_obj.player_name)
    else:
        print(Fore.RED + "%s does not start with %s. Adding strike" % (word, gen_letter))
        print(Style.RESET_ALL)
        striker = player_obj.add_strike()
        # If player has reached 3 strikes.
        if striker is True:
            end_of_game('loss', player_obj.score, player_obj.player_name)


def new_game():
    ####################
    # Welcome to game ##
    ####################

    # Read in logo and print.
    with open("word-craft-logo.txt") as f:
        logo = f.read()
        print(logo)

    # Intro.
    print("Please enter a player name: ")
    print(Fore.RED + "Type 'quit' to quit the game.")
    print(Style.RESET_ALL)
    name = input()

    if name == 'quit':
        print(Fore.RED + "Quitting game...")
        print(Style.RESET_ALL)
        exit()

    player_obj = Player(name)

    # Generate a random letter.
    letters = string.ascii_letters.lower()
    gen_letter = random.choice(letters)

    print("Your letter is %s." % gen_letter)

    # Enter word-giving loop.
    while True:
        print(Fore.RED + "------Type 'q' to quit the game.------")
        print(Style.RESET_ALL)
        print("Enter a word beginning with %s: " % gen_letter)
        print(Fore.BLUE + "Score: %s" % str(player_obj.score))
        print(Style.RESET_ALL)
        given_word = input()
        given_word = given_word.lower()

        if given_word == 'q'.lower():
            end_of_game('quit', player_obj.score, player_obj.player_name)
            exit()
        else:
            check_new_word(given_word, gen_letter, player_obj)


if __name__ == '__main__':

    init()  # initializing colorama module.

    ####################
    # Dictionary      ##
    ####################
    dictionary = json.load(open("collection.json"))


    ####################
    # Argparse        ##
    ####################
    parser = argparse.ArgumentParser()
    # Group will make sure that only one of the arguments in the mutually exclusive group is present on CL.
    group = parser.add_mutually_exclusive_group()

    # Adding optional arguments.
    # 'store-true' - Action used for storing True. Makes checking the arguments parsed work for optional args.
    group.add_argument("-r", "--rules", help="Display the rules for the game.", action="store_true")
    group.add_argument("-n", "--newGame", help="Start a new game.", action="store_true")

    # Parsing arguments.
    args = parser.parse_args()

    # Checking arguments:
    if args.rules:
        display_rules()
    elif args.newGame:
        new_game()


