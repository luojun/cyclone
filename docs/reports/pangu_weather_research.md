# PanGu-Weather Research Report

## 1. Nature Paper (2023)
**Title:** "Accurate medium-range global weather forecasting with 3D neural networks"  
**Authors:** Bi, Kaifeng, et al. (Huawei Cloud)  
**Publication:** Nature, July 2023 (vol 619).  
**Key Findings:**
- First AI model to surpass traditional Numerical Weather Prediction (NWP) methods in accuracy for certain metrics.
- Uses a **3D Earth-Specific Transformer (3DEST)** architecture to process 3D meteorological data.
- 10,000x faster than NWP methods (inference in seconds vs. hours on supercomputers).
- Trained on 43 years of ERA5 reanalysis data.

## 2. Tropical Cyclones & Loss Function (Lingxi Xie Talk, Summer 2024)
- **Challenge:** Traditional Mean Squared Error (MSE) loss function tends to "smoothify" extreme events.
- **Impact:** While PanGu-Weather tracks cyclone paths well due to pressure minima, it often underestimates intensity (wind speed) because MSE penalizes large deviations less effectively for rare, sharp peaks compared to smooth fields.
- **Solution Attempts:** The team acknowledges the need for specialized loss functions or different training objectives to better capture extreme weather intensity, though MSE remains the primary driver for general field accuracy.

## 3. Open Source & Inference
- **Repository:** [`198808xc/Pangu-Weather`](https://github.com/198808xc/Pangu-Weather)
- **License:** BY-NC-SA 4.0 (Non-Commercial).
- **Models:** Pre-trained ONNX models available for 1h, 3h, 6h, and 24h lead times.
- **Hardware:** Inference runs efficiently on consumer GPUs (e.g., V100, or even smaller cards with optimization).

## 4. Usage in Europe (ECMWF)
- **Integration:** ECMWF has integrated PanGu-Weather into its experimental suite.
- **Performance:** Evaluation confirms "very promising" results, comparable to the Integrated Forecasting System (IFS).
- **Output:** 10-day global forecasts are now available on the [ECMWF charts website](https://charts.ecmwf.int/).
- **Validation:** Independent validation by ECMWF highlights the potential of AI models to complement traditional NWP.

## 5. Conclusion & Next Steps
PanGu-Weather represents a validated, state-of-the-art baseline for AI weather forecasting. Its open-source availability (weights) makes it a suitable candidate for the **RL4Science** project.
**Recommendation:** 
1. Use the pre-trained ONNX models for the initial environment.
2. Develop a wrapper (Coder Agent) to interface with the model.
3. Focus EDA efforts on control/adaptation strategies, possibly addressing the "smoothing" issue or domain shift.
