# Takeaway
# Running the producer API (Post)
Clone the repository. <br />
Cd into the directory <br />
Run below command <br />
docker-compose up -d <br />
Once the compose is completes, you can make a POST request by running below command.<br />
curl -d "message=Hello, World." -X POST http://localhost:5000/send <br />

# Running consumer API (Get) to recieve messages. <br />
Open a second terminal window and run the below command <br />
docker exec -it flask-api python receive.py <br />
This will print out the messages recieved on the queue. <br />

# Security Concerns <br />
1) Inter dependency of containers, since one container is dependent on another, so chances are one container getting compromised can lead to other containers also getting compromised.<br />
2) Unreliable image source.<br />
3) Host system getting compromised, since docker shares the underlying kernel of the host, chances are if host system gets compromised via say a kernel exploit, the attacker can then also exploit the running containers as well.<br /> 

# Performance Concerns <br />
1) Scaling issue with the current setup, since we are not using any orchestration with this setup like swarm or kubernetes, the system would have scaling and auto healing issues and would not be able to support large number of requests.<br />
2) As mentioned above the system is not auto healing.

