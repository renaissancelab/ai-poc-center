import xgboost as xgb
import time
import os
import numpy as np

if __name__ == '__main__':
    # Ready
    CURRENT_DIR = os.path.dirname(__file__)
    # Load
    model_name = 'xgboost_model_1113.model'
    bst = xgb.Booster({'nthread': 4})  # init model
    bst.load_model(CURRENT_DIR+"/models/"+model_name)  # load data
    dtest = xgb.DMatrix('dtest.buffer')
    preds = bst.predict(dtest)
    print(preds)


