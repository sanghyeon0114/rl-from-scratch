import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from agent import RandomAgent

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

agent = RandomAgent()
images = []

done = False
steps = 0

obs, info = env.reset()
images.append(env.render())

while not done and steps < 10:
    action = agent.act(obs, info)

    obs, reward, terminated, truncated, info = env.step(action)
    images.append(env.render())

    steps += 1
    done = terminated or truncated

############# print #############

fig, ax = plt.subplots(figsize=(5, 5))
ax.axis('off')
im = ax.imshow(images[0])

for i, image in enumerate(images):
    im.set_data(image)
    ax.set_title(f'step {i}')
    plt.pause(0.2)

plt.show()