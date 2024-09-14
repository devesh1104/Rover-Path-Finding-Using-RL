from rover_env import RoverEnv
from dqn_agent import DQNAgent
import numpy as np
from tqdm import tqdm

# Initialize environment and agent
env = RoverEnv(size=10)
state_size = env.observation_space.shape[0]
action_size = env.action_space.n
agent = DQNAgent(state_size, action_size)

# Training parameters
episodes = 100
batch_size = 32

# Training loop
for episode in tqdm(range(episodes)):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    
    for time in range(500):  # max 500 steps per episode
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        
        if done:
            print(f"Episode: {episode+1}/{episodes}, Score: {time}, Epsilon: {agent.epsilon:.2}")
            break
    
    if len(agent.memory) > batch_size:
        agent.replay(batch_size)

# Save the trained model
agent.save("rover_dqn.weights.h5")
