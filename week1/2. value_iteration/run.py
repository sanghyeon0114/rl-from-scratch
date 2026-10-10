import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from agent import RandomAgent

# 8x8
CUSTOM_MAP = [
    "SFFFFFFH",
    "FFHFFFFF",
    "FFFHFFFF",
    "FFFFFHFF",
    "FFFHFFFF",
    "FHHFFFHF",
    "FHFFHFHF",
    "FFFHFFFG",
]
CUSTOM_MAP = np.array(CUSTOM_MAP, dtype='c')

env = gym.make(
    id='FrozenLake-v1',
    render_mode='rgb_array',
    desc=CUSTOM_MAP,
    is_slippery=False,
)