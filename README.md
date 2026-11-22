# MLOps Kubeflow Pipeline

This project demonstrates a simple ML pipeline created with Kubeflow Pipelines.

## Technologies

- Python
- Kubeflow Pipelines (KFP)
- Kubernetes
- Minikube

## Pipeline structure

The pipeline consists of three components:

1. `prepare_data` — prepares input data.
2. `train_model` — performs a simple model training calculation.
3. `evaluate_model` — evaluates the result.

## Files

- `pipeline.py` — Python source code of the pipeline.
- `pipeline.yaml` — compiled pipeline specification.

## Run environment

The project was prepared using a local Minikube Kubernetes cluster with Kubeflow Pipelines.
