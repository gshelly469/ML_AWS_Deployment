# ML_AWS_Deployment

## Deploy the ML model on AWS Lambda

### Step1: Create an AWS Lambda function
> Create the function in the US East (N. Virginia) zone because the ARN used to add the layer is available in the US East 1. While creating the Lambda function select python 3.8, 3.7, or 3.6.

### Step2: Add a lambda layer
> Lambda function does not contain the scikit-learn, numpy or pandas library. So we need to import those libraries by adding the lambda layer using the ARN mentioned below</br>
| scikit-learn | ARN: `arn:aws:lambda:us-east-1:446751924810:layer:python-3-7-scikit-learn-0-23-1:2`<br>Link: [`model-zoo/scikit-learn-lambda`](https://github.com/model-zoo/scikit-learn-lambda) | `python3.6` `python3.7` `python3.8` |

### Step3: 

