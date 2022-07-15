# Value-Based Methods > Report

[image1]: images/rewards_episodes.png "Score vs Episodes"
[image2]: images/pseudocode.png "pseudocode"
[image3]: images/abbreviations.png "abbreviations"

## Aproach
First i wanted to run this repo locally (on my mac 2021). Therefore i needed to update the pytorch version (it wasn't available when creating the conda environment). I've also added the 'gym' and 'box2d'

Next step was to create an agent that only took left turns. This helped me to get an idea of the action space and controlling the agent. I noticed that 'env.close()' closes the UnityEnvironment and that i couldnt restart if i re-run the jupyter cell. So let's not close the UnityEnvironment when were experimenting.

Now it was time to setup my own Deep Q-Network. 
- I've copied my code ('dqn_agent.py' & 'model.py') into the p1_navigation folder.
- I've instantiated an agent and obiously i had to alter the state-space-size & action-space-size to the specifications of the new environment.
- I've copied my code (dqn function) into the notebook to start training the agent.
- I've coppied the 'random' agent code and replaced the 'random' part with actions from our agent

## Learning Algorithm
For the sollution i chose to use the DQN learning algorithm. This is basically a Q-learning algoritm which utilizes deep-learning techniques.

### Q-learning
The basic idea of Q-learning is to learn the which action is most stuitable for a state. It's roughly speaking a mapping (Q-table) of every possible state and every possible action. The values in this Q-table represent the rewards of each state-action combination. The algorithm uses the Q-table as a lookup, which action yields the highest reward for any given state.

The 'Q-learning' algoritm is trained as follows:
* Initialize an empty Q-table
* It runs for a certain amount of episodes
* At each episode:
    * Update epsilon
    * Get the current (initial) state
    * Set the timestep to 0 
    * Loop over the timesteps
    * At each timestep:
        * Choose an action (based on a greedy policy which get updated every episode with a smaller epsilon)
        * Take the action and get the reward and the next state
        * Update the Q-table for the current state & action 

Here is the pseudocode with the corresponing abbreviations
![pseudocode][image2]
![abbreviations][image3]

### Deep-learning
The deep-learning network comes in to place because we don't have a single input state anymore, but a continuous state space of 37 dimensions. Now it becomes much harder to map that high dimensional input space to the action space. This is where deep-learning networks shines. 

I've created the following network:
- layer 1: input == state size, output == 64, fully connected, relu activation 
- layer 2: input == layer 1 output, output == 64, fully connected, relu activation 
- layer 3: input == layer 2 output, output == action size, fully connected
- adam optimizer

This network replaces the "linear" Q-table with a Q-network suitable for the continuous space.

## Plot of Rewards
![Score vs Episodes][image1]

## Experiments
- i've experimented with the early stopping functionality, stopping when the scoring consolidates. But it averages out at about 16.5
- i've experimented with epsilon decay functionality. in order to increase a little bit faster.

## Results
- **Training**: The agent reached the early_stopping threshold of 16.5 in 816 epsiodes
- **Inferencing**: Here is the result after training the agent: [youtube](https://youtu.be/MCE3GVhhu2U)

## Ideas for Future Work
- try different DL architectures. i've now trained on a fairly simple one. but i expect that different architectures with for example convolutions could also increase the scoring
- perform a grid search (combined with different DL-architectures) in order to find the optimal hyperparameters (i.e. gamma, tau, learning rate)
- experiment with dueling DQN's and Double DQN's
