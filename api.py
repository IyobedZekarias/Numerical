# from flask import Flask
# from flask_restful import Resource, Api, reqparse
from Library.Rational import Rational

# app = Flask(__name__)
# api = Api(app)

# class Rationalclass(Resource):
#     def get(self):
#         data = {'example': 'working'}
#         print('working')
#         return {'data': data}, 200


#     def post(self):
#         parser = reqparse.RequestParser()  # initialize
        
#         parser.add_argument('num', required=True)  # add args
#         parser.add_argument('den', required=True)
        
#         args = parser.parse_args()  # parse arguments to dictionary
#         print('working')
#         return {'data': args}, 200
    

# api.add_resource(Rationalclass, '/rational') 


# if __name__ == '__main__':
#     app.run()  # run our Flask app



from flask import Flask, request
app = Flask(__name__)
#Make an app.route() decorator here

@app.route("/rational", methods = ['GET', 'POST'])
def RationalFunction():
    if request.method == 'GET':
        data = {'example': 'working'}
        print('working')
        return {'data': data}, 200

    elif request.method == 'POST':
        num = request.args.get('num')
        den = request.args.get('den')
        data = {
            'num': num,
            'den': den,
            'Rational': Rational(int(num), int(den)).__str__() 
        }
        return {'data': data}, 200

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)