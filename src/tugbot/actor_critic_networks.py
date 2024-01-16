import torch.nn as nn
import torch
import torch.nn.init as init
# takes in a state observation as input and outputs an action, which is a continuous value.
class Actor(nn.Module):

    def __init__(self, environment_states, action_dim, hidden):
        super(Actor, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(environment_states, hidden), 
            nn.Tanh(), 
            nn.Linear(hidden, hidden), 
            nn.Tanh(), 
            nn.Linear(hidden, hidden), 
            nn.Tanh(), 
            nn.Linear(hidden, action_dim)
        )
        # this is for weight randomity in init
        #for m in self.modules():
        #    if isinstance(m, nn.Linear):
        #        init.xavier_uniform_(m.weight)

    def forward(self, state):
        return self.net(state)
#  takes in both a state observation and an action as input and outputs a Q-value, which estimates the expected total reward for the current state-action pair. 
class Critic(nn.Module):

    def __init__(self, environment_states, action_dim, hidden):
        super(Critic, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(environment_states + action_dim, hidden), 
            nn.Tanh(), 
            nn.Linear(hidden, hidden), 
            nn.Tanh(), 
            nn.Linear(hidden, hidden), 
            nn.Tanh(), 
            nn.Linear(hidden, 1)
        )
        
    def forward(self, state, action):
        return self.net(torch.cat((state, action), 1))