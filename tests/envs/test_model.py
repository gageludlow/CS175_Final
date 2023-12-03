import gymnasium as gym
from gymnasium.wrappers import RecordVideo
import torch as th
from stable_baselines3 import PPO
from stable_baselines3 import DQN
from torch.distributions import Categorical
import torch
import torch.nn as nn
import numpy as np
from torch.nn import functional as F
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor
from stable_baselines3.common.vec_env import SubprocVecEnv

test_ppo = True
test_dqn = False

if(test_ppo):

    model = PPO.load("highway_ppo/model")
    env = gym.make("highway-ice-v0", render_mode="rgb_array")
    for _ in range(5):
        obs, info = env.reset()
        done = truncated = False
        while not (done or truncated):
            action, _ = model.predict(obs)
            obs, reward, done, truncated, info = env.step(action)
            env.render()

elif(test_dqn):

    model = DQN.load("highway_dqn/model")
    env = gym.make("highway-fast-v0", render_mode="rgb_array")
    for _ in range(5):
        obs, info = env.reset()
        done = truncated = False
        while not (done or truncated):
            action, _ = model.predict(obs)
            obs, reward, done, truncated, info = env.step(action)
            env.render()


# show tensorboard for model command = tensorboard --logdir "highway_dqn"
# change highway_dqn to folder containing training logs for the current model you'd like to display
#tensorboard --logdir "highway_ppo_150000_timesteps_model"
