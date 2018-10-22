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
