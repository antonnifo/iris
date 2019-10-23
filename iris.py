from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from flask_restful import Resource, request

iris = datasets.load_iris()

X = iris['data']
y = iris['target']


class IrisClassifier(Resource):

    @classmethod
    def scale_data(cls):
        
        # get the attributes to the same scale
        scaler = StandardScaler()
        return scaler.fit_transform(X)


    @classmethod
    def train_model(cls):

        #train the model
        knn   = KNeighborsClassifier(n_neighbors=5)
        x_std = IrisClassifier.scale_data()
        knn.fit(x_std,y)
        return knn
            
    def post(self):

        observations = request.get_json()
        print(observations['data'])
        # make predictions
        try:
            model = IrisClassifier.train_model()
            pred  = model.predict(observations['data'])

            return pred
        except :
            return {'error' : 'Something weired happened'}, 500 
    
