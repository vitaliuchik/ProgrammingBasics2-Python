# Implementation of the main simulation class.
from arrays import Array
from llistqueue import Queue
from people import TicketAgent, Passenger
import random

class TicketCounterSimulation :
    # Create a simulation object.
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
    # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array( numAgents )
        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run( self ):
        for curTime in range(self._numMinutes + 1) :
            self._handleArrival( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )

    # Print the simulation results.
    def printResults( self ):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %
        len(self._passengerQ) )
        print( "The average wait time was %4.2f minutes." % avgWait )

    def _handleArrival(self, curTime):
        prob = random.random()
        if prob <= self._arriveProb:
            self._numPassengers += 1
            passenger = Passenger(self._numPassengers, curTime)
            self._passengerQ.enqueue(passenger)
            print(("Time %6d Passenger %d arrived.") % (curTime, passenger.idNum()))

    def _handleBeginService(self, curTime):
        for i in range(len(self._theAgents)):
            if not self._passengerQ.isEmpty() and self._theAgents[i].isFree():
                passenger = self._passengerQ.dequeue()
                print(passenger)
                endTime = curTime + self._serviceTime
                self._theAgents[i].startService(passenger, endTime)
                self._totalWaitTime += (curTime - passenger.timeArrived())
                print(("Time %6d Agent %d started serving passenger %d") % (curTime, self._theAgents[i].idNum(), passenger.idNum()))
                break

    def _handleEndService(self, curTime):
        for i in range(len(self._theAgents)):
            if self._theAgents[i].isFinished(curTime):
                passenger = self._theAgents[i].stopService()
                print(("Time %6d Agent %d stopped serving passenger %d") % (curTime, self._theAgents[i].idNum(), passenger.idNum()))
                break
