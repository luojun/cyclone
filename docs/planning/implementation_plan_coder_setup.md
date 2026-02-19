# Implementation Plan - Coder Agent (RL4Science Setup)

## Goal Description
Implement the technical infrastructure to support the EDA agent's interaction with the PanGu-Weather model. This involves setting up a Python environment (potentially Google Colab or local container) that can run the inference model and computing the reward signal (prediction error).

## User Review Required
> [!IMPORTANT]
> - Confirm preference for **Google Colab** vs. **Local/Server Execution**.
> - Review the proposed directory structure for the code.

## Proposed Changes

### 1. Environment Setup
#### [NEW] [weather/requirements.txt](file:///home/jun/Play/sea/weather/requirements.txt)
Dependencies for running PanGu-Weather (ONNX Runtime, PyTorch, etc.).

### 2. Inference Wrapper
#### [NEW] [weather/inference.py](file:///home/jun/Play/sea/weather/inference.py)
A Python class `PanGuInference` that:
- Loads the ONNX model.
- Accepts input tensor (weather state).
- Returns output tensor (forecast).

### 3. RL/EDA Loop
#### [NEW] [eda/agent.py](file:///home/jun/Play/sea/eda/agent.py)
A simple agent class that:
- Observes the error.
- (Placeholder) Updates internal state or logs performance.

## Verification Plan
1.  **Unit Test**: Run `weather/inference.py` with dummy data to verify model loading and execution.
2.  **Integration Test**: Run a single step of the `eda/agent.py` loop.
