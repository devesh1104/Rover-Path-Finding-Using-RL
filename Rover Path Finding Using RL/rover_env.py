
import gym
import numpy as np
from gym import spaces

class RoverEnv(gym.Env):
    def __init__(self, size=10):
        super(RoverEnv, self).__init__()
        
        self.size = size
        self.observation_space = spaces.Box(low=0, high=size-1, shape=(2,), dtype=np.int32)
        self.action_space = spaces.Discrete(4)  # 0: Up, 1: Right, 2: Down, 3: Left
        
        # Generate random terrain
        self.terrain = np.random.rand(size, size)
        
        # Set start and goal positions
        self.start_pos = np.array([0, 0])
        self.goal_pos = np.array([size-1, size-1])
        
        self.current_pos = self.start_pos.copy()
        self.energy = 100.0
        
    def step(self, action):
        # Move the rover
        if action == 0:  # Up
            self.current_pos[0] = max(0, self.current_pos[0] - 1)
        elif action == 1:  # Right
            self.current_pos[1] = min(self.size - 1, self.current_pos[1] + 1)
        elif action == 2:  # Down
            self.current_pos[0] = min(self.size - 1, self.current_pos[0] + 1)
        elif action == 3:  # Left
            self.current_pos[1] = max(0, self.current_pos[1] - 1)
        
        # Calculate energy cost
        energy_cost = self.terrain[tuple(self.current_pos)] * 10
        self.energy -= energy_cost
        
        # Calculate reward
        distance_to_goal = np.linalg.norm(self.current_pos - self.goal_pos)
        reward = -distance_to_goal - energy_cost
        
        # Check if done
        done = np.array_equal(self.current_pos, self.goal_pos) or self.energy <= 0
        
        return self.current_pos, reward, done, {}
    
    def reset(self):
        self.current_pos = self.start_pos.copy()
        self.energy = 100.0
        return self.current_pos
    
    def render(self):
        # Implement visualization if needed
        pass
