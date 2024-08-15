import random

class choices:
	rock = 'rock'
	paper = 'paper'
	scissors = 'scissors'
	
	
class agent:
    score = 0
    plays = ["rock", "rock", "paper", "paper", "scissors", "scissors"]
    answers = [0,0,0,0,0,0] #which plays are correct


def win_condition_RPS (action_agent1, action_agent2): #from the perspective of agent1
    if action_agent1 == action_agent2:
            return 0 #draw
    elif (action_agent1 == choices.paper and action_agent2 == choices.rock) or (action_agent1 == choices.rock and action_agent2 == choices.scissors) or (action_agent1 == choices.scissors and action_agent2 == choices.paper):
            return 1 #agent1 wins
    elif (action_agent1 == choices.rock and action_agent2 == choices.paper) or (action_agent1 == choices.scissors and action_agent2 == choices.rock) or (action_agent1 == choices.paper and action_agent2 == choices.scissors):
            return -1 #agent1 loses
    

def choose_action ():
    action = random.choice([choices.rock, choices.paper, choices.scissors])
    return action

def print_plays (play1, play2):
    print("Agent 1 played: ", play1)
    print("Agent 2 played: ", play2)    

def play_RPS (agent1, agent2, iteration):
    action_agent1 = newPlay(agent1.answers[iteration], agent1.plays[iteration]) 
    agent1.plays.append(action_agent1)
    print_plays(action_agent1, agent2.plays[iteration])
    result = win_condition_RPS(action_agent1, agent2.plays[iteration])
    agent1.score += result
    print("Agent 1 score: ", agent1.score)
    return result


def multiple_plays (agent1, agent2, n):
    for i in range(n):
            play_RPS(agent1, agent2, i)
    print("Agent 1 plays: ", agent1.plays)
        
def newPlay(answer, play):
    if answer == 1 :
          return play
    else :
        return choose_action()


agent1 = agent()
agent2 = agent()
multiple_plays(agent1, agent2, 6)

""" 

Pasos del juego

1. 

 """