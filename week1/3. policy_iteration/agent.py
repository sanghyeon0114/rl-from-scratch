import kymnasium as kym

class Agent(kym.Agent):
    def act(self, observation, info):
        pass

    def save(self, path):
        pass

    @classmethod
    def load(cls, path: str):
        pass