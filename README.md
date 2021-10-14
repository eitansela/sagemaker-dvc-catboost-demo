## Amazon SageMaker CatBoost regression model with DVC Example
## This is `dev_dataset_1` branch used to store DVC metadata files and cache

## Commands used to create the branch using DVC
Below are the commands used to create this branch using DVC.

### Initialize DVC in `dev_dataset_1 branch`
```console
dvc init
git commit -m "Initialize DVC"
```

### Copy the data files needed for training 
```console
mkdir dataset
cp <source> ./dataset/train/california_train.csv
cp <source> ./dataset/test/california_test.csv  
cp <source>./dataset/validation/california_validation.csv 
```

### Start tracking our train, test and validation dataset files
```console
dvc add ./dataset/train/california_train.csv
dvc add ./dataset/test/california_test.csv 
dvc add ./dataset/validation/california_validation.csv
git add ./dataset/*
git commit -m "Add train, test and validation dataset files"
```

### Upload our DVC-tracked dataset files to S3
```console
dvc remote add -d storage s3://<YOUR_BUCKET>
git add .dvc/config
git commit -m "Configure DVC remote storage"
dvc push
```

### Retrieve our DVC-tracked dataset files from S3
```console
dvc pull
```