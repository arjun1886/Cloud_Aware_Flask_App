# Cloud_Aware_Flask_App

This is the backend for a cloud based application, which enables people upload to samaritan acts.

The application consists of two containers which are REST Api services- 

1. Container 1 handles requests regarding acts which users want to interact with or create.
2. Container 2 handles user related requests. 
3. An orchestrator service was written which handles load balancing, fault tolerance and auto scaling. When a container crashes, it is automatically restarted and when the number of requests increase beyond a threshold, a new container serving the same requests is created. Requests are forwarded in a round-robin way to these containers.

Built the backend using Flask and MySQL using REST API’s which is packaged as separate aforementioned docker containers. The service was deployed on AWS.
