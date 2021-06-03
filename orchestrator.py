import docker
import threading
from flask import Flask, render_template, request, jsonify
import json
import time
import requests


app=Flask(__name__)
count=0
l=[]
l1=[]
c = docker.from_env()
b1=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , 8000) } , privileged=False, detach=True)
l.append(8000)
l1.append(b1)
URL="http://0.0.0.0:"
def restart_cont(a):

    b=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , a) } , privileged=False, detach=True)
    return b
def fault_tolerance():
      global l
      global l1
      global c
      while True:
          #time.sleep(1)
          for i in range(len(l)):
               url = URL+str(l[i])+'/api/v1/_health'
               try:
                   r= requests.get(url = url)

                   if r.status_code==500:

                      l1[i].kill()
                      print(l1[i])

                      b=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , l[i]) } , privileged=False, detach=True)

                      l1[i]=b
                      print(b)
               except:
                   print("waiting")
          time.sleep(1)

def scale():
    global count
    global l
    global l1
    while True:
          if count>=1:
              time.sleep(120)
              print(count)
              if count<20:
                 if(len(l)>1):
                   for i in range(1,len(l)):
                       print("kill")
                       g=l1[i]

                       g.kill()
                   l=l[:1]
                   l1=l1[:1]
                 else:
                     pass
              elif(count>=20 and count<40):
                   if(len(l)>2):
                      for i in range(2,len(l)):
                          print("kill")
                          g=l1[i]

                          g.kill()
                      l=l[:2]
                      l1=l1[:2]
                   elif(len(l)<2):
                       print("create")
                       g=l[-1]+1
                       l.append(g)
                       b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                       l1.append(b2)
                   else:
                       pass
              elif(count>=40 and count<60):
                   if(len(l)>3):
                      for i in range(3,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:3]
                      l1=l1[:3]
                   elif(len(l)<3):
                       print("createeee")
                       j=3-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=60 and count<80):
                   if(len(l)>4):
                      for i in range(4,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:4]
                      l1=l1[:4]
                   elif(len(l)<4):
                       j=4-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=80 and count<100):
                   if(len(l)>5):
                      for i in range(5,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:5]
                      l1=l1[:5]
                   elif(len(l)<5):
                       j=5-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=100 and count<120):
                   if(len(l)>6):
                      for i in range(6,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:6]
                      l1=l1[:6]
                   elif(len(l)<6):
                       j=6-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=120 and count<140):
                   if(len(l)>7):
                      for i in range(7,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:7]
                      l1=l1[:7]
                   elif(len(l)<7):
                       j=7-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=140 and count<160):
                   if(len(l)>8):
                      for i in range(8,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:8]
                      l1=l1[:8]
                   elif(len(l)<8):
                       j=8-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=160 and count<180):
                   if(len(l)>9):
                      for i in range(9,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:9]
                      l1=l1[:9]
                   elif(len(l)<9):
                       j=9-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=180 and count<200):
                   if(len(l)>10):
                      for i in range(10,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:10]
                      l1=l1[:10]
                   elif(len(l)<10):
                       j=10-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=200 and count<220):
                   if(len(l)>11):
                      for i in range(11,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:11]
                      l1=l1[:11]
                   elif(len(l)<11):
                       j=11-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=220 and count<240):
                   if(len(l)>12):
                      for i in range(12,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:12]
                      l1=l1[:12]
                   elif(len(l)<12):
                       j=12-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=240 and count<260):
                   if(len(l)>13):
                      for i in range(13,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:13]
                      l1=l1[:13]
                   elif(len(l)<13):
                       j=13-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=260 and count<280):
                   if(len(l)>14):
                      for i in range(14,len(l)):
                          g=l1[i]

                          g.kill()
                      l=l[:14]
                      l1=l1[:14]
                   elif(len(l)<14):
                       j=14-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass
              elif(count>=280):
                   if(len(l)<15):
                       j=15-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass                   
          count=0





@app.route('/api/v1/categories',methods=['GET'])
def redirect_show_category_list():
   global count
   count+=1
   m=(count)%len(l)
   url = URL+str(l[m])+'/api/v1/categories'
   print(l1[m])
   print(count)
   response = requests.get(url = url)
   print(url)
   try:
       obj = response.json()
   except:
       obj = {}
   return jsonify(obj), response.status_code


