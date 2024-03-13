# import necessary libraries and functions 
from flask import Flask, jsonify, request 
  
# creating a Flask app 
app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST']) 
def home(): 
    if request.method == 'GET': 
        data = "flaskserver"
        team_members = [
            {"id": 10, "roll_number": "AP21110010053", "name": "KANDULA AYYAPPA", "grade": "A", "group": "Group-3"},
            {"id": 11, "roll_number": "AP21110010064", "name": "JENIL PADSHALA", "grade": "A"},
            {"id": 12, "roll_number": "AP21110010079", "name": "CHAGANTIPATI AETESH", "grade": "B"},
            {"id": 13, "roll_number": "AP21110010081", "name": "BOLLINENI ROHITH", "grade": "B"},
            {"id": 14, "roll_number": "AP21110010091", "name": "V D PANDURANGA SAI GUPTHA", "grade": "B"}
        ]
        return jsonify({'site_name': data, 'message': 'welcome to flaskServer', 'team_members': team_members, 'topic_name': 'amazon ec2'}) 
  
# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000/home/10 
# this returns 100 (square of 10) 
@app.route('/home/<int:num>', methods=['GET']) 
def disp(num): 
    return jsonify({'data': num**2}) 
  
# driver function 
if __name__ == '__main__': 
    # Run the app, listening on all available network interfaces
    app.run(host='0.0.0.0', port=5000, debug=True)
