from flask import Flask, render_template, request, jsonify
import hashlib
import base64
import binascii
import json
import pymysql
import datetime
import mysql.connector
from pathlib import Path

fd=open("count.txt","w")
fd.write("0")
fd.close()
count=0

app=Flask(__name__)


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
import requests
db = pymysql.connect("172.17.0.2","root","","selfieless" )
cursor = db.cursor()

@app.route('/api/v1/_count', methods = ['GET'])
def count_requests():
    if request.method == 'GET':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
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
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
        return response

@app.route('/api/v1/_count', methods = ['DELETE'])
def reset_requests():
    if request.method == 'DELETE':
       my_file = Path("countt.txt")
       if my_file.is_file():
          response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
          return response        
       fd=open("count.txt","w")
       fd.write("0")
       fd.close()
       response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')
       return response
    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
        return response


@app.route('/api/v1/categories', methods = ['GET'])
def listallcat():
    if request.method == 'GET':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        cursor.execute("SELECT categories.catname, COUNT(acts.actid) FROM categories,acts where categories.catname=acts.catname group by categories.catname")
        cat = cursor.fetchall()
        d={}
        if(cat):
           json_data=[]
           for result in cat:
               d[result[0]]=result[1]
           response = app.response_class(response=json.dumps(d), status=200, mimetype='application/json')
           return response
        else:            
            response = app.response_class(response=json.dumps({}), status=204, mimetype='application/json')
            return response
    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
        return response

#Add a category
@app.route('/api/v1/categories', methods = ['POST'])
def add_category():
    if request.method == 'POST':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response        
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
        cat = content[0]
        query="select catname from categories where catname='%s'"%(cat)
        cursor.execute(query)
        results=cursor.fetchone()
        if(results):
          for row in results:
              if(row==cat):
                 response=app.response_class(response=json.dumps({}), status=400, mimetype='application/json')

                 return response
        sql="INSERT INTO categories(catname) values('%s')"%(str(cat))
        cursor.execute(sql)
        db.commit()
        response = app.response_class(response=json.dumps({}), status=201, mimetype='application/json')
        return response
        #  return render_template('Signup.html'), 201
    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
        return response


@app.route('/api/v1/categories/<categoryName>', methods = ['DELETE'])
def remove_category(categoryName):
    if request.method == 'DELETE':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        if(categoryName):
            query="SELECT catname FROM categories where catname = '%s'"%(categoryName)
            cursor.execute(query)
            row = cursor.fetchone()
            jsonify(row)
            if(row):
                flag=0
                for i in range(len(row[0])):
                    if((row[0])[i]!=categoryName[i]):
                        flag=1
                        break
                if(flag==0):
                    sql1="SELECT acts.catname FROM acts where acts.catname = '%s'"%(categoryName)
                    cursor.execute(sql1)
                    cat = cursor.fetchone()
                    if(cat):
                       sql2="DELETE FROM acts where catname in (Select catname From categories WHERE catname = '%s')"%(categoryName)
                       cursor.execute(sql2)
                       db.commit()
                    sql3="DELETE FROM categories where catname = '%s'"%(categoryName)
                    cursor.execute(sql3)

                    db.commit()
                    response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')

            else:
                response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
    return response



@app.route('/api/v1/categories/<categoryName>/acts', methods = ['GET'])
def list_acts_cat(categoryName):
    if request.method == 'GET':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        if(len(request.args)==2):
            return no_acts_category_range(categoryName)
        if(categoryName):
            query="SELECT * from acts where acts.catname=(select categories.catname from categories where categories.catname = '%s') order by times desc"%(str(categoryName))
            cursor.execute(query)
            cat3= cursor.fetchall()
            if(cat3):
               cat1 = [dict(zip([col[0] for col in cursor.description], row)) for row in cat3]

               sql1="SELECT COUNT(*) FROM acts,categories WHERE acts.catname = categories.catname AND categories.catname = '%s'"%(categoryName)
               cursor.execute(sql1)
               cat4 = cursor.fetchone()
               if(cat4[0] > 100):
                   response = app.response_class(response=json.dumps({}), status=413, mimetype='application/json')
               else:
                   response = app.response_class(response=json.dumps(cat1), status=200, mimetype='application/json')

            else:
                response = app.response_class(response=json.dumps({}), status=204, mimetype='application/json')

    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
    return response



@app.route('/api/v1/categories/<categoryName>/acts/size', methods = ['GET'])
def list_no_acts_category(categoryName):
    if request.method == 'GET':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        if(categoryName):
            query="SELECT COUNT(acts.catname) FROM acts where acts.catname=(select  categories.catname from categories where categories.catname = '%s')"%(str(categoryName))

            cursor.execute(query)
            cat8 = cursor.fetchone()
            if(cat8[0]>=1):

                #cat1 = [dict(zip([col[0] for col in cursor.description], row)) for row in cat8]
                response = app.response_class(response=json.dumps(cat8), status=200, mimetype='application/json')

            else:
                response = app.response_class(response=json.dumps({}), status=204, mimetype='application/json')

    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
    return response

