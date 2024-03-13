# import necessary libraries and functions 
from flask import Flask, jsonify, request 
  
# creating a Flask app 
app = Flask(__name__) 

@app.route('/', methods=['GET', 'POST']) 
def home(): 
    if request.method == 'GET': 
        client_ip = request.headers.get('X-Forwarded-For')
        # If X-Forwarded-For header is not present, get the remote address
        if not client_ip:
            client_ip = request.remote_addr

        data = "hello world"
        return jsonify({'data': data, 'your_ip': client_ip}) 
  
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
