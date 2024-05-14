from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://user:5uewbNA7iLteCcMp@blog-app.kh8tdua.mongodb.net/")
db = client['blog-app']
collection = db['filled-potholes']

@app.route('/')
def home():
    # Fetch data from MongoDB
    data = list(collection.find())
    return render_template('./index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
