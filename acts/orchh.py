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
def fault_tolerance():
    global l
    global l1
    
    while True:
          if(len(l)>0):
              for i in range(len(l)):
                  print(l[i])
                  try:
                      time.sleep(0.5)
                      r=requests.get("http://52.21.133.199:"+str(l[i])+"/api/v1/_health")
                      if r.status_code==500:
                         print("oops") 
                         l1[i].kill()
                         #del l1[i]
                         b=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , l[i]) } , privileged=False, detach=True)
                         #if(len(l)==0):
                         #  l1.append(b)
                         #else:
                         l1[i]=b
                         print("fixed")
                  except:
                      pass
          time.sleep(0.5)
        
def scale():
    global count
    global l
    global l1
    while True:
          if count>=1:
              time.sleep(120)
              count-=1
              if count<20:
                 if(len(l)>1):
                   for i in range(1,len(l)):
                       print("kill")
                       g=l1[i]
                       
                       g.kill()
                       del l[i]
                       del l1[i]
                 else:
                     pass
              elif(count>=20 and count<40):     
                   if(len(l)>2):
                      for i in range(2,len(l)):
                          print("kill")
                          g=l1[i]
                          
                          g.kill()
                          del l[i]
                          del l1[i]
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
                          del l[i]
                          del l1[i]
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
                          del l[i]
                          del l1[i]
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
                          del l[i]
                          del l1[i]
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
                          del l[i]
                          del l1[i]
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
                          del l[i]
                          del l1[i]
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
                          del l[i]
                          del l1[i]
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
                          del l[i]
                          del l1[i]
                   elif(len(l)<9):
                       j=9-len(l)
                       for i in range(j):
                           g=l[-1]+1
                           l.append(g)
                           b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                           l1.append(b2)
                   else:
                       pass          
              elif(count>=180):     
                      
                   if(len(l)<10):
                     j=10-len(l)
                     for i in range(j):
                         g=l[-1]+1
                         l.append(g)
                         b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('0.0.0.0' , g) } , privileged=False, detach=True)
                         l1.append(b2)
                   else:
                       pass                         
              count=0
              
              
#response = app.response_class(response=json.dumps({obj}), status=response.status_code, mimetype='application/json')
#return response              
#c = docker.from_env()
#b1=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , 8000) } , privileged=False, detach=True)

def handle1(site,path):   
   if(count<20):     
     m=count%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response
   elif(count>=20 and count<40):
     m=(count-20)%len(l)
     url = site+str(l[m])+path
     
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response  
   elif(count>=40 and count<60):
     m=(count-40)%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response
   elif(count>=60 and count<80):
     m=(count-60)%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response
   elif(count>=80 and count<100):
     m=(count-80)%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response
   elif(count>=100 and count<120):
     m=(count-100)%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response
   elif(count>=120 and count<140):
     m=(count-120)%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response
   elif(count>=140 and count<160):
     m=(count-140)%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response 
   elif(count>=160 and count<180):
     m=(count-160)%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response
   elif(count>=180):
     m=(count-180)%len(l)
     url = site+str(l[m])+path
     response = requests.get(url = url)
     try:
        return jsonify(response.json()),response.status_code                
     except:
        response = app.response_class(response=json.dumps({}), status=response.status_code, mimetype='application/json')
        return response
    
def handle2(site,path):
   if(count<20):   
     m=count%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)     
     return jsonify(response.json()),response.status_code
   elif(count>=20 and count<40):
     m=(count-20)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers) 
     return jsonify(response.json()),response.status_code  
   elif(count>=40 and count<60):
     m=(count-40)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
   elif(count>=60 and count<80):
     m=(count-60)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code  
   elif(count>=80 and count<100):
     m=(count-80)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
   elif(count>=100 and count<120):
     m=(count-100)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code 
   elif(count>=120 and count<140):
     m=(count-120)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
   elif(count>=140 and count<160):
     m=(count-140)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code  
   elif(count>=160 and count<180):
     m=(count-160)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
   elif(count>=180):
     m=(count-180)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
 
