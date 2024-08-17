from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    # Create a response object
    response = make_response("Cookie is set!")
    
    # Set a cookie on the response object
    response.set_cookie('my_cookie', 'cookie_value')
    
    # Return the response with the cookie
    return response

@app.route('/get_cookie')
def get_cookie():
    # Retrieve the cookie value from the request
    cookie_value = request.cookies.get('my_cookie')
    
    # Return the cookie value
    return f'The value of the cookie is: {cookie_value}'

if __name__ == "__main__":
    app.run(debug=True)
