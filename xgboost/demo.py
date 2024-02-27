import xgboost as xgb
import time
import os
import numpy as np


if __name__ == '__main__':
    # Ready
    CURRENT_DIR = os.path.dirname(__file__)
    dtrain = xgb.DMatrix(CURRENT_DIR+'/resource/data/agaricus.txt.train?format=libsvm')
    dtest = xgb.DMatrix(CURRENT_DIR+'/resource/data/agaricus.txt.test?format=libsvm')
    watchlist = [(dtest, "eval"), (dtrain, "train")]

    # Training
    print("start running example to start from a initial prediction")
    param = {'max_depth': 2, 'eta': 1, 'objective': 'binary:logistic'}
    num_round = 2
    bst = xgb.train(param, dtrain, num_round, watchlist)

    t = time.time()
    model_name = str(int(round(t)))+".model"
    bst.save_model(CURRENT_DIR+"/models/"+model_name)

    # Load
    bst = xgb.Booster({'nthread': 4})  # init model
    bst.load_model(CURRENT_DIR+"/models/"+model_name)  # load data

    # Prediction
    ptrain = bst.predict(dtrain, output_margin=True)
    ptest = bst.predict(dtest, output_margin=True)
    dtrain.set_base_margin(ptrain)
    dtest.set_base_margin(ptest)

    print("this is result of running from initial prediction")
    bst = xgb.train(param, dtrain, 1, watchlist)
