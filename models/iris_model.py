import pickle  # to save our trained model to disk

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()

X = iris['data']
y = iris['target']


class IrisModel:

    def __init__(self,features,target):
        
        self.features = features
        self.target   = target

    def scale_data(self):
        
        # get the attributes to the same scale
        scaler = StandardScaler()
        return scaler.fit_transform(X)

    def model(self):

        #train the model
        knn   = KNeighborsClassifier(n_neighbors=5)
        x_std = self.scale_data()
        knn.fit(x_std,y)
        pickle.dump(knn, open('model.pkl','wb'))  # Saving model to disk
        

def map_predictions(self):
        
        map_ = { 0 : 'Iris setosa',
                 1 : 'Iris versicolor',
                 2 : 'Iris virginica' 
                }

        for k,v in map_.items():
            pass

if __name__ == '__main__':
    classifier = IrisModel(X,y)
    classifier.model()
    