import random
import pickle
import kymnasium as kym


class RandomAgent(kym.Agent):
    ACTIONS = [0, 1, 2, 3]

    def act(self, obs, info):
        return random.choice(self.ACTIONS)

    def save(self, path):
        with open(path, mode='wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, path: str):
        with open(path, mode='rb') as f:
            return pickle.load(f)