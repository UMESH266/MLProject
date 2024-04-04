import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomeException
from src.logger import logging

from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrianer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array, preprocessor_path):
        try:
            logging.info('split training and test input data')
            x_train, y_train, x_test, y_test = (train_array[:, :-1], train_array[:, -1],
                                                test_array[:,:-1], test_array[:,-1])
            
            models = {
                'Random forest': RandomForestRegressor(),
                'Decision tree': DecisionTreeRegressor(),
                'Gradient boosting': GradientBoostingRegressor(),
                'Linear regressor': LinearRegression(),
                'KNN regressor': KNeighborsRegressor(),
                'XGB regressor': XGBRegressor(),
                'Catboost regressor': CatBoostRegressor(),
                'Adaboost regressor': AdaBoostRegressor()
            }

            model_report:dict = evaluate_models(x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test,
                                               models=models)

            }

        except:
            pass
