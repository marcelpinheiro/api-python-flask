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
        if args.get('member_id') != None:
                data = data.query("MEMBER_ID ==" + args['member_id'])
        return data.to_json(), 200  # return data and 200 OK code
pass

@app.route('/totalwin',methods=["GET"])
def totalwin():
        args = get_arguments()
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV   
             
        data = data.query("MEMBER_ID ==" + args['member_id'])

        if args.get('month') != None:
                data = data[ data['ACTIVITY_YEAR_MONTH'].astype(str).str.endswith(args['month']) ]
        if args.get('game_id') != None:
                data = data.query("GAME_ID ==" + args['game_id'])
        
        data = data[['MEMBER_ID','WIN_AMOUNT']].groupby('MEMBER_ID').sum('WIN_AMOUNT')
               
        return data.to_json(), 200  # return data and 200 OK code
pass

@app.route('/wageramount',methods=["GET"])
def totalwageramount():
        args = get_arguments()
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
        data = data.query("MEMBER_ID ==" + args['member_id'])
        if args.get('month') != None:
                data = data[ data['ACTIVITY_YEAR_MONTH'].astype(str).str.endswith(args['month']) ]
        if args.get('game_id') != None:
                data = data.query("GAME_ID ==" + args['game_id'])

        data = data[['MEMBER_ID','WAGER_AMOUNT']].groupby('MEMBER_ID').sum('WAGER_AMOUNT')        
        
        return data.to_json(), 200  # return data and 200 OK code
pass

@app.route("/wagernumber",methods=["GET"])
def wagernumber():
        args = get_arguments()
        data = pd.read_csv('Revenue_Analysis_Test_Data.csv')  # read CSV
        data = data.query("MEMBER_ID ==" + args['member_id'])
        if args.get('month') != None:
                data = data[ data['ACTIVITY_YEAR_MONTH'].astype(str).str.endswith(args['month']) ]
        if args.get('game_id') != None:
                data = data.query("GAME_ID ==" + args['game_id'])
        data = data[['MEMBER_ID','NUMBER_OF_WAGERS']].groupby('MEMBER_ID').sum('NUMBER_OF_WAGERS')                        
        return data.to_json(), 200  # return data and 200 OK code
pass

    
if __name__ == '__main__':   
    app.run()  
    