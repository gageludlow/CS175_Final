# highway-env-ice

## The environment

### Highway

```python
env = gymnasium.make("highway-ice-v0")
```

In this task, the ego-vehicle is driving on a slippery multilane highway populated with other vehicles.
The agent's objective is to reach a high speed while avoiding collisions with neighbouring vehicles while also staying on the road. Driving on the right side of the road is also rewarded. There is and option to include a forward Progress reward.

<p align="center">
    <img src="https://github.com/gageludlow/ICS175_Final/assets/14191062/e25d07ef-1a3b-415f-8a83-457fee247b7e">
<br/>
    <em>The highway-ice-v0 environment.</em>
</p>


Uploading rl-video-episode-2.mp4…


## Installation

First start by cloning this repo.

To install this version of highway-env-ice you have to pip install the git repo.
`cd <root folder of project>`
Then run pip install on the project folder.
`pip install -e .`

This will install highway-env-ice, you may also need to pip install other dependencies like pygame, tensorboardx, and gymnasium. if a mac user you will most likely need to use xQuartz for the video recording libraries. This is an app that will need to be downloaded and installed. Windows users should not have an issue here and linux users can just run:

`pip install tensorboardx gym pyvirtualdisplay`


## Usage

```python
import gymnasium as gym

env = gym.make('highway-ice-v0', render_mode='rgb_array')

obs, info = env.reset()
done = truncated = False
while not (done or truncated):
    action = ... # Your agent code here
    obs, reward, done, truncated, info = env.step(action)
```

## Documentation

Read the [documentation online](https://farama-foundation.github.io/HighwayEnv/).

