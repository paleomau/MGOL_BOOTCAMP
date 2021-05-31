import os
import sys
from flask import Flask, request, render_template
from functions import read_json


# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    #return app.send_static_file('greet.html')
    return "Por defecto"

@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/info")
def create_json():
    import pandas as pd
    df = pd.read_csv(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + os.sep + 'documentation' + os.sep + 'lung_nn_outl.csv')
    return df.to_json()

# localhost:6060/give_me_id?password=12345
@app.route('/give_me_id', methods=['GET'])
def give_id():
    token_id = request.args['password']
    if token_id == "p10875558":
        return request.args
    else:
        return "No es la contraseña correcta"
    

@app.route("/recibe_informacion")
def recibe_info():
    pass 

# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    # Para ambos: os.sep
    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons
    DEBUG = json_readed["debug"]
    HOST = json_readed["host"]
    PORT_NUM = json_readed["port"]
    # Dos posibilidades:
    # HOST = "0.0.0.0"
    # HOST = "127.0.0.1"  --> localhost
    app.run(debug=DEBUG, host=HOST, port=PORT_NUM)

if __name__ == "__main__":
    main()