import random
import time
from enum import Enum
from typing import List, Tuple, Optional

class CellType(Enum):
    EMPTY = 0
    OBSTACLE = 1
    GOAL = 2
    AGENT = 3
    COLLECTED = 4

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class ReflexAgent:
    def __init__(self, grid_size: Tuple[int, int], obstacle_density: float = 0.2):
        self.rows, self.cols = grid_size
        self.position = (0, 0)  # Starting position
        self.goals_collected = 0
        self.steps_taken = 0
        self.max_steps = 1000
        
        # Initialize grid
        self.grid = [[CellType.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]
        self._generate_environment(obstacle_density)
        
        # Place agent at starting position
        self.grid[self.position[0]][self.position[1]] = CellType.AGENT
    
    def _generate_environment(self, obstacle_density: float):
        """Generate random obstacles and goals in the environment"""
        total_cells = self.rows * self.cols
        num_obstacles = int(total_cells * obstacle_density)
        num_goals = max(3, int(total_cells * 0.05))  # 5% goals, minimum 3
        
        # Place obstacles randomly (avoid starting position)
        obstacles_placed = 0
        while obstacles_placed < num_obstacles:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) != self.position and self.grid[row][col] == CellType.EMPTY:
                self.grid[row][col] = CellType.OBSTACLE
                obstacles_placed += 1
        
        # Place goals randomly (avoid starting position and obstacles)
        goals_placed = 0
        while goals_placed < num_goals:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) != self.position and self.grid[row][col] == CellType.EMPTY:
                self.grid[row][col] = CellType.GOAL
                goals_placed += 1
    
    def _get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions"""
        row, col = pos
        neighbors = []
        
        for direction in Direction:
            dr, dc = direction.value
            new_row, new_col = row + dr, col + dc
            
            # Check if position is within bounds
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def _perceive_environment(self) -> dict:
        """Perceive the current environment around the agent"""
        perception = {
            'current_cell': self.grid[self.position[0]][self.position[1]],
            'neighbors': {},
            'goals_visible': [],
            'obstacles_nearby': False
        }
        
        # Check immediate neighbors
        for neighbor_pos in self._get_neighbors(self.position):
            row, col = neighbor_pos
            cell_type = self.grid[row][col]
            perception['neighbors'][neighbor_pos] = cell_type
            
            if cell_type == CellType.OBSTACLE:
                perception['obstacles_nearby'] = True
            elif cell_type == CellType.GOAL:
                perception['goals_visible'].append(neighbor_pos)
        
        return perception
    
    def _decide_action(self, perception: dict) -> Optional[Tuple[int, int]]:
        """Simple reflex agent decision making"""
        current_pos = self.position
        
        # Rule 1: If there's a goal adjacent, move to it
        if perception['goals_visible']:
            return perception['goals_visible'][0]  # Move to first visible goal
        
        # Rule 2: If current cell is a goal, collect it (stay in place)
        if perception['current_cell'] == CellType.GOAL:
            return current_pos
        
        # Rule 3: Move to a safe adjacent cell (avoid obstacles)
        safe_moves = []
        for neighbor_pos, cell_type in perception['neighbors'].items():
            if cell_type != CellType.OBSTACLE:
                safe_moves.append(neighbor_pos)
        
        # Rule 4: If no safe moves, stay in place
        if not safe_moves:
            return current_pos
        
        # Rule 5: Prefer moves that don't go backwards or to visited cells
        # For simplicity, we'll just choose randomly from safe moves
        return random.choice(safe_moves)
    
    def _execute_action(self, new_position: Tuple[int, int]) -> bool:
        """Execute the chosen action"""
        old_pos = self.position
        
        # Check if it's a valid move
        if new_position not in self._get_neighbors(old_pos) and new_position != old_pos:
            return False
        
        # Check if moving to an obstacle
        if (new_position != old_pos and 
            self.grid[new_position[0]][new_position[1]] == CellType.OBSTACLE):
            return False
        
        # Perform the action
        if new_position == old_pos:
            # Staying in place - check if collecting a goal
            if self.grid[old_pos[0]][old_pos[1]] == CellType.GOAL:
                self.grid[old_pos[0]][old_pos[1]] = CellType.COLLECTED
                self.goals_collected += 1
                print(f"Goal collected! Total goals: {self.goals_collected}")
        else:
            # Moving to new position
            if self.grid[new_position[0]][new_position[1]] == CellType.GOAL:
                self.goals_collected += 1
                print(f"Goal collected! Total goals: {self.goals_collected}")
                self.grid[new_position[0]][new_position[1]] = CellType.COLLECTED
            
            # Update grid
            if self.grid[old_pos[0]][old_pos[1]] == CellType.AGENT:
                self.grid[old_pos[0]][old_pos[1]] = CellType.EMPTY
            self.grid[new_position[0]][new_position[1]] = CellType.AGENT
            self.position = new_position
        
        self.steps_taken += 1
        return True
    
    def print_grid(self):
        """Print the current state of the grid"""
        symbols = {
            CellType.EMPTY: '.',
            CellType.OBSTACLE: '#',
            CellType.GOAL: 'G',
            CellType.AGENT: 'A',
            CellType.COLLECTED: 'X'
        }
        
        print(f"\nStep {self.steps_taken} - Goals collected: {self.goals_collected}")
        print("+" + "-" * (self.cols * 2 - 1) + "+")
        
        for row in self.grid:
            print("|" + " ".join(symbols[cell] for cell in row) + "|")
        
        print("+" + "-" * (self.cols * 2 - 1) + "+")
        print("Legend: A=Agent, G=Goal, #=Obstacle, X=Collected, .=Empty")
    
    def run_simulation(self, max_steps: Optional[int] = None, delay: float = 0.5, verbose: bool = True):
        """Run the agent simulation"""
        if max_steps:
            self.max_steps = max_steps
        
        print(f"Starting simulation with {self.rows}x{self.cols} grid")
        print(f"Agent starting at position {self.position}")
        
        if verbose:
            self.print_grid()
        
        while self.steps_taken < self.max_steps:
            # Perceive environment
            perception = self._perceive_environment()
            
            # Decide on action
            action = self._decide_action(perception)
            
            if action is None:
                print("No valid action available!")
                break
            
            # Execute action
            success = self._execute_action(action)
            
            if not success:
                print("Action execution failed!")
                break
            
            if verbose:
                self.print_grid()
                time.sleep(delay)
            
            # Check if all goals are collected
            remaining_goals = sum(row.count(CellType.GOAL) for row in self.grid)
            if remaining_goals == 0:
                print(f"\nAll goals collected in {self.steps_taken} steps!")
                break
        
        print(f"\nSimulation ended:")
        print(f"Steps taken: {self.steps_taken}")
        print(f"Goals collected: {self.goals_collected}")
        print(f"Final position: {self.position}")

# Example usage and demonstration
if __name__ == "__main__":
    # Create and run a simple simulation
    print("=== Simple Reflex Agent Demo ===")
    
    # Create agent with a 8x8 grid and 20% obstacle density
    agent = ReflexAgent(grid_size=(8, 8), obstacle_density=0.15)
    
    # Run simulation
    agent.run_simulation(max_steps=50, delay=1.0, verbose=True)
    
    print("\n" + "="*50)
    print("=== Running a faster simulation ===")
    
    # Create another agent for a faster demo
    agent2 = ReflexAgent(grid_size=(6, 6), obstacle_density=0.1)
    agent2.run_simulation(max_steps=30, delay=0.3, verbose=True)