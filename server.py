
from flask import Flask

# app config
app = Flask(__name__)
app.secret_key = '#nobiscuitsChallange'
app.debug = True



# Home Page
@app.route('/')
def home():
    # do your logic for route '/' here
    return "Sobhy Is doing some stuff!"
####


# Main Function To Run the App
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded = True)
