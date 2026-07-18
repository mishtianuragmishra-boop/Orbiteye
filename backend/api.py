from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route("/api/satellitecount")
def satelitecount():
    return{ 
        "count":satelitecount()
    }

if __name__=="__main__":
    app.run(debug=True)