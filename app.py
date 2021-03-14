from datetime import datetime
from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import pandas as pd




app = Flask(__name__)
api = Api(app)

def get_arguments():
        parser = reqparse.RequestParser()
        parser.add_argument("member_id", default=None)
        parser.add_argument("month", default=None)
        parser.add_argument("game_id", default=None)
        
        return parser.parse_args()
   
@app.route('/general',methods=["GET"])
def general():
        args = get_arguments()
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
        data = data.query("MEMBER_ID ==" + args['member_id'])
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code
pass

@app.route('/totalwin',methods=["GET"])
def totalwin():
        args = get_arguments()
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV   
             
        data = data.query("MEMBER_ID ==" + args['member_id'])

        if args.get('month') != None:
                data = data[ data['ACTIVITY_YEAR_MONTH'].astype(str).str.endswith(args['month']) ]
        
        result = float(data['WIN_AMOUNT'].sum())
        
        return {'data': result}, 200  # return data and 200 OK code
pass

@app.route('/totalwageramount',methods=["GET"])
def totalwageramount():
        args = get_arguments()
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
        data = data.query("MEMBER_ID ==" + args['member_id'])
        result = float(data['WAGER_AMOUNT'].sum())
        # g.data = result  # convert dataframe to dictionary
        return {'data': result}, 200  # return data and 200 OK code
pass

@app.route("/wagernumber",methods=["GET"])
def wagernumber():
        args = get_arguments()
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
        data = data.query("MEMBER_ID ==" + args['member_id'])
        result = int(data['NUMBER_OF_WAGERS'].sum())
        # data = result  # convert dataframe to dictionary
        return {'data': result}, 200  # return data and 200 OK code
pass

    
if __name__ == '__main__':   
    app.run()  
    