# highway-env

[![build](https://github.com/eleurent/highway-env/workflows/build/badge.svg)](https://github.com/eleurent/highway-env/actions?query=workflow%3Abuild)
[![Documentation Status](https://github.com/Farama-Foundation/HighwayEnv/actions/workflows/build-docs-dev.yml/badge.svg)](https://farama-foundation.github.io/HighwayEnv/)
[![Downloads](https://img.shields.io/pypi/dm/highway-env)](https://pypi.org/project/highway-env/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/63847d9328f64fce9c137b03fcafcc27)](https://app.codacy.com/manual/eleurent/highway-env?utm_source=github.com&utm_medium=referral&utm_content=eleurent/highway-env&utm_campaign=Badge_Grade_Dashboard)
[![GitHub contributors](https://img.shields.io/github/contributors/eleurent/highway-env)](https://github.com/eleurent/highway-env/graphs/contributors)


A collection of environments for *autonomous driving* and tactical decision-making tasks, maintained by [Edouard Leurent](https://github.com/eleurent)

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/highway-env.gif?raw=true"><br/>
    <em>An episode of one of the environments available in highway-env.</em>
</p>

## [Try it on Google Colab! ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](scripts)

## The environments

### Highway

```python
env = gymnasium.make("highway-ice-v0")
```

In this task, the ego-vehicle is driving on a slippery multilane highway populated with other vehicles.
The agent's objective is to reach a high speed while avoiding collisions with neighbouring vehicles while also staying on the road. Driving on the right side of the road is also rewarded. There is and option to include a forward Progress reward.

<p align="center">
    <img src="https://raw.githubusercontent.com/eleurent/highway-env/master/../gh-media/docs/media/highway.gif?raw=true"><br/>
    <em>The highway-ice-v0 environment.</em>
</p>

## Installation

To install this version of highway-env-ice you have to pip install the git folder.
`cd <root folder of project>`
Then run pip install on the project folder.
`pip install -e .`

This will install highway-env-ice, you may also need to pip install other dependencies like pygame, tensorboardx, and gymnasium. if a mac user you will most likely need to use xQuartz for the video recording libraries. This is an app that will need to be downloaded and installed. Windows users should not have an issue here and linux users can just run:

'pip install tensorboardx gym pyvirtualdisplay'


## Usage

```python
import gymnasium as gym

env = gym.make('highway-ice-v0', render_mode='rgb')

obs, info = env.reset()
done = truncated = False
while not (done or truncated):
    action = ... # Your agent code here
    obs, reward, done, truncated, info = env.step(action)
```

## Documentation

Read the [documentation online](https://farama-foundation.github.io/HighwayEnv/).

