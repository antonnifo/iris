import pickle  # to save our trained model to disk
import json

import numpy as np
from flask_restful import Resource, request


class IrisClassifier(Resource):
           
    def post(self):

        observations = request.get_json(force=True)
        data = json.loads(observations['data'])
               
        try:

            model    = pickle.load(open('./model.pkl','rb'))
            pred     = model.predict(data)
            int_pred = int(pred[0])
            # pred  = np.array2string(model.predict(data))

            if int_pred == 0:
                prediction = 'Iris setosa'

            elif int_pred == 1:
                prediction = 'Iris versicolor'

            elif int_pred == 2:
                prediction = 'Iris virginica'
            else:
                prediction =  'an error occurred' 

            return prediction        

        except :
            
            return {'error' : 'Something weired happened'}, 500 
