import torch
import torch.nn as nn
import torch.nn.functional as F


class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=64, fc2_units=64):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)

        # define the network

        # add a fully connected layer with state_size as inputs and fc1_units as outputs
        self.fc1 = nn.Linear(state_size, fc1_units)

        # add a fully connected layer with fc1_units as inputs and fc2_units as outputs
        self.fc2 = nn.Linear(fc1_units, fc2_units)

        # add a fully connected layer with fc2_units as inputs and action_size as outputs
        self.fc3 = nn.Linear(fc2_units, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""

        # do a forward pass on the network

        # state (input) > fc1 layer > relu function > x (output)
        x = F.relu(self.fc1(state))

        # x (input) > fc2 layer > relu function > x (output)
        x = F.relu(self.fc2(x))

        # x (input) > fc3 layer > return
        return self.fc3(x)
