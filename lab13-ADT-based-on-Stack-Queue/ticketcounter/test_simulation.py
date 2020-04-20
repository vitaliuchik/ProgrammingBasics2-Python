import random
from simulation import TicketCounterSimulation


if __name__ == '__main__':
    simulator = TicketCounterSimulation(2, 25, 2, 3)
    random.seed(4500)
    simulator.run()
    simulator.printResults()