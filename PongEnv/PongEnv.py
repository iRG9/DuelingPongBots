import pygame
import random
import numpy as np
import gym
from gym import spaces

from pongGame import *

CANVAS_WIDTH = 256
CANVAS_HEIGHT = 256
AGENT_ACT_SPACE = 3

class PongEnv(gym.Env):
    def __init__(self):
        super(PongEnv, self).__init__()

        # Initialize pygame
        pygame.init()

        # Create game window
        self.game = Game(CANVAS_WIDTH, CANVAS_HEIGHT)

        self.board_state = None # Will get set when render() is called

        self.action_space = spaces.Tuple([spaces.Discrete(AGENT_ACT_SPACE),spaces.Discrete(AGENT_ACT_SPACE)])
        self.observation_space = spaces.Box(low=0, high=1, shape=(CANVAS_WIDTH,CANVAS_HEIGHT), dtype=np.float32)

    def reset(self):
        self.game.reset()
        self.board_state = self.game.getScreenGrayscale()
        return self.board_state

    def step(self, action_vec):
        assert self.action_space.contains(action_vec)
        assert len(action_vec) == 2
        timestep_info = self.game.step(action_vec[0], action_vec[1])
        reward = (timestep_info['leftPlayerRew'], timestep_info['rightPlayerRew'])
        done = timestep_info['done']
        self.board_state = self.game.getScreenGrayscale()
        info = self.game.getExtraInfo()
        return self.board_state, reward, done, info

    def seed(self, seed):
        self.seed = seed
        random.seed(seed)

    def render(self):
        self.game.render()

    def close(self):
        pass


if __name__ == "__main__":
    print("Making env")
    env = PongEnv()
    print("Resetting env")
    env.reset()

    while True:
        print("Stepping")
        print("Ball velocity", env.game.Ball.velocityX, env.game.Ball.velocityY)
        obs, rew, done, info = env.step((1, 2))
        env.render()
        if done:
            break