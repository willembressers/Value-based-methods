[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135602-b0335606-7d12-11e8-8689-dd1cf9fa11a9.gif "Trained Agents"
[image2]: https://user-images.githubusercontent.com/10624937/42386929-76f671f0-8106-11e8-9376-f17da2ae852e.png "Kernel"

# Value-Based Methods

![Trained Agents][image1]

This repository contains material related to Udacity's Value-based Methods course.

## Project Details
The goal of this project is to train an reinforcement learning agent that will play a game. The goal of the game is to walk around in a 3D environment and pickup the 'yellow' bananas (and ignore the 'blue' bananas).

The game's state space consists of a continuous state space of 37 dimensions.

The actions space (possible actions to take) of the player is:
- move left
- move right
- move forward
- move backward

The game is considered solved when; the agent gets an average score of +13 over 100 consecutive episodes.

## Getting Started

1. First you'll need to download the unity environment.
- Linux: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip
- Mac OSX: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip
- Windows (32-bit): https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip
- Windows (64-bit): https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip
and put the file in the 'p1_navigation' folder

To set up your python environment to run the code in this repository, follow the instructions below.

2. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
	
3. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.
```bash
git clone https://github.com/willembressers/Value-based-methods.git
cd Value-based-methods/python
pip install .
```

4. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `drlnd` environment.  
```bash
python -m ipykernel install --user --name drlnd --display-name "drlnd"
```

## Instructions

1. Start the notebook
```bash
cd ..
jupyter notebook
```

2. Before running code in a notebook, change the kernel to match the `drlnd` environment by using the drop-down `Kernel` menu. 

![Kernel][image2]


3. Now you can 'run all' cell's, which will train the agent, and once trained it will play the game (once).

## Want to learn more?

<p align="center">Come learn with us in the <a href="https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893">Deep Reinforcement Learning Nanodegree</a> program at Udacity!</p>

<p align="center"><a href="https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893">
 <img width="503" height="133" src="https://user-images.githubusercontent.com/10624937/42135812-1829637e-7d16-11e8-9aa1-88056f23f51e.png"></a>
</p>
