import numpy as np
from flask import Flask, request
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def process(data, model, n_estimators=100, max_depth=3):

    data_items = np.zeros((len(data), 5))
    y_train_pre= np.zeros((len(data), 1))

    type_list=[]

    for i in range(len(data)):

        data_items[i][0] = data[i]["l1"]
        data_items[i][1] = data[i]["l2"]
        data_items[i][2] = data[i]["l3"]
        data_items[i][3] = data[i]["l4"]
        data_items[i][4] = data[i]["l5"]
        y_train_pre[i][0] = data[i]["target"]
        type_list.append(data[i]["type"])

    # print(data_items)

    X_train_pre = data_items
    unique_type_list = []

    for item in type_list:
        if item not in unique_type_list:
            unique_type_list.append(item)
            
    last_element = unique_type_list[-1]
    unique_type_list = unique_type_list[:-1]
    # print(unique_type_list)

    dic_unique_items = {}
    for i in range(len(unique_type_list)):
        dic_unique_items[unique_type_list[i]] = i
    print(dic_unique_items)

    row_size=len(type_list)
    column_size = len(unique_type_list)

    arr = np.zeros((row_size, column_size))


    for i in range(len(type_list)):
        if type_list[i] != last_element:
            arr[i][dic_unique_items[type_list[i]]]=1


    X_train_pre = np.append(X_train_pre, arr, axis=1)

    pre_scaling = StandardScaler()
    X_train_pre = pre_scaling.fit_transform(X_train_pre)

    X_train, X_test, y_train, y_test = train_test_split(X_train_pre, y_train_pre, test_size=0.01, random_state=0)

    print(type(n_estimators),n_estimators, type(max_depth), max_depth, 'this is the model')
    if model=='1':
        lr = LinearRegression()
        lr.fit(X_train, y_train.ravel())
        pred = lr.predict(X_test)
        mse = mean_squared_error(y_test, pred)
    elif model=='2':
        rfr = RandomForestRegressor(random_state=0, n_estimators=int(n_estimators), max_depth=int(max_depth))
        rfr.fit(X_train, y_train.ravel())
        pred = rfr.predict(X_test)
        mse = mean_squared_error(y_test, pred)
    elif model=='3':
        gbr = GradientBoostingRegressor(random_state=0, n_estimators=int(n_estimators), max_depth=int(max_depth))
        gbr.fit(X_train, y_train.ravel())
        pred = gbr.predict(X_test)
        mse = mean_squared_error(y_test, pred)

    else:
        mse = "Model parameter not between 1-3"


    return mse



app = Flask(__name__)
@app.route('/')
def home():
    return "key"

@app.route('/testmlpost', methods=['POST'])
def lambda_func():
    req_data = request.get_json()
    model = request.args.get('model')   
    n_estimators = request.args.get('n_estimator')
    max_depth = request.args.get('max_depth')

    meanSquareError = process(req_data, model, n_estimators, max_depth)
    print(meanSquareError)

    # print(req_data)

    return json.dumps({"MSE":meanSquareError})
    
# If deployed in the Local System then no need to add the host
app.run(host = '0.0.0.0', port=8000)
