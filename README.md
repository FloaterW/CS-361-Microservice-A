# CS-361-Microservice-A

# Microservice: Quote Provider

## Communication Contract
This microservice provides random quotes upon request. The client program can request a quote, and the microservice retrieves it from `quotes.txt` (or default quotes if the file is missing).

## How to Request Data
To request a quote, the client sends the following request to the microservice:

**Request:**
```python
socket.send_string("request_quote")
```

## How to Receive Data
The microservice responds with a randomly selected quote:

**Response Example:**
```python
quote = socket.recv_string()
print(f"Received Quote: {quote}")
```

## Example Usage

### Running the Microservice
Start the microservice by running:
```bash
python microservice.py
```

### Running the Client
Once the microservice is running, start the client:
```bash
python client.py
```
The client will request a quote and display the received response.

## UML Sequence Diagram
Below is a UML sequence diagram illustrating the request-response process:

![image](https://github.com/user-attachments/assets/f733e2f9-8174-4f8f-8069-fae7e36d3044)
