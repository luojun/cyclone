import os
import numpy as np
import onnxruntime as ort

class PanGuInference:
    """
    Wrapper for running inference with the PanGu-Weather ONNX models.
    """
    def __init__(self, model_path, device='cpu'):
        """
        Initialize the PanGu-Weather inference session.

        Args:
            model_path (str): Path to the .onnx model file.
            device (str): Device to run inference on ('cpu' or 'cuda').
        """
        self.model_path = model_path
        self.device = device
        self.session = self._create_session()

        # Input shape expectations (Batch, Channels, Depth, Height, Width)
        # 13 pressure levels for upper-air variables (z, q, t, u, v)
        # Surface variables separate
        self.input_shape = (1, 5, 13, 721, 1440)

        self.predictor_observation_shape = (6,) # Observable aspects of predictor. 

    def _create_session(self):
        """Creates the ONNX Runtime session."""
        if not os.path.exists(self.model_path):
            print(f"Warning: Model file not found at {self.model_path}. Inference will fail.")
            return None

        providers = ['CPUExecutionProvider']
        if self.device == 'cuda':
            providers.insert(0, 'CUDAExecutionProvider')
        
        try:
            session = ort.InferenceSession(self.model_path, providers=providers)
            print(f"PanGu-Weather model loaded from {self.model_path} on {self.device}")
            return session
        except Exception as e:
            print(f"Error loading model: {e}")
            return None

    def predict(self, input_data):
        """
        Run inference on the input data.

        Args:
            input_data (np.ndarray): Input tensor matching model expectations.
                                     Shape: (1, 5, 13, 721, 1440) for upper air + surface inputs.

        Returns:
            np.ndarray: The model prediction.
        """
        if self.session is None:
            raise RuntimeError("Model session is not initialized.")

        # Note: Actual PanGu input handling is complex (surface + upper air).
        # This is a simplified interface for the EDA agent loop.
        
        input_name = self.session.get_inputs()[0].name
        output_name = self.session.get_outputs()[0].name
        
        # Ensure input data type is correct (usually float32)
        if input_data.dtype != np.float32:
            input_data = input_data.astype(np.float32)

        result = self.session.run([output_name], {input_name: input_data})
        return result[0]

    def dummy_input(self):
        """Generates a dummy input tensor for testing."""
        return np.random.randn(*self.input_shape).astype(np.float32)

    def weather_observation(self):
        """Generates a dummy observation tensor for testing."""
        return np.random.randn(*self.input_shape).astype(np.float32)

    def predictor_observation(self):
        """Generates a dummy prediction tensor for testing."""
        return np.random.randn(*self.input_shape).astype(np.float32)

if __name__ == "__main__":
    # Simple test
    print("Testing PanGuInference wrapper...")
    # Expects a model file to exist, strictly for testing logic flow
    dummy_path = "pangu_weather_24h.onnx"
    inference = PanGuInference(dummy_path)
    
    if inference.session is None:
        print("Skipping actual inference (no model file).")
    else:
        dummy = inference.dummy_input()
        print(f"Input shape: {dummy.shape}")
        try:
            output = inference.predict(dummy)
            print("Inference successful.")
            print(f"Output shape: {output.shape}")
        except Exception as e:
            print(f"Inference failed: {e}")
