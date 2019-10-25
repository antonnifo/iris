from flask import Flask

from flask_restful import Api
from resources.iris import IrisClassifier

# created an object of flask using a unique name
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True 
api = Api(app)


api.add_resource(IrisClassifier ,'/iris')        
      

if __name__ == '__main__':
    app.run()