def handle3(site,path):
   if(count<20): 
     m=count%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)     
     return jsonify(response.json()),response.status_code
   elif(count>=20 and count<40):
     m=(count-20)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers) 
     return jsonify(response.json()),response.status_code  
   elif(count>=40 and count<60):
     m=(count-40)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
   elif(count>=60 and count<80):
     m=(count-60)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code  
   elif(count>=80 and count<100):
     m=(count-80)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
   elif(count>=100 and count<120):
     m=(count-100)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code 
   elif(count>=120 and count<140):
     m=(count-120)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
   elif(count>=140 and count<160):
     m=(count-140)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code  
   elif(count>=160 and count<180):
     m=(count-160)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
   elif(count>=180):
     m=(count-180)%len(l)
     url = site+str(l[m])+path
     data = json.loads(request.data)
     headers = {'content-type': 'application/json'}
     response = requests.post(url = url,data = data,headers = headers)
     return jsonify(response.json()),response.status_code
 
#def handle
     
@app.route('/api/v1/acts', methods=['POST'])
def create_act():
    global count
    count+=1
    r=handle2("http://52.21.133.199:","/api/v1/acts")
    return r
@app.route('/api/v1/categories/<categoryName>/acts?start=<startRange>&end=<endRange>', methods = ['GET'])
def range_actss():
    url="http://52.21.133.199:"+str(l[m])+'/api/v1/categories/'+str(categoryName)+"/acts?="+str(start)+"&"+"end="+str(end)
    start = request.args.get('start')
    end = request.args.get('end')    
    payload={'startRange':start,'endRange':end}
    response = requests.get(url = url, params = payload)
    return jsonify(response.json()),response.status_code
	

@app.route('/api/v1/categories', methods = ['GET'])
def list_cat(): 
    global count
    count+=1 
    r=handle1("http://52.21.133.199:","/api/v1/categories")
    return r
@app.route('/api/v1/categories', methods = ['POST'])
def add_cat(): 
    global count
    count+=1 
    r=handle1("http://52.21.133.199:","/api/v1/categories")
    return r 

@app.route('/api/v1/categories/<categoryName>', methods = ['DELETE'])
def del_cat():
    global count
    count+=1
    r=handle2("http://52.21.133.199:","/api/v1/categories/<categoryName")
    return r  

@app.route('/api/v1/categories/<categoryName>/acts', methods = ['GET'])
def acts_per_cat():
    global count
    count+=1
    r=handle1("http://52.21.133.199:","/api/v1/categories/<categoryName>/acts")
    return r

@app.route('/api/v1/categories/<categoryName>/acts/size', methods = ['GET'])
def acts_size_per_cat():
    global count
    count+=1
    r=handle1("http://52.21.133.199:","/api/v1/categories/<categoryName>/acts/size")    
    return r

@app.route('/api/v1/categories/<categoryName>/acts?start=<startRange>&end=<endRange>', methods = ['GET'])
def range_acts():
    global count
    count+=1
    r=handle1("http://52.21.133.199:","/api/v1/categories/<categoryName>/acts?start=<startRange>&end=<endRange>")
    return r
@app.route('/api/v1/acts/upvote', methods = ['POST'])
def upvote_acts():
    global count
    count+=1
    r=handle2("http://52.21.133.199:","/api/v1/acts/upvote")
    return r   	 
@app.route('/api/v1/acts/<actid>', methods = ['DELETE'])
def del_actid():
    global count
    count+=1
    r=handle2("http://52.21.133.199:","/api/v1/acts/<actid>")
    return r
@app.route('/api/v1/acts/count', methods = ['GET'])
def count_acts():
    global count
    count+=1
    r=handle1("http://52.21.133.199:","/api/v1/acts/count")
    return r
@app.route('/api/v1/_crash', methods = ['POST'])
def crash():
    r=handle2("http://52.21.133.199:","/api/v1/_crash")    
    return r
@app.route('/api/v1/_health', methods = ['GET'])
def health():
    r=handle1("http://52.21.133.199:","/api/v1/_health")
    return r
if __name__ == '__main__':
    t1 = threading.Thread(target=fault_tolerance) 
    t2 = threading.Thread(target=scale) 
    t1.start() 
    t2.start() 
    app.run(host='0.0.0.0', port=80)
    