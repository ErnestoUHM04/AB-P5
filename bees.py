# Cornejo Morales Paola
# Hernándz Martínez Ernesto Ulises

# Usar el algoritmo de colonia de abejas para resolver el problema de la mochila que se asignó en la práctica 1.
# Recuerden utilizar los límites de las variables de acuerdo con problema, respetando los límites de 3 Love Potions y 2 Skiving Snackbox.
# Para el resto de productos los límites están entre (0,10).

import random

# Tamaño del enjambre = 40
beehive_size = 40
# abeja obreras = 20
worker_bees_count = beehive_size // 2
#print("Número de abejas obreras:", worker_bees_count)
# abejas Observadoras = 20
observer_bees_count = beehive_size // 2
#print("Número de abejas observadoras:", observer_bees_count)
# límite = 5
limit = 5
# iteraciones = 50
max_iterations = 50

# x1 = Decoy Detonators (0-10)  - 4 lb      - $ 10
#x1_lower_bound = 0
#x1_upper_bound = 10
# x2 = Love Potions (3-10)      - 2 lb      - $ 8
#x2_lower_bound = 3
#x2_upper_bound = 10
# x3 = Extendable Ears (0-10)   - 5 lb      - $ 12
#x3_lower_bound = 0
#x3_upper_bound = 10
# x4 = Skiving Snackbox (2-10)  - 5 lb      - $ 6
#x4_lower_bound = 2
#x4_upper_bound = 10
# x5 = Fever Fudge (0-10)       - 2 lb      - $ 3
#x5_lower_bound = 0
#x5_upper_bound = 10
# x6 = Puking Pastilles (0-10)  - 1.5 lb    - $ 2
#x6_lower_bound = 0
#x6_upper_bound = 10
# x7 = Nosebleed Nougat (0-10)  - 1 lb      - $ 2
#x7_lower_bound = 0
#x7_upper_bound = 10

def create_worker_bee(lower_bounds, upper_bounds):
    bee = []
    for i in range(n):
        r1 = random.random() # Número aleatorio entre 0 y 1
        xi = lower_bounds[i] + r1 * (upper_bounds[i] - lower_bounds[i])
        xi = round(xi) # Redondear al entero más cercano
        bee.append(xi)
    return bee

def create_worker_bees(lower_bounds, upper_bounds, values, weights):
    # Create worker bees
    worker_bees = []
    for i in range(worker_bees_count):
        worker_bee = create_worker_bee(lower_bounds, upper_bounds)
        fitness_value = fitness(worker_bee, values)
        weight_value = weight(worker_bee, weights)
        print("Worker Bee:", worker_bee, "\tValue:", fitness_value, "\tWeight:", weight_value)
        worker_bees.append((worker_bee, fitness_value, weight_value, 0)) # (bee, fitness, weight, limit_counter)
    return worker_bees

def create_observer_bee(acumulated_probabilities, worker_bees):
    # We select a worker bee based on the accumulated probabilities
    roullete_wheel_index = roullete_wheel(acumulated_probabilities)
    selected_bee = worker_bees[roullete_wheel_index][0]
    # Now that we have selected a bee, we can create a new observer bee based on it

    # Add the observer bee creation logic here

    return ((selected_bee, roullete_wheel_index)) # (value, index of the selected worker bee)

def roullete_wheel(acumulated_probabilities):
    r = random.random()
    for i, p in enumerate(acumulated_probabilities):
        if r <= p:
            return i
    return len(acumulated_probabilities) - 1

def fitness(bee, values):
    total_value = sum(bee[i] * values[i] for i in range(n))
    return total_value

def weight(bee, weights):
    total_weight = sum(bee[i] * weights[i] for i in range(n))
    return total_weight


n = 7 # Número de variables

lower_bounds = [0, 3, 0, 2, 0, 0, 0]
upper_bounds = [10, 10, 10, 10, 10, 10, 10]

values = [10, 8, 12, 6, 3, 2, 2]
weights = [4, 2, 5, 5, 2, 1.5, 1]

worker_bees = create_worker_bees(lower_bounds, upper_bounds, values, weights)

# We need them to work now :)


# After they finish working, we evaluate their fitness and create probabilities for observer bees
# Rember initialization of the limit counter for each worker bee

# After the worker bee, create observer bees based on the best solutions found by worker bees
sum_fitness = sum(bee[1] for bee in worker_bees)
probabilities = [bee[1] / sum_fitness for bee in worker_bees]
acumulated_probabilities = []
acum_sum = 0
for p in probabilities:
    acum_sum += p
    acumulated_probabilities.append(acum_sum)

# Create observer bees
observer_bees = []
for i in range(observer_bees_count):
    observer_bee = create_observer_bee(acumulated_probabilities, worker_bees)
    fitness_value = fitness(observer_bee, values)
    weight_value = weight(observer_bee, weights)
    print("Observer Bee:", observer_bee, "\tValue:", fitness_value, "\tWeight:", weight_value)
    observer_bees.append((observer_bee, fitness_value, weight_value))

# We select the best solution found by observer_bees via the waggle dance
