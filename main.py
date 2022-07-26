from flask import Flask
from flask_restful import Api, Resource

# Wrapping the app in restful API
app = Flask(__name__)
api = Api(app)

# Resource has variables to work with different requests, so the object inherits these// key:value for json format
class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

# Adding resource to the API and defining the endpoint
api.add_resource(HelloWorld, "/helloworld")

# Starting the server of a minimal Hello World API
# debug = True for showing all logging informations while running the app// for testing
if __name__ == "__main__":
    app.run(debug=True)
