# basics 
import os 
import numpy as np 

# data
import pandas as pd 

# machine learning 
# scaling of data
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
# train/test split
from sklearn.model_selection import train_test_split
# model selection 
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
# model
from sklearn.kernel_ridge import KernelRidge
# pipeline 
from sklearn.pipeline import Pipeline
# PCA
from sklearn.decomposition import PCA
# Dummy model
from sklearn.dummy import DummyClassifier, DummyRegressor
# Variance Threshold 
from sklearn.feature_selection import VarianceThreshold, SelectFromModel
# metrics 
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             mean_absolute_error, mean_squared_error, max_error)
# feature names
#from descriptornames import * 

# save/load models 
import joblib

# For the permutation importance
from joblib import Parallel
from joblib import delayed
from sklearn.metrics import check_scoring
from sklearn.utils import Bunch
from sklearn.utils import check_random_state
from sklearn.utils import check_array

# plotting 
import matplotlib.pyplot as plt 
import seaborn as sns

# for interactive plots, you can try to use holoviewes
import holoviews as hv
from holoviews import dim, opts
hv.extension('plotly', 'bokeh', 'matplotlib')

RANDOM_SEED = 4242424242
DATA_DIR = 'data'
DATA_FILE = os.path.join(DATA_DIR, 'data.csv')

np.random.seed(RANDOM_SEED)

df = pd.read_csv('data/data.csv')

print(df.head())

