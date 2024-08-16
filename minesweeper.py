import random

class Choices:
	rock = "rock"
	paper = "paper"
	scissors = "scissors"
	
class Agent:
    def __init__(self, score = 0, plays = None, answers = None):
        if plays is None:
            plays = [random.choice([Choices.rock, Choices.paper, Choices.scissors]) for _ in range(6)]
        if answers is None:
            answers = [random.randint(0, 1) for _ in range(6)]
        
        self.score = score
        self.plays = plays
        self.answers = answers

# Basados en el punto del agente 1
def win_condition_RPS (action_agent1, action_agent2):
    if action_agent1 == action_agent2:
        return 0 #draw
    elif (action_agent1 == Choices.paper and action_agent2 == Choices.rock) or \
         (action_agent1 == Choices.rock and action_agent2 == Choices.scissors) or \
         (action_agent1 == Choices.scissors and action_agent2 == Choices.paper):
        return 1 #agent1 gana
    else:
        return -1 #agent1 pierde
    
def choose_action ():
    return random.choice([Choices.rock, Choices.paper, Choices.scissors])

def play_RPS (agent1, agent2, iteration):
    action_agent1 = new_play(agent1.answers[iteration], agent1.plays[iteration]) 
    result = win_condition_RPS(action_agent1, agent2.plays[iteration])
    agent1.plays[iteration] = action_agent1
    agent1.score += result
    agent1.answers[iteration] = update_answer(result)
    return result

def multiple_plays (agent1, agent2, n):
    agent1.score = 0 #reseteamos el score para que no se acumule
    for i in range(n):
            play_RPS(agent1, agent2, i)
        
def new_play(answer, play):
    if answer == 1:
          return play
    else:
        return choose_action()
    
def update_answer(win):
    return 1 if win == 1 else 0
              
# Se mezclan los padres con mejor puntaje para crear a un hijo
# de puntajes mas grandes
def crossover(parent1, parent2): 
    child_agent = Agent()
    for i in range(6):
        child_agent.answers[i] = parent1.answers[i] if random.random() < 0.5 else parent2.answers[i] 

    return child_agent

def mutation(child, mutation_rate):
    for i in range(len(child.answers)):
        if (random.random()) < mutation_rate: #Creo que el calculo para la ejecutar la mutación esta raro
            child.answers[i] = random.randint(0, 1) #aqui estamos haciendo que mute la respuesta y provoca que crea que una respuesta es correcta cuando no
    return child
     
def evolve_population(population, generations, mutation_rate):
    for gen in range(generations):
        # Ordena a la poblacion en base al score de mayor a menor
        population = order_population_max(population)
        next_gen = []

        # Seleccion - Primera mitad de la poblacion
        top_half = population[ : len(population) // 2]

        # Crossover & Mutacion
        for i in range(len(population)):
            parent1 = random.choice(top_half)
            parent2 = random.choice(top_half)
            child = crossover(parent1, parent2)
            child = mutation(child, mutation_rate)
            next_gen.append(child)

        population = next_gen

        #creamos al agente NO inteligente al que se debera ganarle
        dumb_agent = Agent(plays=["rock", "rock", "rock", "rock", "rock", "rock"], answers=[0, 0, 0, 0, 0, 0])

        # Simula juegos para poder cambiar el score obtenido
        for agent in population:
            multiple_plays(random.choice(population), dumb_agent, 6)

        # Ordena a la poblacion en base al score de mayor a menor pero solo para mostrar el mejor agente
        print(f"Gen {gen+1} terminada: El mejor Agente obtuvo: {order_population_max(population)[0].score}")

    return population

def order_population_max(population):
    return sorted(population, key=lambda x: x.score, reverse=True)

def clear_score(population):
    for agent in population:
        agent.score = 0
    return population

# Creamos un arreglo de agentes para nuestra poblacion
population = [Agent() for _ in range(10)]
generations = 10
mutation_rate = 0.1

# Iniciamos el proceso de evolucion
evolved_population = evolve_population(population, generations, mutation_rate)

# Muestra las decisiones mas optimas del top 3 agentes
print("\nTop 3 Agentes resultantes de la evolucion:")
for idx, agent in enumerate(order_population_max(evolved_population)[:3]):
    print(f"Agente {idx+1}: Respuestas: {agent.answers} | Puntaje: {agent.score}")
    print(f"Jugadas: {agent.plays}\n")
