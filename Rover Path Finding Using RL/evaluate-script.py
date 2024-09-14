from rover_env import RoverEnv
from dqn_agent import DQNAgent
import numpy as np
import matplotlib.pyplot as plt

# Initialize environment and agent
env = RoverEnv(size=10)
state_size = env.observation_space.shape[0]
action_size = env.action_space.n
agent = DQNAgent(state_size, action_size)

# Load the trained model
agent.load("rover_dqn.weights.h5")

# Evaluation parameters
episodes = 100

# Evaluation loop
scores = []
paths = []

for episode in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    done = False
    score = 0
    path = [state[0]]
    
    while not done:
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])
        score += reward
        state = next_state
        path.append(state[0])
    
    scores.append(score)
    paths.append(path)

# Visualize results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(scores)
plt.title('Scores over episodes')
plt.xlabel('Episode')
plt.ylabel('Score')

plt.subplot(1, 2, 2)
plt.imshow(env.terrain, cmap='terrain')
plt.colorbar(label='Terrain Difficulty')
for path in paths[-10:]:  # Plot last 10 paths
    path = np.array(path)
    plt.plot(path[:, 1], path[:, 0], 'r-', alpha=0.5)
plt.plot(env.start_pos[1], env.start_pos[0], 'go', label='Start')
plt.plot(env.goal_pos[1], env.goal_pos[0], 'bo', label='Goal')
plt.title('Rover Paths on Terrain')
plt.legend()

plt.tight_layout()
plt.savefig('evaluation_results.png')
plt.show()

print(f"Average score: {np.mean(scores):.2f}")
print(f"Standard deviation: {np.std(scores):.2f}")
