import docker
import threading
fd=open("count.txt","w")
fd.write("0")
fd.close()
c = docker.from_env()
b1=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , 8000) } , privileged=False, detach=True)
#b1=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': (127.0.0.1 , 8001) } , privileged=False, detach=True)
#b3=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': (127.0.0.1 , 8002) } , privileged=False, detach=True)
p=8000
l=[]
l.append(p)
l1=[]
l1.append(b1)
#b1.kill()
@app.route('/api/v1/categories',methods=['GET'])
def show_category_list():
   fd=open("count.txt","r")
   fd.seek(0)
   temp=fd.read()
   count=int(temp)
   count+=1
   fd=open("count.txt","w")
   fd.write(str(count))
   fd.close()
   if(count<20):
     
     url = "http://localhost:"+str(l[0])+"/api/v1/categories"
     response = requests.get(url)
     
     return jsonify(response.json()),response.status_code
   elif(count==20):
     url = "http://localhost:"+str(l[0])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b2=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
     l1.append(b2)
     return jsonify(response.json()),response.status_code  
     
	elif(count>20 and count<40)
     m=(count-20)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
   elif(count==40):
     m=(count-20)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b3=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
	  l1.append(b3)
     return jsonify(response.json()),response.status_code  
   elif(count>40 and count<60)
     m=(count-40)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
   elif(count==60):
     m=(count-40)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b4=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
	  l1.append(b4)
     return jsonify(response.json()),response.status_code
       
	elif(count>60 and count<80)
     m=(count-60)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
   elif(count==80):
     m=(count-60)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b5=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
	  l1.append(b5)
     return jsonify(response.json()),response.status_code  
   elif(count>80 and count<100)
     m=(count-80)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
   elif(count==100):
     m=(count-80)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b6=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
	  l1.append(b6)
     return jsonify(response.json()),response.status_code
   elif(count>100 and count<120)
     m=(count-100)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
   elif(count==120):
     m=(count-100)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b7=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
	  l1.append(b7)
     return jsonify(response.json()),response.status_code  
   elif(count>120 and count<140)
     m=(count-120)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
   elif(count==140):
     m=(count-120)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b8=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
	  l1.append(b8)
     return jsonify(response.json()),response.status_code
       
	elif(count>140 and count<160)
     m=(count-140)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
   elif(count==160):
     m=(count-140)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b9=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
	  l1.append(b9)
     return jsonify(response.json()),response.status_code  
   elif(count>160 and count<180)
     m=(count-160)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
   elif(count==180):
     m=(count-160)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     g=l[-1]+1
     b10=c.containers.run('123456arjun/acts:latest' , ports = {'80/tcp': ('127.0.0.1' , g) } , privileged=False, detach=True)
	  l1.append(b10)
     return jsonify(response.json()),response.status_code
   elif(count>180):
     m=(count-180)%len(l)
     url = "http://localhost:"+str(l[m])+"/api/v1/categories"
     response = requests.get(url)
     return jsonify(response.json()),response.status_code
     
@app.route('/api/v1/acts', methods=['POST'])
def create_act():

	url = "http://localhost:"+portno+"/api/v1/acts"
	data = json.loads(request.data)
	headers = {'content-type': 'application/json'}
	response = requests.post(url,data = data,headers = headers)
	return jsonify(response.json()), response.status_code

@app.route('/api/v1/categories', methods = ['POST'])
def create_cat():  
   url = "http://localhost:"+portno+"/api/v1/categories"
	data = json.loads(request.data)
	headers = {'content-type': 'application/json'}
	response = requests.post(url,data = data,headers = headers)
	return jsonify(response.json()), response.status_code

@app.route('/api/v1/categories/<categoryName>', methods = ['DELETE'])
def del_cat():
   url = "http://localhost:"+portno+"/api/v1/categories/<categoryName"
	data = json.loads(request.data)
	headers = {'content-type': 'application/json'}
	response = requests.post(url,data = data,headers = headers)
	return jsonify(response.json()), response.status_code    

@app.route('/api/v1/categories/<categoryName>/acts', methods = ['GET'])
def acts_per_cat():
   url = "http://localhost:"+portno+"/api/v1/categories/<categoryName>/acts"
	response = requests.get(url)
	return jsonify(response.json()),response.status_code

@app.route('/api/v1/categories/<categoryName>/acts/size', methods = ['GET'])
def acts_size_per_cat():
   url = "http://localhost:"+portno+"/api/v1/categories/<categoryName>/acts/size"
	response = requests.get(url)
	return jsonify(response.json()),response.status_code    

@app.route('/api/v1/categories/<categoryName>/acts?start=<startRange>&end=<endRange>', methods = ['GET'])
def range_acts():
   url = "http://localhost:"+portno+"/api/v1/categories/<categoryName>/acts?start=<startRange>&end=<endRange>"
	response = requests.get(url)
	return jsonify(response.json()),response.status_code

@app.route('/api/v1/acts/upvote', methods = ['POST'])
def range_acts():
   url = "http://localhost:"+portno+"/api/v1/acts/upvote"
   	data = json.loads(request.data)
	headers = {'content-type': 'application/json'}
	response = requests.post(url,data = data,headers = headers)
	return jsonify(response.json()), response.status_code

@app.route('/api/v1/acts/<actid>', methods = ['DELETE'])
def del_actid():
   url = "http://localhost:"+portno+"/api/v1/acts/<actid>"
   	data = json.loads(request.data)
	headers = {'content-type': 'application/json'}
	response = requests.post(url,data = data,headers = headers)
	return jsonify(response.json()), response.status_code

@app.route('/api/v1/acts/count', methods = ['GET'])
def count_acts():
   url = "http://localhost:"+portno+"/api/v1/acts/count"
	response = requests.get(url)
	return jsonify(response.json()),response.status_code

@app.route('/api/v1/_crash', methods = ['POST'])
def crash():
   url = "http://localhost:"+portno+"/api/v1/_crash"
   	data = json.loads(request.data)
	headers = {'content-type': 'application/json'}
	response = requests.post(url,data = data,headers = headers)
	return jsonify(response.json()), response.status_code    

@app.route('/api/v1/_health', methods = ['GET'])
def health():
   url = "http://localhost:"+portno+"/api/v1/_health"
	response = requests.get(url)
	return jsonify(response.json()),response.status_code
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)