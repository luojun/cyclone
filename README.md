# Cyclone: an EDA for Weather as RL4Science Project

This project explores an RL4Science setup by using an **Experiential Digital Agent**
(**EDA**) to continually learn to control and adapt a weather prediction system,
such as PanGu-Weather or other NWP (Numerical Weather Prediction) systems.

## Goal

The fundamental goal is to chart a path for the broad use of continual
reinforcement learning—an agent learning from its own experience—in scientific
research and application.

## Direction

The guiding intuition is that wherever computational modeling is used for
simulation, prediction, and generation, researchers make and continually adjust
decisions about the computational setup based on how well the current setup is
doing. In other words, their iterative decision-making about the setup is a
continual RL process, or *researchers learning from experience*.

Consider weather prediction. Discretization, solver choice, model architecture,
data reanalysis scheme, etc., all impact prediction quality. We can view
prediction quality or accuracy as reward feedback on those decisions; continual
NWP improvement then looks like continual RL. If this conception is valid, it
generalizes to other domains—wherever numerical or computational methods (with or
without deep learning) are used to simulate, predict, or generate in science,
engineering, or application, e.g. a digital twin of a tokamak for simulating its
magnetic field.

## RL Framing

### Environment

The **environment** for the RL agent is primarily the computational modeling
setup, not just the real world (e.g. weather). More accurately, *the modeling
setup and the real world together form the environment*. Likewise for a tokamak
digital twin: the simulator plus the physical device and its measurements form the
environment.

### Action

The **action** (A) should correspond to researchers’ decisions that change
the computational or modeling setup. Because researchers as modellers typically
do not affect the real world that they model, their action primarily affects
the computational or modeling setup.

### Reward

**Reward** (R) should be the accuracy—or a high-level quality measure—of the
setup. Even if the setup produces complex, multi-dimensional predictions, reward
is a single quality signal. That may seem at odds with supervised learning, but
in RL what matters is sustained good performance over time, not fine-grained,
per-prediction correctness. This general principle could be seen as underlying
RL-tuning of LLMs and of humanoid imitation policies. Its generality does not
require a pre- vs. post-training distinction.

### Observation

**Observation** (O) should cover the essential features of the setup, especially
those affected by the action—the part of the environment the researcher
controls. It may also cover real-world state the setup models, e.g. inputs to
the computational model or raw pipeline inputs before data engineering or
analysis.

## Strategy

We use NWP as the test case to motivate and guide research on EDA towards RL4Science.
We chose not to develop EDA as a standalone framework first, but to do the weather
prediction case well, then factor out and generalize the lessons for an EDA
architecture. We may still take on other cases early (e.g. tokamak digital twins)
if they add value.

## Cyclone as a litmus test

The project is code-named "Cyclone" because supervised weather models (e.g.
PanGu-Weather) often struggle with tropical cyclone trajectory prediction,
sometimes attributed to the inadequacy of the loss function. Given the 
[reward](#reward) framing above, an EDA or other RL approach may help.
We will treat cyclone trajectory prediction as a litmus test.

## Directory Structure

- `docs/`: Project documentation, planning, and prompting history.
- `code/eda/`: Code and documentation related to the EDA architecture.
- `code/weather/`: Code and resources for the weather model integration.

The split follows the agent–environment distinction (agent in `code/eda`,
environment in `code/weather`). The concrete RL interface to be figured
out will bind them. We may add more case studies such as `code/tokamak`
along the way.