@app.route('/api/v1/categories/<categoryName>/acts?start=<startRange>&end=<endRange>', methods = ['GET'])
def no_acts_category_range(categoryName):
    if request.method == 'GET':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        
        query="SELECT * FROM acts where acts.catname='%s'"%(categoryName)
        cursor.execute(query)
        
        length=cursor.rowcount
        startRange=int(request.args.get('start'))
        endRange=int(request.args.get('end'))
        if(((endRange-startRange)+1)>100):
          response = app.response_class(response=json.dumps({}), status=413, mimetype='application/json')
          return response
        if(startRange >= 1 and endRange<=length):
            query="SELECT * FROM acts where acts.catname='%s' order by times desc"%(categoryName)
            cursor.execute(query)
            results = cursor.fetchall()
            d={}
            l=[]
            l1=[]
            b=[]
            if(results):
                for row in results:
                    b.append({"actid":row[0],"uname":row[1],"times":row[2],"votes":row[3],"caption":row[4],"catname":row[5],"imgb64":row[6]})
                
                b=b[startRange-1:endRange]
                response = app.response_class(response=json.dumps(b), status=200, mimetype='application/json')

                return response
            else:
                 response = app.response_class(response=json.dumps({}), status=204, mimetype='application/json')
                 return response
        else:
            response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
            return response
    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
        return response

@app.route('/api/v1/acts/upvote', methods = ['POST'])
def upvote_act():
    if request.method == 'POST':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        content1 = request.get_json()
        actid = int(content1[0])
        query="SELECT votes FROM acts WHERE actid = '%s'"%(actid)
        cursor.execute(query)
        row = cursor.fetchone()
        if(row):
            votes = row[0] + 1
            votes = int(votes)
            sql1 = "UPDATE acts SET votes = '%s' WHERE actid = '%s'"%(votes, actid)
            cursor.execute(sql1)
            db.commit()
            response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')
        else:
            response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')

    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
    return response


@app.route('/api/v1/acts/<actid>', methods = ['DELETE'])
def remove_act(actid):
    if request.method == 'DELETE':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
        fd=open("count.txt","r")
        fd.seek(0)
        temp=fd.read()
        count=int(temp)
        count+=1
        fd.close()
        fd=open("count.txt","w")
        fd.write(str(count))
        fd.close()
        actid = int(actid)
        query="SELECT actid FROM acts WHERE actid = '%s'"%(actid)
        cursor.execute(query)
        id = cursor.fetchone()
        if(id):
           if(id[0] == actid):
              sql1="DELETE FROM acts where actid = '%s'"%(actid)
              cursor.execute(sql1)
              db.commit()
              response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')
        else:
            response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')

    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
    return response
def is_content(a):
    try:
        upvote=int(a)
        return 1
    except KeyError:
          return 0

@app.route('/api/v1/acts', methods = ['POST'])
def upload_act():

    if request.method == 'POST':
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response
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
        actid=content['actId']
        cat = content['categoryName']
        caption=content['caption']
        username=content['username']
        times=content['timestamp']
        imgb64=content['imgB64']
        imgb64=str(imgb64)
        #upvote=is_content(content['upvote'])
        if(len(content)>6):
        #if(upvote==1):
           response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
           return response
        votes=0
        query="select actid from acts where acts.actid='%s'"%(int(actid))
        cursor.execute(query)
        actcheck=cursor.fetchone()
        if(actcheck is not None):

            response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
            return response

        base=isBase64(imgb64)

        if(base==0):
           response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
           return response
        r=requests.get('http://3.215.82.121:80/api/v1/users')
        if r.status_code==204:
           response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
           return response
        users=r.json()
        if users is None:
           pass
        elif username not in users:
           response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
           return response


        query2="select * from categories where catname='%s'"%(cat)
        cursor.execute(query2)
        catt=cursor.fetchone()


        if(catt is None):
           response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
           return response

        if(date(times)):
            response = app.response_class(response=json.dumps({}), status=400, mimetype='application/json')
            return response

        cat3 = "INSERT INTO acts (actid,uname,times,votes,caption,catname,imgb64) VALUES ('%d','%s','%s','%s','%s','%s','%s')"%(int(actid),username,times,votes,caption,cat,imgb64)
        cursor.execute(cat3)
        db.commit()
        response = app.response_class(response=json.dumps({}), status=201, mimetype='application/json')

    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
    return response

@app.route('/api/v1/acts/count', methods = ['GET'])
def total_acts():
    if request.method == 'GET':
       my_file = Path("countt.txt")
       if my_file.is_file():
          response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
          return response
       fd=open("count.txt","r")
       fd.seek(0)
       temp=fd.read()
       count=int(temp)
       count+=1
       fd.close()
       fd=open("count.txt","w")
       fd.write(str(count))
       fd.close()
       sql="SELECT count(*) from acts"
       cursor.execute(sql)
       a=cursor.fetchone()
       l=[]
       for row in a:
           l.append(row)
       response = app.response_class(response=json.dumps(l), status=200, mimetype='application/json')
       return response
    else:
        my_file = Path("countt.txt")
        if my_file.is_file():
           response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
           return response        
        response = app.response_class(response=json.dumps({}), status=405, mimetype='application/json')
        return response

@app.route('/api/v1/_health', methods = ['GET'])
def health():
    my_file = Path("countt.txt")
    if my_file.is_file():
       response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
       return response
    r=requests.get('http://3.215.82.121:80/api/v1/users')
    r1=requests.get('http://52.21.133.199:80/api/v1/categories')
    if r.status_code!=500 and r1.status_code!=500:
       response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')
       return response 
    else:
        response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')
        return response

@app.route('/api/v1/_crash', methods = ['POST'])
def crash():
    my_file = Path("countt.txt")
    if my_file.is_file():
       response = app.response_class(response=json.dumps({}), status=500, mimetype='application/json')
       return response    
    else:
       fd=open("countt.txt","w")
       fd.write("0")
       fd.close()
       response = app.response_class(response=json.dumps({}), status=200, mimetype='application/json')
       return response

if __name__ == '__main__':
   app.run(host='0.0.0.0',port="80")
