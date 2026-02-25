# Cyclone: an EDA for Weather as RL4Science Project

This project explores an RL4Science setup, by concretely using an **Experiential Digital Agent**, or **EDA**, to continually learn to control and adapt a weather prediction system, such as PanGu-Weather or any other NWP (Numerical Weather Prediction) system. 

## Goal

The fundamental goal is to chart a path for the broad use of continual reinforcement
learning -- an agent learning from its own experience -- in scientific research and
application.

## Direction

The guiding intuition is that wherever computational modeling is used for
simulation, prediction, and generation, many decisions will have been made and
continually adjusted by the researchers according to the ongoing and accumulating
experience informed by how good or bad the current version of the computational
modeling setup is doing. In other words, the iterative decision making by the
researchers about the specific setup of computational modeling is actually a
continual RL process, or a process of *researchers learning from experience*.

Consider weather prediction as an example. The temporal and spatial discretization,
choices and configurations of PDE solver, model architectures and deep learning
methods when neural networks are used, scheme and configurations of data reanalysis,
etc., all impact the prediction quality. We could then view prediction quality or
even just prediction accuracy as reward feedback for the researcher about how well
their modeling decisions are doing. This way, the continual improvement of NWP
through the researcher's effort might be viewed as a continual RL process.

If this conception its valid, it generalizes to other domains, to wherever numerical
and computational methods with or without deep learning components are used to
simulate, predict, generate or just "model" in science, engineering, and application
contexts, such as in building a digital twin of the tokamak machine for accurately 
simulating its magnetic field.

## RL Framing

### Environment

The **environment** here for the RL agent is primarily the computational modeling
setup rather than just the real world where weather phenomenon happens. More
accurately, *the computational modeling setup and the real world together form the environemnt*. Likewise, in the case of the digital twin of tokamak, it's the
simulator plus the physical device that affords real-world measurement together
that form the environment.

### Action

As to the RL interface, first and foremost, the action (A) here should
correspond to the normal decisions made by the researchers that change the actual
computational setup being used. Crucially, because the researchers do not affect the
real world that they are modeling or predicting about, their action primarily
affects the computational setup.

### Reward

Secondly, accuracy of the computational setup should be the reward. In other words,
even though the modeling setup may make a complex prediction along many dimensions,
the reward (R) should actually be a quality indicator at a higher-level. While
this could be counterintuitive from the perspective of supervised learning. From
an RL perspective, this could make perfect sense because what ultimately matters
for an RL agent is not where the fine-grained predictions went right or wrong, but
that the prediction performance should stay good over an extended period of time or
indefinitely into the future. The underlying principle here is also what is behind
today's practice of using RL to tune an LLM or an imitation policy for humanoid 
robots. But the principle does not presuppose a pre- vs. post-training distinction.

### Observation

Finally, observation (O) should cover the essential features of the computational
setup, especially those that could be affected by the action. This, again, should be
quite intutive, once we compare with how a research may view their models or 
modeling setup, because it is such setup that constitutes the main part, or at least
the controllable of the overall environment. Observation could also be about the real world that the computational setup is modeling. This is likely in the form of
the input into the computatoinal model to make prediction, but it could also take
the form the raw input into the whole pipeline before any data engineering or data
analysis even happens.

## Strategy

We use NWP as the test case to both motivate and guide the EDA research
Strategically, we chose not to develop EDA independently as a framework, but rather
focus on doing the weather prediction case well first. We will then factor out and
generalize the lessons learned for an EDA architecture.

However, we do not rule out the possibility that even early enough in the project,
we will already start to considering other meaningful cases, such as building digital twins for tokamak machines.

## Cyclone as a litmus test

Our project is code named "Cyclone" because deep learning models for weather
prediction trained with supervised learning (such as PanGu-Weather) could have 
difficulty with predicting future trajectory of a tropical cyclone. This
difficulty has sometimes been attributed to the choice of loss function.

Given what is said earlier about [reward](#reward), the EDA approach may help
to address the issue. There may be multiple concrete ways to address the issue,
from an RL perspective, with or without strictly falling under the EDA framework.
For now, we will just say that we will keep an eye on the cyclone trajectory
prediction case as a litmus test.

## Directory Structure

We adopt a simple project structure as follows:

- `docs/`: General project documentation, planning, and prompting history.
- `code/eda/`: Code and documentation related to the EDA architecture.
- `code/weather/`: Code and resources for the weather model integration.

The differentiation of `code/` is according to the agent-environment distinction
with agent in `code/eda` and environment in `code/weather`. What binds these
will be the RL interface. As the RL interface get figured out, we could also
consider adding `code/tokamak` etc.
