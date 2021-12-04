# ML_AWS_Deployment

## Scalable ML training in AWS Lambda

### Step1: Create an AWS Lambda function
Create the function in the US East (N. Virginia) zone because the ARN used to add the layer is available in the US East 1</br>
> While creating the Lambda function select python 3.8, 3.7, or 3.6.

### Step2: Add a lambda layer
Lambda function does not contain the scikit-learn, numpy or pandas library. So we need to import those libraries by adding the lambda layer using the ARN mentioned below</br>
| Name | ARN / Link | Compatible Runtimes |
|------|------------|---------------------|
| scikit-learn | ARN: `arn:aws:lambda:us-east-1:446751924810:layer:python-3-7-scikit-learn-0-23-1:2`<br>Link: [`model-zoo/scikit-learn-lambda`](https://github.com/model-zoo/scikit-learn-lambda) | `python3.6` `python3.7` `python3.8` |

### Step3: AWS Lambda code source
> Push the AWS_lambda_ML_deployment.py file to code source</br>
The code accepts 3 Parameters which can be passed in the string paramters of the POST request
- Model: 3 Models can be selected
  1. For the LinearRegression
  2. For the RandomForestRegressor
  3. For the GradientBoostingRegressor
- N_estimators: Number of the trees in the model 2 and model 3 ensembling
- Max_depth: Maximum depth of the tress used in the model 2 and model 3

### Step4: Build a HTTP API in the API Gateway
In the US East (N. Virginia) zone build HTTP API and integrate it with the AWS Lambda function created in the previous steps</br>
Create POST method and also check for the resource path</br>
Deploy the API

### Step5: Send the POST request using Postman
Convert the Dataset_train.csv to JSON data and pass it through the body of the POST request
> Pass the 3 string paramters according to the user requirement
