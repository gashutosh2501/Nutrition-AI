from abc import ABC,abstractmethod

class BaseAgent(ABC):

    @abstractmethod
    def observe(self):
        pass

    @abstractmethod
    def think(self,observation):
        pass

    @abstractmethod
    def act(self,decision):
        pass

    def run(self):
        observation=self.observe()
        decision=self.think(observation)
        result=self.act(decision)

        return result
