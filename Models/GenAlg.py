from abc import ABC, abstractmethod


class GenAlg(ABC):

    def __init__(self, frameskip, isLeftPlayer, obsIsImage):
        assert(frameskip > 0)
        self.frameskip = frameskip
        self.isLeftPlayer = isLeftPlayer
        self.obsIsImage = obsIsImage

    @abstractmethod
    def get_action(self, X):
        pass

    def predict(self, X):
        raise NotImplementedError()

    def train(self, min_tsteps):
        raise NotImplementedError()

    def save(self, save_dir):
        raise NotImplementedError()

    def load(self, save_path):
        raise NotImplementedError()