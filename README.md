# Takeaway
# Running the producer API (Post)
Clone the repository.
Cd into the directory
Run below command
docker-compose up -d
Once the compose is completes, you can make a POST request by running below command.
curl -d "message=Hello, World." -X POST http://localhost:5000/send

# Running consumer API (Get) to recieve messages.
Open a second terminal window and run the below command
docker exec -it flask-api python receive.py
This will print out the messages recieved on the queue.
