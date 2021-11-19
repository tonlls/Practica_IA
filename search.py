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

from node import Node
import util

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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    n = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return n.getTotalPath()

    fringe = util.Queue()
    fringe.push(n)
    generated = set()   

    while not fringe.isEmpty():
        n = fringe.pop()
        generated.add(n.state)  # Expanded

        for s, a, c in problem.expand(n.state):
            ns = Node(s, n, a, n.cost + c)
            if ns.state not in generated:  # Not in expanded and not in fringe
                if problem.isGoalState(ns.state):
                    return ns.getTotalPath()
                fringe.push(ns)
                generated.add(ns.state)  # Fringe

    print("No solution")


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    n = Node(problem.getStartState())
    if problem.isGoalState(problem.getStartState()):
        return n.total_path()

    fringe = util.PriorityQueue()
    generated = {}
    fringe.push(n, 0)
    generated[n.state] = ("F", 0)

    while not fringe.isEmpty():
        n = fringe.pop()
        if problem.isGoalState(n.state):
            return n.total_path()
        if generated[n.state][0] == "E":
            # Node has been expanded, continue
            continue
        generated[n.state] = ("E", n.cost)
        for s, a, c in problem.getSuccessors(n.state):
            ns = Node(s, n, a, n.cost + c)
            if ns.state not in generated:
                fringe.push(ns, ns.cost)
                generated[ns.state] = ("F", ns.cost)
            elif generated[ns.state][0] == "F" and generated[ns.state][1] > ns.cost:
                fringe.update(ns, ns.cost)
                generated[ns.state] = ("F", ns.cost)

    print("No solution")
    # sys.exit(-1)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
    
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    openList=[]
    closedList=[]
    openList.append(Node(problem.getStartState(),None,None,0,0))
    while len(openList)>0:
        currentNode=openList.pop(0)
        closedList.append(currentNode)
        if problem.isGoalState(currentNode.state):
            return currentNode.getTotalPath()
        if currentNode.state not in closedList:
            closedList.append(currentNode.state)
            for child in problem.expand(currentNode.state):
                childNode=Node(child[0],currentNode,child[1],currentNode.cost+child[2],heuristic(child[0],problem))
                if childNode.state not in closedList:
                    openList.append(childNode)
                    openList.sort(key=lambda x: x.cost+x.heuristic)
    print("No solution")
    # sys.exit(-1)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
