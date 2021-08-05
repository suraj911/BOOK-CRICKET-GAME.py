# THIS IS A BOOK CRICKET GAME. THE ONE WHICH WE USED TO PLAY IN SCHOOL IN FREE TIME :)  .
# THIS IS A 2 PLAYER GAME.
# Rules of this game is assumed from  https://www.traditionalgames.in/book-cricket.

# There is a class named as Player having a constructor and Player has name, wickets_available, score, wickets_taken_till_now,
# and limit_of_score(which inhibit any player to play in infinite manner) and ball_taken_till_now data member.

# Class Player also has a member function which calculate the score of a player.
# There is a range_of_score variable which is equal to length of book which  gives the page number under that range.
# We are using a python built-in library 'random' which helps us to generate a random number in a specific range.

# INPUT SEQUENCE:
#       1) THE NUMBER OF BATSMEN
#       2) LIMIT OF SCORE
#       3) LENGTH OF BOOK
#       4) NAME OF PLAYER 1
#       5) NAME OF PLAYER 2

# SAMPLE TEST CASE:
#  2
#  1000
#  500
#  abc
#  def
# ========
# 11
# 700
# 200
# VFA
# VSA
# =======
# 11
# 700
# 600
# SF
# FSD



#=====================================================================================================================================
import random

class Player:

    def __init__(self, name, wickets_available,limit_of_score, score, wickets_taken_till_now,ball_taken_till_now, range_of_score):
        self.name = name
        self.wickets_available =  wickets_available         # No of batsmen = wickets available
        self.score = score
        self.wickets_taken_till_now = wickets_taken_till_now
        self.limit_of_score = limit_of_score
        self.ball_taken_till_now = ball_taken_till_now
        self.range = range_of_score


    def score_cal(self):
        while self.wickets_taken_till_now < self.wickets_available :
            self.ball_taken_till_now += 1
            n = random.randint(0,self.range)
            if n % 2 != 0:
                continue
            elif n % 2 == 0:
                if n % 10 == 0:
                    self.wickets_taken_till_now += 1
                self.score += n % 10
            if self.score > self.limit_of_score or self.wickets_taken_till_now > self.wickets_available:
                break
        return self.score

#=====================================================================================================================================

def main():
    print('Enter number of batsmen : ')
    no_of_batsmen = int(input())
    print('Enter limit of score : ')
    limit_of_score = int(input())
    print('Enter number of pages in book : ')
    length_of_book = int(input())
    print('Enter name of Player 1: ')
    pla1 = Player(input(), no_of_batsmen, limit_of_score, 0, 0, 0, length_of_book)
    print('Enter name of Player 2: ')
    pla2 = Player(input(), no_of_batsmen, limit_of_score, 0, 0, 0, length_of_book)

    batting = random.randint(0, 3)
    if batting == 1:
        m = pla1.score_cal()
        x = pla2.score_cal()
    else:
        x = pla2.score_cal()
        m = pla1.score_cal()

    if m > x:
        print('Winner is ' + pla1.name + ' and winning score is ' + str(pla1.score) + ' scored using ' + str(pla1.ball_taken_till_now) + " balls !")
    elif(x > m):
        print('Winner is ' + pla2.name + ' and winning score is ' + str(pla2.score) + ' scored using ' + str(pla2.ball_taken_till_now) + " balls !")
    else:
        print('Nobody wins, Match Draws')

#=====================================================================================================================================

if __name__ == '__main__':
    main()