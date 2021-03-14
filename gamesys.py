from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import pandas as pd




app = Flask(__name__)
api = Api(app)

def get_arguments(self):
        parser = reqparse.RequestParser()
        parser.add_argument("member_id", default=None)
        parser.add_argument("month", default=None)
        parser.add_argument("game_id", default=None)
        
        args = parser.parse_args()

        print (
            args["member_id"],
            args["month"],
            args["game_id"]            
        ) 

   
@app.route('/general2',methods=["GET"])
def general2():
    get_arguments()
    # args = get_arguments
    # print( args['member_id'])
    data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
    # data = data.query("MEMBER_ID ==" + args['member_id'])
    data = data.to_dict()  # convert dataframe to dictionary
    return {'data': data}, 200  # return data and 200 OK code
pass





@app.route('/general/<search_term>',methods=["GET"])
def general(search_term):
    data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
    data = data.query("MEMBER_ID ==" + search_term)
    data = data.to_dict()  # convert dataframe to dictionary
    return {'data': data}, 200  # return data and 200 OK code
pass

@app.route('/totalwin/<search_term>',methods=["GET"])
def totalwin(search_term):
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV            
        data = data.query("MEMBER_ID ==" + search_term)
        result = float(data['WIN_AMOUNT'].sum())
        return {'data': result}, 200  # return data and 200 OK code
pass

@app.route('/totalwageramount/<search_term>',methods=["GET"])
def totalwageramount(search_term):
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
        data = data.query("MEMBER_ID ==" + search_term)
        result = float(data['WAGER_AMOUNT'].sum())
        # g.data = result  # convert dataframe to dictionary
        return {'data': result}, 200  # return data and 200 OK code
pass

@app.route("/wagernumber/<search_term>",methods=["GET"])
def wagernumber(search_term):
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
        data = data.query("MEMBER_ID ==" + search_term)
        result = int(data['NUMBER_OF_WAGERS'].sum())
        # data = result  # convert dataframe to dictionary
        return {'data': result}, 200  # return data and 200 OK code
pass

# @app.route("/teste",methods=["GET"])
# def teste():
#     # print(args['member_id'])
# pass
    




    
if __name__ == '__main__':   
    app.run()  # run our Flask app
    