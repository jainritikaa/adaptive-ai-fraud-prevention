# Adaptive AI Fraud Prevention System

## Overview

The **Adaptive AI Fraud Prevention System** is an AI-powered solution designed to detect and prevent fraud across the insurance lifecycle. It combines machine learning, graph analysis, document forgery detection, and federated learning to offer scalable and robust fraud detection and prevention capabilities.

## Features

- **Dynamic Fraud Detection**: Uses machine learning models (XGBoost, LightGBM, Autoencoders) for anomaly detection and fraud risk scoring.
- **Document Forgery Detection**: Detects tampered documents using OCR and deep learning models.
- **Behavioral Profiling**: Identifies suspicious patterns and relationships between customers and claims using Graph Neural Networks (GNNs).
- **Federated Learning**: Facilitates collaboration among insurers to improve fraud detection models while preserving data privacy.
- **Fraud Simulation**: Generates synthetic fraud data with GANs to enhance model robustness.
- **Real-Time Detection**: Implements lightweight models for fraud detection at the data ingestion stage.
- **Interactive Dashboard**: Visualizes fraud trends and high-risk claims for investigators.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/adaptive-ai-fraud-prevention.git
    cd adaptive-ai-fraud-prevention
    ```

2. **Create and activate the Conda environment**:
    ```bash
    conda env create -f environment.yml
    conda activate fraud-detection
    ```

3. **Install additional dependencies** (if needed):
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the project**:
    ```bash
    python test.py
    ```
