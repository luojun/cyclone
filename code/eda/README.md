# Experential Digital Agent

Research on learning from experience where the agent-environment interaction is digital.

While the research is supposed to be generic, we are emphasizing applications to AI4Science, especially continual RL for science.

We will use weather prediction as the starting point.

## EDA Architecture: Toward Continual Control of Weather Prediction

The **EDA (Experiential Digital Agent)** is to be designed to control and adapt a weather prediction system (e.g., PanGu-Weather), called "weather predictor" for our purposes.

## Core Philosophy

Based on **"The Alberta Plan"** (Sutton et al.) and **"Welcome to the Era of Experience"** (Silver & Sutton), the system aims to move away from static, human-labeled datasets towards:

1.  **Continual Learning**: The agent learns from a continuous stream of experience (prediction vs. observation).
2.  **Agent-Environment Interaction**: The weather predictor and its continual adaptation is part of the agent's "world". Note that the real, physical world about which the weather predictor makes prediction is **not** part of the agent's world but rather the source of the reward signal.
3.  **Reward-Driven**: The discrepancy between the weather predictor and real-world weather measurements provides a reward signal guiding the EDA's policy.

### Architecture Components

#### 1. The Environment (World)
- **State ($S_t$)**: Current weather observation (e.g., ERA5 reanalysis snapshot, or live sensor data).
- **Action ($A_t$)**: Control parameters for the prediction model (e.g., model weights updates, prompt tuning if applicable, or ensemble weights).
- **Reward ($R_{t+1}$)**: Negative prediction error (e.g., $-MSE$) of the forecast made at time $t$ when verified at $t+k$.

#### 2. The Agent (EDA)
The agent consists of sub-modules inspired by the Alberta Plan:
- **Perception**: Encodes the weather predictor's state $S_t$.
- **Policy ($\pi$)**: Determines the best action $A_t$ to maximize reward as negative prediction error.
- **Value Function ($V$)**: Estimates the long-term expected accuracy.
- **Model ($M$)**: A learned internal model of how the *weather predictor* behaves.

### Implementation Strategy (RL4Science)

1.  **Baseline**: Run PanGu-Weather in inference mode.
2.  **Adaptation**:
    - **Short-term**: Adjust bias correction terms or ensemble weights based on recent error trends.
    - **Long-term**: Fine-tune the PanGu-Weather weights (or a lightweight adapter layer) using the accumulated "experience" stream.

### References
- **The Alberta Plan for AI Research**: Sutton, Bowling, Pilarski (2022).
- **Welcome to the Era of Experience**: Silver, Sutton (2024).
