afrom flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
from flask import send_file
from cv2 import *
import time
app = Flask(__name__)

engine = create_engine('oracle://hr:hr@127.0.0.1:1521/xe', convert_unicode=True)


@app.route("/getdata")
def getdata():
   #conn = engine.connect()
   #query = conn.execute("select * from employees") # This line performs query and returns json result
   return ("asdfasd") # Fetches first column that is Employee ID


@app.route("/pic")
def index():
     pic= str(time.time())
     print(pic)
     #conn = engine.connect()
     #query = conn.execute("select * from employees") # This line performs query and returns json result
     #return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
     # initialize the camera
     cam = VideoCapture(0)   # 0 -> index of camera
     s, img = cam.read()
     if s:    # frame captured without any errors
      #namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
      #imshow("cam-test",img)
      #waitKey(0)
      #destroyWindow("cam-test")
      imwrite(pic+".jpg",img)
      return send_file(pic+'.jpg', mimetype='image/gif')
      #return("BAD boy")
 
if __name__ == "__main__":
    app.run(host="192.168.0.111",port=80)