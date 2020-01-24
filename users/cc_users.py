from flask import Flask, render_template, request, jsonify
import hashlib
import base64
import binascii
import json
import pymysql
import datetime
import requests
fd=open("count.txt","w")
fd.write("0")
fd.close()
count=0

app=Flask(__name__)

@app.route('/api/v1/_count', methods = ['GET'])
def count_requests():
    if request.method == 'GET':
        r=requests.get('http://52.21.133.199:80/api/v1/categories')
        if r.status_code==500:
           return r.status_code
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        fd.close()
        l=[]
        l.append(count)

        response = app.response_class(response=json.dumps(l), status=200, mimetype='application/json')
        return response
    else:
        r=requests.get('http://52.21.133.199:80/api/v1/categories')
        if r.status_code==500:
           return r.status_code        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
        return response

@app.route('/api/v1/_count', methods = ['DELETE'])
def reset_requests():
    if request.method == 'DELETE':
       r=requests.get('http://52.21.133.199:80/api/v1/categories')
       if r.status_code==500:
          return r.status_code       
       fd=open("count.txt","w")
       fd.write("0")
       fd.close()
       response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')
       return response
    else:
       r=requests.get('http://52.21.133.199:80/api/v1/categories')
       if r.status_code==500:
          return r.status_code        
       response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
       return response

def isBase64(s):
    try:
        if(base64.b64encode(base64.b64decode(s)) == s):
           return 1
    except Exception:
        return 0

def date(date_string):
    date_format = '%d-%m-%Y:%S-%M-%H'
    try:
        date_obj = datetime.datetime.strptime(date_string, date_format)
        return 0
    except ValueError:
           return 1

def is_sha1(maybe_sha):
    if len(maybe_sha) != 40:
        return False
    try:
        sha_int = int(maybe_sha, 16)
    except ValueError:
        return 0
    return 1

db = pymysql.connect("172.17.0.2","root","","selfieless" )
cursor = db.cursor()



@app.route('/')
def index():
    return render_template('Index.html'), 200

@app.route('/api/v1/users', methods = ['GET'])
def list_user():
    if request.method == 'GET':
        r=requests.get('http://52.21.133.199:80/api/v1/categories')
        if r.status_code==500:
           return r.status_code        
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        cursor.execute("SELECT users.username from users")

        cat = cursor.fetchall()

        if(cat):
           json_data=[]
           for result in cat:
               json_data.append(str(result[0]))

           response = app.response_class(response=json.dumps(json_data), status=200, mimetype='application/json')
           return response

        else:
            response = app.response_class(response=json.dumps({}), status=204, mimetype='application/json')
            return response
    else:
        r=requests.get('http://52.21.133.199:80/api/v1/categories')
        if r.status_code==500:
           return r.status_code        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
        return response

@app.route('/api/v1/users', methods = ['POST'])
def add_user():
    if request.method == 'POST':
        r=requests.get('http://52.21.133.199:80/api/v1/categories')
        if r.status_code==500:
           return r.status_code        
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        content = request.get_json()
        username = content['username']
        username1 = str(username)
        password =  content['password']
        a=is_sha1(password)
        if(a==0):
           response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
           return response
        query="SELECT username FROM users Where users.username = '%s'"%(username1)
        cursor.execute(query)

        results = cursor.fetchone()
        if(results):
            flag=0
            for row in results:
                if(row==username1):
                   flag=1
                   response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
                   return response
        else:
            sql = "INSERT INTO users VALUES('%s','%s')"%(username1,password)

            cursor.execute(sql)
            db.commit()
            response = app.response_class(response=json.dumps({}), status=201, mimetype='application/json')
            return response

    else:
         r=requests.get('http://52.21.133.199:80/api/v1/categories')
         if r.status_code==500:
            return r.status_code
         response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
         return response

@app.route('/api/v1/users/<username>', methods = ['DELETE'])
def remove_user(username):
    if request.method == 'DELETE':
       r=requests.get('http://52.21.133.199:80/api/v1/categories')
       if r.status_code==500:
          return r.status_code       
       fd=open("count.txt","r")
       fd.seek(0)
       temp=fd.read()
       count=int(temp)
       count+=1
       fd.close()
       fd=open("count.txt","w")
       fd.write(str(count))
       fd.close()
       if(username):
          sql="SELECT username FROM users where users.username = '%s'"%(username)
          cursor.execute(sql)
          results = cursor.fetchone()
          
          if(results):
             
             for row in results:
                 if(row==str(username)):
                    
                    sql2="DELETE FROM users where username = '%s'"% (username)
                    
                    cursor.execute(sql2)
                    db.commit()

                    response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')
                    return response
          else:
               response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
               return response
    else:
         r=requests.get('http://52.21.133.199:80/api/v1/categories')
         if r.status_code==500:
            return r.status_code        
         response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
         return response

if __name__ == '__main__':
   app.run(host='0.0.0.0',port="80")
