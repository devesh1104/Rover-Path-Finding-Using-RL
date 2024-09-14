# Terrain-Based Rover Path Planning using Reinforcement Learning

## Project Overview

This project implements a reinforcement learning model to optimize path planning for a lunar or Martian rover, considering terrain features and energy constraints. The simulation is built in Unity using a height map created in Blender, and the learning process is facilitated by Unity's ML-Agents toolkit.

### Key Features

- Custom Unity environment simulating planetary terrain
- Reinforcement learning agent (rover) trained using PPO algorithm
- Integration of Blender-created height maps for realistic terrain
- Energy constraint simulation for the rover
- Visualization tools for training progress and results

## Table of Contents

1. [Installation](#installation)
2. [Project Structure](#project-structure)
3. [Usage](#usage)
4. [Training Process](#training-process)
5. [Evaluation](#evaluation)
6. [Customization](#customization)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/rover-path-planning.git
   cd rover-path-planning
   ```

2. Install Unity Hub and Unity (version 2020.3 LTS or later)

3. Install Python dependencies:
   ```
   pip install mlagents numpy matplotlib
   ```

4. Open the Unity project located in the `UnityProject` folder

5. Install ML-Agents in Unity:
   - Window > Package Manager
   - Click "+" > Add package from git URL
   - Enter: `com.unity.ml-agents`

## Project Structure

```
rover-path-planning/
├── UnityProject/
│   ├── Assets/
│   │   ├── Scripts/
│   │   │   └── RoverAgent.cs
│   │   ├── Scenes/
│   │   │   └── TrainingScene.unity
│   │   └── Terrain/
│   │       └── HeightMap.asset
│   └── ...
├── TrainingConfig/
│   └── rover_config.yaml
├── Results/
│   └── ...
├── Scripts/
│   ├── check_tensorflow.py
│   └── visualize_results.py
├── README.md
└── LICENSE
```

## Usage

1. Open the Unity project
2. Load the `TrainingScene` from the `Assets/Scenes` folder
3. Press Play to run the simulation in manual mode
4. To start training:
   - Open a terminal in the project root
   - Run: `mlagents-learn TrainingConfig/rover_config.yaml --run-id=RoverTraining1`
   - Press Play in the Unity Editor

## Training Process

The rover is trained using the Proximal Policy Optimization (PPO) algorithm. The training process involves the following steps:

1. The rover observes its current state (position, rotation, velocity)
2. It takes an action (move, rotate)
3. It receives a reward based on its proximity to the goal and energy usage
4. The process repeats until the rover reaches the goal or depletes its energy

Training hyperparameters can be adjusted in the `rover_config.yaml` file.

## Evaluation

After training, you can evaluate the model's performance:

1. In Unity, change the Behavior Type of the Behavior Parameters component to "Inference"
2. Drag the trained model file (`.onnx`) from the `Results` folder to the Model field
3. Press Play to observe the trained rover's behavior

To visualize training results:

```
python Scripts/visualize_results.py
```

This will generate a plot of the cumulative reward over time.

## Customization

- Terrain: Replace the height map in `UnityProject/Assets/Terrain/HeightMap.asset` with your own Blender-created terrain
- Rover Properties: Adjust the rover's physical properties in Unity Inspector
- Training Parameters: Modify `TrainingConfig/rover_config.yaml` to experiment with different learning settings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
