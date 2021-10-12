## Amazon SageMaker Local Mode with DVC Example

This repository contains example and related resources showing you how to train a CatBoost model with California housing dataset, fetched using DVC, and serve on your local machine using Amazon SageMaker Local mode. 

## Overview

### SageMaker Local Mode
The local mode in the Amazon SageMaker Python SDK can emulate CPU (single and multi-instance) and GPU (single instance) SageMaker training jobs by changing a single argument in the TensorFlow, PyTorch or MXNet estimators.  To do this, it uses Docker compose and NVIDIA Docker.  It will also pull the Amazon SageMaker TensorFlow, PyTorch or MXNet containers from Amazon ECS, so you’ll need to be able to access a public Amazon ECR repository from your local environment.

[Read the blog post](https://aws.amazon.com/blogs/machine-learning/use-the-amazon-sagemaker-local-mode-to-train-on-your-notebook-instance/)

### California Housing dataset
We use the California Housing dataset, present in [Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html). 

The California Housing dataset was originally published in:

Pace, R. Kelley, and Ronald Barry. "Sparse spatial auto-regressions." Statistics & Probability Letters 33.3 (1997): 291-297.

### Data Version Control · DVC
DVC is built to make ML models shareable and reproducible. It is designed to handle large files, data sets, machine learning models, and metrics as well as code.

[DVC Official Site](https://dvc.org/)

## Branches used in this GitHub Repository
In this example, there are two branches used in the GitHub repo: 
- `main` - used to store the Python code and file needed to build the Docker image for CatBoost. 
- `dev_dataset_1` - used to store DVC metadeta files and cache.