
import optuna
import optuna.visualization as vis
import time
import scipy.stats as st

import pandas as pd
import numpy as np

# import matplotlib.pyplot as plt
# import seaborn as sns

from sklearn.model_selection import cross_val_score

# from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
from sklearn.neighbors import KNeighborsRegressor,KNeighborsClassifier


from sklearn.preprocessing import MinMaxScaler, StandardScaler,OneHotEncoder
from sklearn.metrics import  root_mean_squared_error, make_scorer

def objective(trial, confidence_level, folds, X_train, y_train):

    # First, we define the grid with values to consider when train several possible combinations.
    # Now we specify a range/list of values to try for each hyper-parameter, and we let optuna to decide which
    # combination to try.
    n_neighbors = trial.suggest_int("n_neighbors", 2, 25)
    weights = trial.suggest_categorical("weights", ['uniform', 'distance'])
    p = trial.suggest_int("p", 1, 3)

    knn = KNeighborsRegressor(n_neighbors=n_neighbors,
                              weights=weights,
                              p=p)

    scorer = make_scorer(root_mean_squared_error)

    scores = cross_val_score(knn, X_train, y_train, cv=folds, scoring=scorer) # The scores provided will be the R2 on each hold out fold
    # scores = cross_val_score(knn, X_train_norm_df, y_train, cv=folds)# The scores provided will be the R2 on each hold out fold
    mean_score = np.mean(scores)

    sem = np.std(scores, ddof=1) / np.sqrt(folds)
    tc = st.t.ppf(1-((1-confidence_level)/2), df=folds-1)

    lower_bound = mean_score - ( tc * sem )
    upper_bound = mean_score + ( tc * sem )

    # Here, we're storing confidence interval for each trial. It's not possible for the objective function to return
    # multiple values as Optuna uses the only returned value to find the best combination of hyperparameters.
    trial.set_user_attr("CV_score_summary", [round(lower_bound,4), round(np.mean(scores),4), round(upper_bound,4)])

    return np.mean(scores)