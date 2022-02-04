import pandas as pd
import numpy as np

class RuleBasedClassifiers:
    
    x_train = []
    x_test = []
    y_train = []
    y_test = []

    n_sample = 0
    n_features = 0

    csv_datasets = ['./Data/contact_lenses.csv']

    csv_datasets_col_names = [['age','visual_deficiency','astigmatism','production','service_rating']]

    def csv_processor(self, csv_path, feature_names):
        dataset = pd.read_csv(csv_path)
        dataset.columns = feature_names
        return dataset

    def repair_continuous_attributes(self, dataset, features):
        self.n_sample = dataset.shape[0]
        self.n_features = dataset.shape[1] - 1

        for feature in features:
            if dataset[feature].dtype == np.float64:
                dataset[feature] = dataset[feature].astype(int)
                print(dataset[feature])
            

    def build_learning_sets(self, dataset, class_attr, train_size):

        dataset = dataset.sample(frac=1).reset_index(drop = True)
        n_train = int(self.n_sample*train_size)
        n_test = self.n_sample - n_train

        dataset_ = dataset.copy(deep = True)

        print(dataset_)

        input("Berhenti dahulu")

        self.y_train = dataset_.loc[0:n_train,class_attr].copy(deep=True)
        self.y_test = dataset_.loc[n_train+1:self.n_sample,class_attr].copy(deep=True)
        
        dataset_ = dataset_.drop(class_attr,1)

        self.X_train = dataset_.loc[0:n_train].copy(deep=True)
        self.X_test = dataset_.loc[n_train+1:self.n_sample].copy(deep=True)

    def display_data_info(self, dataset):
        print("\n1. Number of samples: " + str(self.n_sample))
        print("\n2. Number of features: " + str(self.n_features))
        print("\n3. Feature types:")
        print(dataset.dtypes)
        print("\n4. Data:")
        print(dataset)
        print("\n5. Training sets:")
        print(self.X_train)
        print(self.y_train)
        print("\n6. Testing sets:")
        print(self.X_test)
        print(self.y_test)

    def data_preprocessing(self):

        print('A) Memproses File CSV::')
        dataset = self.csv_processor(self.csv_datasets[0], self.csv_datasets_col_names[0])

        print('B) Memperbaiki Atribut Berkelanjutan di Datasets::')
        self.repair_continuous_attributes(dataset, dataset.columns)

        print('C) Membangun Train/Test sets::')
        self.build_learning_sets(dataset,dataset.columns[-1],1.0)

        print('D) Informasi Dataset::')
        self.display_data_info(dataset)

    def PRISM(self):
        prism_rule_test = []

RBC = RuleBasedClassifiers()

RBC.data_preprocessing()
rule_set = RBC.PRISM()

print("----------- FINAL PRISM RULE TEST -----------\n")
for prism_rule in rule_set:
    print(prism_rule)