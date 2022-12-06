from flask import *
import json
import requests
import pyodbc
a=[0,1,2,3,4,5]
print(a[-1])
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f' {escape(subpath)}'
@app.route('/Test2')
def about():
     return render_template("drainwax.html")
@app.route("/Test")
def hello_world1():
    return render_template("casting.html")
@app.route("/Test1")
def hello_world2():
    return render_template("threadverification.html")
@app.route('/Test3')
def hello_world3():
     return render_template("deburring.html")
# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         ten = request.form["quang"] 
#         print(ten)
#         ten2 = request.form["ngay"]
#         print(ten2) 
#         #url2 = 'http://127.0.0.1:5000/login'
#         #Req = requests.(url2)
#         #ten1=json.loads(Req.status_code)
#         #print(ten1)
#         return ""
#     else:
#         return render_template("quang2.html")
# @app.route('/printdmc', methods=['POST'])
# def printdmc():
#     g = request.form["casting"] 
#     gg = request.form["product"] 
#     print(g+"quang dep trai"+gg)
    
#     return "Quang"
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=999)

