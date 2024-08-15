import random

class plays:
	rock = 'rock'
	paper = 'paper'
	scissors = 'scissors'


class agent:
        score = 0
        plays = []


def win_condition_RPS (action_agent1, action_agent2): #from the perspective of agent1
        if action_agent1 == action_agent2:
                return 0 #draw
        elif (action_agent1 == plays.paper and action_agent2 == plays.rock) or (action_agent1 == plays.rock and action_agent2 == plays.scissors) or (action_agent1 == plays.scissors and action_agent2 == plays.paper):
                return 1 #agent1 wins
        elif (action_agent1 == plays.rock and action_agent2 == plays.paper) or (action_agent1 == plays.scissors and action_agent2 == plays.rock) or (action_agent1 == plays.paper and action_agent2 == plays.scissors):
                return -1 #agent1 loses
    

def choose_action ():
        action = random.choice([plays.rock, plays.paper, plays.scissors])
        return action

def print_plays (play1, play2):
        print("Agent 1 played: ", play1)
        print("Agent 2 played: ", play2)    

def play_RPS (agent1, agent2):
        action_agent1 = choose_action()
        action_agent2 = choose_action()
        agent1.plays.append(action_agent1)
        agent2.plays.append(action_agent2)
        print_plays(action_agent1, action_agent2)
        result = win_condition_RPS(action_agent1, action_agent2)
        agent1.score += result
        print("Agent 1 score: ", agent1.score)
        return result


def multiple_plays (agent1, agent2, n):
        for i in range(n):
                play_RPS(agent1, agent2)
        print("Agent 1 plays: ", agent1.plays)
        

agent1 = agent()
agent2 = agent()

multiple_plays(agent1, agent2, 6)