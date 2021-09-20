from flask import Flask
from flask_restful import Api, Resource
from joblib import load

#Defining App !
app = Flask(__name__)
api = Api(app)
# defining route Resource
class Model(Resource):
    def get(self, job_title):
        model = load('model.joblib')
        pred_industry = model.predict([job_title])
        return pred_industry[0], 200
   
# Adding routes to the Application and Endpoints to App to predict input job title.
api.add_resource(Model, "/model/api/<string:job_title>")

# Run the server !
app.run()