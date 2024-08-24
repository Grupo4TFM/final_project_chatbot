from flask import Flask, render_template, request,  flash,redirect
import requests
from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

# connection to the database
config = dotenv_values(".env") 

@app.route("/")
def index():
    msg="NOTHING"
    return render_template('chat.html',msg=msg)


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    return get_Chat_response(msg)


def get_Chat_response(text):
    
    try : 

        reqUrl =  "https://final-project-api-w4e3.onrender.com/tfm4/llama_rag/"+text+"?="
        
        headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
        }
        response = requests.request("POST", reqUrl,headers=headersList)
        response=response.json()
        return response["data"]["response"]+"@@@"+response["data"]["source_nodes"][0]["node"]["metadata"]["file_name"]
    except :
        return "Sorry something happened!!!"


if __name__ == '__main__':
    app.run()
