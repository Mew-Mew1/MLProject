##Data ingestion is the process of collecting, importing, and preparing raw data from multiple sources into a system for storage, processing, and analysis.
#eg. train and test
import os
import sys
from source.exception import CustomException
from source.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from source.components.data_transformation import DataTransformation
from source.components.data_transformation import DataTransformationConfig
from source.components.model_trainer import ModelTrainerConfig
from source.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv(r'C:\Projects\MLProject\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_training(train_arr,test_arr))





'''
@dataclass: Automatically generates boilerplate methods like __init__, __repr__, and __eq__, making the class 
cleaner and easier to use.
Attributes:
- train_data_path → points to "artifacts/train.csv"
- test_data_path → points to "artifacts/test.csv"
- raw_data_path → points to "artifacts/raw.csv"

Purpose: It’s a configuration holder for file paths used in a data pipeline (training, testing, raw data). 
Instead of hardcoding paths everywhere, you centralize them in one structured class.

'''



'''
- This block only runs when you execute the file directly (not when it’s imported as a module).
- It creates an instance of the DataIngestion class (obj) and then calls its method initiate_data_ingestion().
- That’s the entry point of your pipeline: it triggers the ingestion process, which should read the CSV, split 
the data, and save it into the artifacts folder.
'''

'''
__init__: Creates a DataIngestionConfig object, which holds the file paths for 
raw, train, and test data.
initiate_data_ingestion:
1. Logs the start of ingestion.
2. Reads the dataset (stud.csv) into a pandas DataFrame.
3. Ensures the artifacts directory exists.
4. Saves the raw dataset to raw.csv.
5. Splits the data into training and testing sets (80/20 split).
6. Saves those sets to train.csv and test.csv.
7. Logs completion and returns the paths of the train and test files.
8. Error handling: If anything fails, it raises a CustomException with detail.

'''