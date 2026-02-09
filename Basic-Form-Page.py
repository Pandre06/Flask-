from flask import Flask

app = Flask(__name__):        #app is the object is for Flask class

@app.route("/")                #defining oute for home page
def hello_world:
  return "Hello. All, this is my First Flask Website.

@app.route('/about')   # defining route for about page - used for connecting url to function
def about():
    return "This is a simple Flask application created by Sagar."   #returning response for about page

@app.route('/contact')   # defining route for contact page
def contact():  
    return "Contact me at:"

@app.route('/contact/email')   # defining route for email contact
def contact_email():
    return "Email: zyz@example.com"

@app.route('/contact/phone')   # defining route for phone contact
def contact_phone():        
    return "Phone: +1234567890"  

@app.route("/submit", methods=['POST',"GET"])   # defining route for form submission with POST method
def submit():
    if request.method == 'POST':
        return "Form submitted successfully!"   #returning response for form submission
    else:
        return "Please submit the form using POST method."   #response for non-POST requests


if __name__ == '__main__':   #ensuring the app runs only if this file is executed directly
    app.run(debug=True)    #running the app in debug mode for easier development and troubleshooting



