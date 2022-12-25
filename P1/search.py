# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    def getMoves(state_list):
        temp =[]
        for i in state_list:
            temp.append(i[1])
        return temp[1:]

    fringe = util.Stack()
    explored = set()
    fringe.push([(problem.getStartState(),[],0)])
    while not(fringe.isEmpty()):
        popped = fringe.pop()
        node_added_to_explored = popped[len(popped)-1]
        if(problem.isGoalState(node_added_to_explored[0])):
            return getMoves(popped)
        else:
            if(node_added_to_explored[0] not in explored):
                explored.add(node_added_to_explored[0])
                successors = problem.getSuccessors(node_added_to_explored[0])
                for i in successors:
                    list_temp = []
                    list_temp.extend(popped)
                    list_temp.append(i)
                    fringe.push(list_temp)





    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # "*** YOUR CODE HERE ***"

    def getMoves(state_list):
        temp =[]
        for i in state_list:
            temp.append(i[1])
        return temp[1:]
    def is_in_Fringe(node,fringe):
        for i in fringe.list:
            if(node==i[len(i)-1][0]):
                return True
        return False

    fringe = util.Queue()
    explored = set()
    fringe.push([(problem.getStartState(),[],0)])
    while not(fringe.isEmpty()):
        popped = fringe.pop()
        node_added_to_explored = popped[len(popped)-1]
        if (problem.isGoalState(node_added_to_explored[0])):
            return getMoves(popped)
        if(node_added_to_explored[0] not in explored):
            explored.add(node_added_to_explored[0])
            successors = problem.getSuccessors(node_added_to_explored[0])
            # print(successors)
            for i in successors:
                    if (not (is_in_Fringe(i[0], fringe)) and (i[0] not in explored)):
                        # if (problem.isGoalState(i[0])):
                        #     list_temp = []
                        #     list_temp.extend(popped)
                        #     list_temp.append(i)
                        #     return getMoves(list_temp)
                        # else:
                            list_temp = []
                            list_temp.extend(popped)
                            list_temp.append(i)
                            fringe.push(list_temp)
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    def getMoves(state_list):
        temp =[]
        for i in state_list:
            temp.append(i[1])
        return temp[1:]


    def updateFringe(node,path,fringe,priortiy):
        isExisted = False
        for i in fringe.heap: #each i is tuple (priortiy,counter,(path,priority))
            if(node[0]==i[2][0][len(i[2][0])-1]):
                isExisted=True
        if(not (isExisted)):
            fringe.push((path,priortiy),priortiy)
        else:
            for i in fringe.heap:  # each i is tuple (priortiy,counter,(path,priority))
                if (node[0] == i[2][0][len(i[2][0])-1]):
                    if (i[0] > priortiy):
                        y = list(i[2])
                        y[0] = path
                        y[1] = priortiy
                        new_tuple = (priortiy,i[1],tuple(y))
                        fringe.heap[fringe.heap.index(i)] = new_tuple



    fringe = util.PriorityQueue()
    explored = set()
    updateFringe((problem.getStartState(),[],0),[(problem.getStartState(),[],0)],fringe,0)
    #     # -------------------
    while not(fringe.isEmpty()):
        popped = fringe.pop()
        node_added_to_explored = popped[0][len(popped[0])-1]
        if (problem.isGoalState(node_added_to_explored[0])):
            return getMoves(popped[0])
        if(node_added_to_explored[0] not in explored):
            explored.add(node_added_to_explored[0])
            successors = problem.getSuccessors(node_added_to_explored[0])
            for i in successors:
                    if ((i[0] not in explored)):
                        list_temp = []
                        list_temp.extend(popped[0])
                        list_temp.append(i)
                        # fringe.push((list_temp,i[2]+popped[1]),i[2]+popped[1])
                        updateFringe(i, list_temp, fringe, i[2]+popped[1])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # print(problem.goal)
    # print("------------------------------")
    def getMoves(state_list):
        temp =[]
        for i in state_list:
            temp.append(i[1])
        return temp[1:]


    def updateFringe(node,path,fringe,priortiy,cost):
        isExisted = False
        for i in fringe.heap: #each i is tuple (priortiy,counter,(path,cost))
            if(node[0]==i[2][0][len(i[2][0])-1]):
                isExisted=True
        if(not (isExisted)):
            fringe.push((path,cost),priortiy)
        else:
            for i in fringe.heap:  # each i is tuple (priortiy,counter,(path,cost))
                if (node[0] == i[2][0][len(i[2][0])-1]):
                    if (i[0] > priortiy):
                        y = list(i[2])
                        y[0] = path
                        y[1] = cost
                        new_tuple = (priortiy,i[1],tuple(y))
                        fringe.heap[fringe.heap.index(i)] = new_tuple

    fringe = util.PriorityQueue()
    explored = set()
    updateFringe((problem.getStartState(), [], 0), [(problem.getStartState(), [], 0)], fringe, 0,0)
    while not(fringe.isEmpty()):
        popped = fringe.pop() # each item after popped : (path,cost)
        node_added_to_explored = popped[0][len(popped[0])-1]
        if (problem.isGoalState(node_added_to_explored[0])):
            return getMoves(popped[0])
        if(node_added_to_explored[0] not in explored):
            explored.add(node_added_to_explored[0])
            successors = problem.getSuccessors(node_added_to_explored[0])
            for i in successors:
                    if ((i[0] not in explored)):
                        list_temp = []
                        list_temp.extend(popped[0])
                        list_temp.append(i)
                        cost = i[2]+popped[1]
                        pr = cost+heuristic(i[0],problem)
                        updateFringe(i, list_temp, fringe, pr, cost)


def dls(problem,limit):
    def getMoves(state_list):
        temp =[]
        for i in state_list:
            temp.append(i[1])
        return temp[1:]

    fringe = util.Stack()
    explored = set()
    fringe.push([(problem.getStartState(),[],0)])
    while not(fringe.isEmpty()):
        popped = fringe.pop()
        node_added_to_explored = popped[len(popped)-1]
        if(problem.isGoalState(node_added_to_explored[0])):
            return (getMoves(popped),True)
        else:
            if(node_added_to_explored[0] not in explored):
                explored.add(node_added_to_explored[0])
                if((len(popped)-1)<=limit):
                    successors = problem.getSuccessors(node_added_to_explored[0])
                    for i in successors:
                        list_temp = []
                        list_temp.extend(popped)
                        list_temp.append(i)
                        fringe.push(list_temp)
    return ([],False)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
