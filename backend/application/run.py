import os
import sys
import socket
sys.path.append(os.path.abspath('.'))
from application import app
from application.mongo import get_client
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
from flask_cors import CORS

client = get_client()
#client.server_info()
#database_names = client.list_database_names()
db = client["interview"]
collection = db['schedule']


CORS(app)

@app.route('/home',endpoint="home_page", methods=['GET', 'DELETE'])
def home_page():
    # GET Interview data from database
    if request.method == 'GET':
       
        
        collection.update_many({}, [{'$set': {'date': {'$toDate': '$date'}}}])
       
        
        result = collection.aggregate([
            {
                '$lookup': {'from': 'employee', 'localField': 'employees', 'foreignField': 'e_id', 'as': 'employees'}
            },
            {
                "$lookup": {'from': 'candidate', 'localField': 'candidate', 'foreignField': 'c_id', 'as': 'candidate'}
            },
            {
                "$project": {
                    "_id": 0,
                    "interview_id": 1,
                    "employees": ["$employees.e_id", "$employees.e_name"],
                    "candidate": ["$candidate.c_id", "$candidate.c_name"],
                    "date": {"year": {"$year": "$date"},
                             "month": {"$month": "$date"},
                             "day": {"$dayOfMonth": "$date"}
                             },
                    "slot": 1,
                    "status": 1
                }
            }
        ])
        interview_slots = []
        for c in result:
            interview_slots.append(dict(c))
        print()
        print(interview_slots)
        for interview in interview_slots:
            interview['employees'] = list(
                map(lambda x: {"id": x[0], "name": x[1]}, zip(interview['employees'][0], interview['employees'][1])))
            interview['candidate'] = {"id": interview['candidate'][0][0], "name": interview['candidate'][1][0]}
        response = jsonify(interview_slots)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        
    # DELETE a interview slot
    if request.method == 'DELETE':
        body = request.json
        id = body['interview_id']

        db.schedule.delete_one({'interview_id': id})
        print('\n # Deletion successful # \n')
        return jsonify({'status': 'Interview ID: ' + id + ' is deleted!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
