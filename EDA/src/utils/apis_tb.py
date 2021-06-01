import os
import sys
from flask import Flask, request, render_template
from utils.functions import read_json


# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    #return app.send_static_file('greet.html')
    return "Por favor introduce el end-point /info, e introduce el parámetro token_id con el valor correspondiente"



@app.route("/info")
def create_json():
    if 'token_id' in request.args:
        x = request.args['token_id']
        if x == "p10875558":
            import pandas as pd
            df = pd.read_csv(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + os.sep + 'documentation' + os.sep + 'lung_nn_outl.csv')
            return df.to_json()
        else:
            return 'wrong password'
    else:
        return 'wrong parameter'



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