"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable

import time

def update():
    for episode in range(50):
        print('# episode ', episode, '...')
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
    
# %%
# demonstrate final games until terminate manually
def end_test():
    while True:
        # initial observation
        observation = env2.reset()
        
        step = 0
        while True:
            # fresh env
            env2.render()
    
            # RL choose action based on observation
            action = RL.choose_action(str(observation))
    
            # RL take action and get next observation and reward
            observation_, reward, done = env2.step(action)
            time.sleep(0.1)
    
            # swap observation
            observation = observation_
    
            # break while loop when end of this episode
            if done:
                env2.render()
                if reward == 1:
                    print('# get oval in', step, 'steps!')
                elif reward == -1:
                    print('# die after', step, 'steps...')
                break
            
            step += 1
        
        time.sleep(2)

print('# unstopping demonstration starts...')
env2 = Maze(oval_location=4)
env2.after(100, end_test)
env2.mainloop()
