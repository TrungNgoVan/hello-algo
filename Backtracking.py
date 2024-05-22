# Define Tree node 
from random import choices
from sre_parse import State
from tkinter import NO


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1: Given a binary tree, search and record all nodes with a value of 7, please return a list of nodes.
res = []

def pre_order_1(root: TreeNode) -> None:
    if root is None:
        return 
    if root.val == 7:
       res.append(root)
    
    pre_order_1(root.left)
    pre_order_1(root.right) 

# Example 2: In a binary tree, search for all nodes with a value of 7 and please 
# return the paths from the root node to these nodes.
res = []
path = []

def pre_order_2(root: TreeNode) -> None:
    if root is None:
        return
    path.append(root)
    # Attempt
    if root.val == 7:
        # Record solution
        res.append(list(path))
    pre_order_2(root.left)
    pre_order_2(root.right)
    # Retract
    path.pop()

# Example 3: In a binary tree, search for all nodes with a value of 7 and return 
# the paths from the root to these nodes, requiring that the paths do not contain nodes with a value of 3

res = []
path = []

def pre_order_3(root: TreeNode) -> None:
    # Pruning
    if root is None or root.val == 3:
        return
    # Attempt
    path.append(root)

    if root.val == 7:
        # Record solution
        res.append(list(path))
    pre_order_3(root.left)
    pre_order_3(root.right)
    # Retract
    path.pop()

#! Framework code
"""
def backtrack(state: State, choices: list[choice], res: list[state]):
    #! Check if it's a solution
    if is_solution(state):
        #! Record solution
        record_solution(state, res)
        #! Stop searching
        return
    #! Iterate through all choices
    for choice in choices:
        #! Pruning: Check if the choice is valid
        if is_valid(state, choice):
            #! Try: make a choice, update the state
            make_choice(state, choice)
            backtrack(state, choices, res)
            #! Retreat: Undo the choice, revert to the previous state
            undo_choice(state, choice)
"""

# Next, we solve Example 3 based on the framework code. The state is the node traversal path, 
# choices are the current node's left and right children, and the result res is the list of paths:

def is_solution(state: list[TreeNode]) -> bool:
    """Determine if the current state is a solution"""
    return state and state[-1].val == 7

def record_solution(state: list[TreeNode], res: list[list[TreeNode]]):
    """Record solution"""
    res.append(list(state))

def is_valid(state: list[TreeNode], choice: TreeNode) -> bool:
    """Determine if the choice is legal under the current state"""
    return choice is not None and choice.val != 3

def make_choice(state: list[TreeNode], choice: TreeNode):
    """Update state"""
    state.append(choice)

def undo_choice(state: list[TreeNode], choice: TreeNode): 
    """Restore state"""
    state.pop()

def backtrack(state: list[TreeNode], choices: list[TreeNode], res: list[list[TreeNode]]):
    if is_solution(state):
        record_solution(state, res)
    for choice in choices:
        if is_valid(state, choice):
            make_choice(state, choice)
            backtrack(state, [choice.left, choice.right], res)
            undo_choice(state, choice)
    

# Practice

# Problem 1: Full permutation problem: Given a set, find all possible permutations and combinations of it.
# Input: [1,2,3]
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

res: list[list[int]] = []
nums: list[int] = [1,2,3]

def permutation(state, choices, res=res):
    if len(state) == len(choices):
        res.append(list(state))

    for i in choices:
        if i not in state:
            state.append(i)
            permutation(state, choices, res)
            state.pop()

# Problem 2: n queens: Place n queens on an n chessboard so that they do not attack each other.
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

def solveNQueens(self, n: int) -> list[list[str]]:
            def is_not_under_attack(row, col):
                for prev_row in range(row):
                    # Check if the column is attacked
                    if col == positions[prev_row]:
                        return False
                    # Check if the major diagonal is attacked
                    if col - (row - prev_row) == positions[prev_row]:
                        return False
                    # Check if the minor diagonal is attacked
                    if col + (row - prev_row) == positions[prev_row]:
                        return False
                return True

            def place_queen(row):
                if row == n:
                    # Construct a board from the positions
                    board = []
                    for r in range(n):
                        line = ['.'] * n
                        line[positions[r]] = 'Q'
                        board.append(''.join(line))
                    solutions.append(board)
                    return
                
                for col in range(n):
                    if is_not_under_attack(row, col):
                        positions[row] = col
                        place_queen(row + 1)
                        # No need to remove the queen as we are going to overwrite positions[row] in the next iteration

            solutions = []
            positions = [-1] * n
            place_queen(0)
            return solutions
