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


env = gym.make("highway-ice-v0", render_mode="rgb_array")
model = PPO.load("highway_ppo_150000_timesteps_model/model", env=env)
env = RecordVideo(env, video_folder="highway_ppo_150000_timesteps_model/videos", episode_trigger=lambda e: True)
env.unwrapped.set_record_video_wrapper(env)
env.configure({"simulation_frequency": 15})  # Higher FPS for rendering

for videos in range(4):
    done = truncated = False
    obs, info = env.reset()
    while not (done or truncated):
        # Predict
        action, _states = model.predict(obs, deterministic=True)
        # Get reward
        obs, reward, done, truncated, info = env.step(action)
        # Render
        env.render()
env.close()