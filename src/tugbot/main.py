import rclpy
from .tugbot_node import TugbotNode
from .rl import RL
import numpy as np
import random
from .ddpg import DDPG 
from .exploration_noise import GaussianNoise
import os

def main(args=None):
    rclpy.init(args=args)
    env = RL(TugbotNode())
    all_rewards = []
    num_episodes = 10000
    max_trajectory = 200000
    epsilon = 1
    max_epsilon = 1
    min_epsilon = 0.001
    exploration_decay_rate = 0.0001
    state_dim = env.state_dim
    action_dim = env.action_dim
    max_action = env.max_action
    min_action = env.min_action

    agent = DDPG(state_dim, action_dim)
    if os.path.exists("/home/anil/Desktop/Projects/ros2-bundle/actor.pth"):
        agent.load()
    noise_generator = GaussianNoise(action_dim,max_action,min_action)

    for episode in range(num_episodes):
        episode_total_reward = 0
        done = False
        state = env.reset()
        trajectory = 0
        while not done:
            if None in state:
                rclpy.spin_once(env.node)
                state = env.newState()
                continue
            action = agent.select_action(state)
            
            # epsilon greedy
            if random.uniform(0, 1) < epsilon:
                action = noise_generator.sample(action)
                
            next_state, reward, done = env.step(action)
            episode_total_reward += reward
            agent.replay_buffer.push((state, next_state, action, reward, float(done)))
            if trajectory > max_trajectory:
                done = True
            state = next_state
            trajectory += 1
        agent.update()
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-exploration_decay_rate*episode)
        print("Training: " + str(episode+1) + "/" + str(num_episodes) + " Episode Total Reward: " + str(episode_total_reward) + ". Epsilon: " +str(epsilon) + " Step: " + str(trajectory) + " Battery: " + str(state[13]))
        agent.save()

if __name__ == '__main__':
    main()
