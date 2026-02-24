# Cyclone: EDA + Weather Project

This project aims to integrate PanGu-Weather (or similar AI weather models) into an RL4Science setup, using an "EDA" (Experiential Digital Agent) architecture to continually control and adapt the weather prediction system.

## Goal

The fundamental goal is to chart a path for the broad use of continual reinforcement learning in scientific research and application.

## Direction

The guiding intuition is that wherever computational modeling is used for simulation, prediction, and generation, many decisions will have been made and continually adjusted by the researchers according to the ongoing and accumulating experience informed by how good or bad the new version of the computational modeling setup is doing. In other words, the iterative decision making by the researchers about the specific setup of computational modeling is actually a continual RL process.

Concretely, the quality of simulation, prediction or generation
by the computation modeling setup could be viewed as the reward
signal associated with the decisions about the computational setup.

Take weather prediction as an example, temporal and spatial discretization, choices and configurations of PDE solver, model architectures and deep learning methods if neural networks are used, setup of data reanalysis, etc., all impact the prediction quality. If we view prediction quality or even just accuracy as reward, then such a reward signal is feedback on all these modeling decisions. This is how we may view the continual improvement of numerical weather prediction in general as a continual RL process.

And this point generalizes to other domains, to wherever numerical methods with or without deep learning components are used to simulate, predict, generate or just "model" in scientific, engineering, and application contexts.

## RL Framing

Thus, the environment here for the RL agent is primarily the computational modeling setup rather than just the real world where weather phenomenon happens. Or, more accurately, the computational modeling setup and the real world together for the environemnt.

As to the RL interface, first and foremost, the action (A) here should correspond to the normal decisions made by the researchers that impact the actual computational setup used. Crucially, because the researchers do not affect the real world they are modeling or predicting about, their action primarily affects the computational setup.

Secondly, accuracy of the computational setup should be the reward. In other words, even though the modeling setup may make a complex prediction along many dimensions, what the reward (R) should be is actually a higher level quality summary. This might be counter intuitive, but from an RL perspective this could make perfect sense because what matters about RL is that the prediction performance over extended period of time or indefinitely into the horizon stays good, rather than fine-grained momemntary correctness.

Finally, observation (O) might still include observation of the real world as it were, here likely in the form of the input into the computatoinal model, and ultimately in the form the raw input into the whole pipeline before any data engineering or data analysis happens. It is probably more important to note that the observation should also include the essential features of the computational modeling setup itself. This, again, should be quite intutive, once we compare with how a research may view their models or modeling setup.

## Strategy

[CONT] 

Use weather prediction as the test case to motivate and guide
the RL method research.

We do not independently develop EDA, but rather focus on doing the weather prediction case well first. We will then factor out and generalize lessons we learn for an EDA architecture.

## Hypothesis on a key test case: Cyclone

RL at the meta level could address it.

## Directory Structure

- `docs/`: General project documentation, planning, and prompting history.
- `code/eda/`: Code and documentation related to the EDA architecture.
- `code/weather/`: Code and resources for the weather model integration.