@app.route('/api/v1/categories', methods=['POST'])
def redirect_add_category():
   global count
   count+=1
   m=(count)%len(l)
   url = URL+str(l[m])+'/api/v1/categories'
   print(l[m])
   data = json.dumps(json.loads(request.data))
   headers = {'content-type':'application/json'}
   response = requests.post(url = url, data = data, headers = headers)
   try:
           obj = response.json()
   except:
           obj = {}
   return jsonify(obj), response.status_code




@app.route('/api/v1/categories/<category>', methods=['DELETE'])
def redirect_remove_category(category):
   global count
   count+=1
   m=(count)%len(l)
   url = URL+str(l[m])+'/api/v1/categories/'+str(category)
   print(l1[m])
   response = requests.delete(url = url)
   try:
           obj = response.json()
   except:
           obj = {}

   return jsonify(obj), response.status_code


@app.route('/api/v1/categories/<category>/acts',methods=['GET'])
def redirect_show_category_acts(category):
   global count
   count+=1
   m=(count)%len(l)
   print(l1[m])
   qs = request.query_string
   if len(qs)==0:
           url = URL+str(l[m])+'/api/v1/categories/'+str(category)+'/acts'
   else:
           url = URL+str(l[m])+'/api/v1/categories/'+str(category)+'/acts?'+qs.decode("utf-8")
   response = requests.get(url = url)
   try:
           obj = response.json()
   except:
           obj = {}
   return jsonify(obj),response.status_code
@app.route('/api/v1/categories/<category>/acts/size',methods=['GET'])
def redirect_show_acts_size(category):
   global count
   count+=1
   m=(count)%len(l)
   print(l1[m])
   url = URL+str(l[m])+'/api/v1/categories/'+str(category)+'/acts/size'
   response = requests.get(url = url)
   try:
           obj = response.json()
   except:
           obj = {}
   return jsonify(obj),response.status_code



def handle1(site,path):
    global count
    m=(count)%len(l)
    print(l1[m])
    url = site+str(l[m])+path
    response = requests.get(url = url)
    try:
       return jsonify(response.json()),response.status_code
    except:
       response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
       return response

@app.route('/api/v1/_health', methods = ['GET'])
def health():
    r=handle1("http://0.0.0.0:","/api/v1/_health")

    return r

@app.route('/api/v1/acts/upvote',methods=['POST'])
def redirect_upvote_acts():
   global count
   count+=1
   m=(count)%len(l)
   print(l1[m])
   url = URL + str(l[m])+'/api/v1/acts/upvote'
   data = json.dumps(json.loads(request.data))
   headers = {'content-type':'application/json'}
   response = requests.post(url = url, data = data, headers = headers)
   try:
           obj = response.json()
   except:
           obj = {}

   return jsonify(obj), response.status_code


@app.route('/api/v1/acts/<actId>', methods=['DELETE'])
def redirect_delete_act(actId):
   global count
   count+=1
   m=(count)%len(l)
   print(l1[m])
   url = URL+str(l[m])+'/api/v1/acts/'+str(actId)
   response = requests.delete(url = url)
   try:
           obj = response.json()
   except:
           obj = {}

   return jsonify(obj), response.status_code


@app.route('/api/v1/acts', methods=['POST'])
def redirect_create_act():
   global count
   count+=1
   m=(count)%len(l)
   print(l1[m])
   url = URL + str(l[m])+'/api/v1/acts'
   data = json.dumps(json.loads(request.data))
   headers = {'content-type':'application/json'}
   response = requests.post(url = url, data = data, headers = headers)
   try:
           obj = response.json()
   except:
      obj = {}

   return jsonify(obj), response.status_code

@app.route('/api/v1/_crash', methods = ['POST'])
def crash():
   global count
   m=(count)%len(l)
   print(l1[m])
   url = URL + str(l[m])+'/api/v1/_crash'
   headers = {'content-type':'application/json'}
   response = requests.post(url = url, headers = headers)
   try:
           obj = response.json()
   except:
      obj = {}

   return jsonify(obj), response.status_code

@app.route('/api/v1/acts/count', methods = ['GET'])
def count_acts():
   global count
   count+=1
   m=(count)%len(l)
   print(l1[m])
   url = URL+str(l[m])+'/api/v1/acts/count'
   response = requests.get(url = url)
   try:
       obj = response.json()
   except:
       obj = {}
   return jsonify(obj), response.status_code

if __name__ == '__main__':
    t1 = threading.Thread(target=fault_tolerance)
    t2 = threading.Thread(target=scale)

    t1.daemon=True
    t2.daemon=True

    t1.start()
    t2.start()
    app.run(host='0.0.0.0', port=80)
