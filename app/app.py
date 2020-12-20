from flask import Flask, request, jsonify
import json

from registerUser import registerUserSQL
app = Flask(__name__)

@app.route('/')
def homeendpoint():
    return 'Main Endpoint'
    
@app.route('/registerUser', methods=["GET", "POST"])
def registerUser():
    if request.method == "POST":
        post_data = request.get_json(force = True)
        print(post_data)
        firstName = post_data.get("firstName")
        lastName = post_data.get("lastName")
        email = post_data.get("email")
        passHash = post_data.get("passHash")
        response = registerUserSQL(firstName, lastName, email, passHash)
        return jsonify(serverResponse = response)
    else:
        response = "OKAY"
    return response
    
    
    
    
if __name__ == "__main__":
    # http://flask.pocoo.org/docs/0.12/errorhandling/#working-with-debuggers
    # https://docs.aws.amazon.com/cloud9/latest/user-guide/app-preview.html
    use_c9_debugger = False
    app.run(use_debugger=not use_c9_debugger, debug=True,
                    use_reloader=not use_c9_debugger, host='0.0.0.0', port=8080)

