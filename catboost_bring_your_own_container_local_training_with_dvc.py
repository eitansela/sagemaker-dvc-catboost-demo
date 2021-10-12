# This is a sample Python program that trains a simple CatBoost Regressor tree model with data using DVC, and then performs inference.
# This implementation will work on your *local computer*.
#
# Prerequisites:
#   1. Install required Python packages:
#       pip install boto3 sagemaker pandas scikit-learn
#       pip install 'sagemaker[local]'
#   2. Docker Desktop has to be installed on your computer, and running.
#   3. Open terminal and run the following commands:
#       docker build  -t sagemaker-catboost-dvc-local container/.
###########################################################################################################################################

import pandas as pd
from sagemaker.estimator import Estimator
from sagemaker.local import LocalSession
from sagemaker.predictor import csv_serializer
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

sagemaker_session = LocalSession()
sagemaker_session.config = {'local': {'local_code': True}}

# For local training a dummy role will be sufficient
role = 'arn:aws:iam::111111111111:role/service-role/AmazonSageMaker-ExecutionRole-20200101T000001'
image = 'sagemaker-catboost-dvc-local'


def main():
    # Prepare data for testing model predictions
    data = fetch_california_housing()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=42
    )
    # we don't train a model, so we will need only the testing data
    testX = pd.DataFrame(X_test, columns=data.feature_names)

    # We use the Estimator from the SageMaker Python SDK
    local_regressor = Estimator(
        image,
        role,
        instance_count=1,
        instance_type="local",
        hyperparameters={
            "dvc-repo-url": "https://github.com/eitansela/sagemaker-dvc-catboost-demo",
            "dvc-branch-name":  "dev_dataset_1"
        },
    )

    # Start model training
    print("Starting model training.")
    local_regressor.fit()
    print('Completed model training.')

    # Deploy endpoint in local mode
    print('Deploying endpoint in local mode.')
    predictor = local_regressor.deploy(1, 'local', serializer=csv_serializer)

    # Invoke local mode endpoint to get predictions
    print('Invoking local mode endpoint to get predictions.')
    predicted = predictor.predict(testX[data.feature_names].to_csv(header=False, index=False)).decode('utf-8')
    print(predicted)

    # Delete the local endpoint
    print('About to delete the endpoint to stop paying (if in cloud mode).')
    predictor.delete_endpoint()

if __name__ == "__main__":
    main()