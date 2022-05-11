import os
from flask import Flask, render_template, request, redirect, url_for, abort,jsonify
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

Employee=[{
    'empId':'1001',
    'empName':'Debasmit',
    'CompanyName':'StratLytics',
    'DOJ':'1/1/2015',
    'Designation':"CEO"
     },
    {
    'empId':'1002',  
    'empName':'Bratati',
    'CompanyName':'StratLytics',
    'DOJ':'1/1/2015',
    'Designation':"CFO"},
    {
    'empId':'1005',
    'empName':'Abhisek',
    'CompanyName':'StratLytics',
    'DOJ':'1/1/2020',
    'Designation':"Consultant"
    }]



@app.route('/')
def upload():
    return render_template("upload1.html")

@app.route('/done',methods=['POST'])
def doUpload():
    if request.method=='POST':
        f=request.files['file']
        f.save(f.filename)
        return render_template('done.html',name=f.filename)


@app.route('/index')
def index():
    return " Welcome to our StratLytics's API call"

@app.route("/employee",methods=['GET'])
def get():
    return jsonify({"Employee":Employee})

@app.route("/employee/<int:empId>",methods=["GET"])
def get_emp(empId):
    return jsonify({"employee":Employee[empId]})

@app.route("/employee",methods=['POST'])
def create():
    newEmployee={
    'empId':'1007',
    'empName':'Abhi',
    'CompanyName':'StratLytics',
    'DOJ':'1/1/2022',
    'Designation':"Associate Consultant"
    }
    Employee.append(newEmployee)
    return jsonify({"NewEmp":Employee})
# to run this, use curl -i -H "Content-Type:Application/json" -X POST http://localhost:5000/employee/

@app.route("/employee/<int:EmpId>", methods=["PUT"])
def emp_update(empId):
    Employee[empId]["EmpType"]="temp"
    return jsonify({'Employee':employee[empId]})



@app.route("/employee/<int:emplId>",methods=['DELETE'])
def delete(empId):
    Employee.remove(Employee[empId])
    return jsonify({'result':True})




if __name__=='__main__':
    app.run(debug=True)

    
