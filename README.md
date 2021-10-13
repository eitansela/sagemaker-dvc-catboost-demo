## Amazon SageMaker CatBoost regression model with DVC Example
## This is `dev_dataset_1` branch used to store DVC metadata files and cache

## Commands used to create the branch using DVC
Below are the commands used to create this branch using DVC.

### Initialize DVC in `dev_dataset_2 branch`
```console
dvc init
git commit -m "Initialize DVC"
```

### Copy the data files needed for training 
```console
mkdir dataset
cp <source> ./dataset/train/california_train_1.csv
cp <source> ./dataset/train/california_train_2.csv
cp <source> ./dataset/train/california_train_3.csv
cp <source> ./dataset/train/california_train_4.csv
cp <source> ./dataset/train/california_train_5.csv
cp <source> ./dataset/test/california_test.csv  
cp <source>./dataset/validation/california_validation_1.csv
cp <source>./dataset/validation/california_validation_2.csv
cp <source>./dataset/validation/california_validation_3.csv 
```

### Start tracking our train, test and validation dataset files
```console
dvc add ./dataset/train/*.csv
dvc add ./dataset/test/*.csv 
dvc add ./dataset/validation/*.csv
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