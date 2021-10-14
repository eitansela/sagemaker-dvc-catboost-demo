## Amazon SageMaker CatBoost regression model with DVC Example

This repository contains example and related resources showing you how to train a CatBoost model with California housing dataset, fetched using DVC. 

## Overview

```bash
.
├── README.MD                                                     <-- This instructions file
├── catboost_bring_your_own_container_local_training_with_dvc.py  <-- Python code to run example with SageMaker Local
├── catboost_bring_your_own_container_training_with_dvc.ipynb     <-- Notebook to run example with SageMaker Notebooks instance
├── install_dvc_on_sagemaker_notebook.ipynb                       <-- Notebook that shows how to install DVC on SageMager notebook instance
├── container                                                     <-- All the components you need to package the sample algorithm for Amazon SageMager
│   └── Dockerfile                                                <-- Describes how to build your Docker container image
│   └── catboost_regressor                                        <-- Contains the files that will be installed in the container
```

## Branches used in this GitHub Repository
In this example, there are three branches used in the GitHub repo: 
- `main` - used to store the Python code and file needed to build the Docker image for CatBoost. 
- `dev_dataset_1` - used to store DVC metadata files and cache for development dataset #1.
- `dev_dataset_2` - used to store DVC metadata files and cache for development dataset #2.

## Resources

### SageMaker Local Mode
The local mode in the Amazon SageMaker Python SDK can emulate CPU (single and multi-instance) and GPU (single instance) SageMaker training jobs by changing a single argument in the TensorFlow, PyTorch or MXNet estimators.  To do this, it uses Docker compose and NVIDIA Docker.  It will also pull the Amazon SageMaker TensorFlow, PyTorch or MXNet containers from Amazon ECS, so you’ll need to be able to access a public Amazon ECR repository from your local environment.

[Read the blog post](https://aws.amazon.com/blogs/machine-learning/use-the-amazon-sagemaker-local-mode-to-train-on-your-notebook-instance/)


### SageMaker notebook instance
An Amazon SageMaker notebook instance is a machine learning (ML) compute instance running the Jupyter Notebook App. SageMaker manages creating the instance and related resources. Use Jupyter notebooks in your notebook instance to prepare and process data, write code to train models, deploy models to SageMaker hosting, and test or validate your models.

[Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)

### California Housing dataset
We use the California Housing dataset, present in [Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html). 

The California Housing dataset was originally published in:

Pace, R. Kelley, and Ronald Barry. "Sparse spatial auto-regressions." Statistics & Probability Letters 33.3 (1997): 291-297.

### Data Version Control · DVC
DVC is built to make ML models shareable and reproducible. It is designed to handle large files, data sets, machine learning models, and metrics as well as code.

[DVC Official Site](https://dvc.org/)

