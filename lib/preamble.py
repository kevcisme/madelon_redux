import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
<<<<<<< HEAD
import pickle
import seaborn as sns
import warnings

from IPython.display import display, HTML, Image
from matplotlib import rcParams
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectKBest, SelectFromModel, RFE
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV, ShuffleSplit 
from sklearn.preprocessing import StandardScaler, MinMaxScaler


=======
import seaborn as sns
import warnings

from matplotlib import rcParams
>>>>>>> 4461a0f465f5d444b410cf5078ec98772b94c028

def suppress_warnings():
    warnings.filterwarnings('ignore')

__all__ = [
<<<<<<< HEAD
            'display',
            'GridSearchCV',
            'HTML',
            'Image',
            'Lasso',
            'MinMaxScaler',
            'np',
            'PCA',
            'pd',
            'pickle',
            'plt',
            'RandomForestRegressor',
            'rcParams',
            'RFE',
            'Ridge',
            'SelectKBest',
            'SelectFromModel',
            'StandardScaler',
            'ShuffleSplit',
            'sns',
            'warnings',
=======
            'np',
            'pd',
            'plt',
            'sns',
>>>>>>> 4461a0f465f5d444b410cf5078ec98772b94c028
          ]