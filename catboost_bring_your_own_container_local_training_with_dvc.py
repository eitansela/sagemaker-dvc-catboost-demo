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
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

sagemaker_session = LocalSession()
sagemaker_session.config = {'local': {'local_code': True}}

# For local training a dummy role will be sufficient
role = 'arn:aws:iam::111111111111:role/service-role/AmazonSageMaker-ExecutionRole-20200101T000001'


image = 'sagemaker-catboost-dvc-local'

local_regressor = Estimator(
    image,
    role,
    instance_count=1,
    instance_type="local")

local_regressor.fit()

# predictor = local_regressor.deploy(1, 'local', serializer=csv_serializer)
#
# with open(local_test, 'r') as f:
#     payload = f.read().strip()
#
# predicted = predictor.predict(payload).decode('utf-8')
# print(predicted)
#
# predictor.delete_endpoint()
