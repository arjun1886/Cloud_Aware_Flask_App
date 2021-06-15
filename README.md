# Cloud_Aware_Flask_App

This is the backend for a cloud based web application, which enables people to upload samaritan acts.

The application consists of two containers which are REST Api services- 

1. Container 1 handles user related requests.
2. Container 2 handles requests regarding acts which users want to interact with or create.
3. An orchestrator service was written which handles load balancing, fault tolerance and auto scaling. When a container crashes, it is automatically restarted and when the number of requests increases beyond a threshold, new containers serving the same requests are created, if the number of requests decreases beyond a threshold, the excess containers are killed. Requests are forwarded in a round-robin way to these containers.

Built the backend using Flask and MySQL using REST API’s which is packaged as separate aforementioned docker containers. The service was deployed on AWS EC2 instances.
