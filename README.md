# CS-361-Microservice-A  
## Microservice: Quote Provider  

## Communication Contract  
This microservice provides random quotes upon request. The client program can request a quote, and the microservice retrieves it from `quotes.txt` (or default quotes if the file is missing).  

## How to Request Data  
To request data from the microservice, send the following request:  

**Request:**  
```python
socket.send_string("request_quote")
```

## How to Receive Data  
To receive data from the microservice, handle the response like this:  

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

### Using the Microservice in Your Own Program  
Once the microservice is running, you can integrate it into your own program by sending a request and receiving a response as shown in the examples above.  

Your program should:  
1. **Connect to the microservice using ZeroMQ.**  
2. **Send the request** (`"request_quote"`) using `socket.send_string()`.  
3. **Wait for a response** and process the received quote.  

The microservice will return a randomly selected quote, which your program can then display or use as needed.  

## UML Sequence Diagram  
Below is a UML sequence diagram illustrating the request-response process:  
![image](https://github.com/user-attachments/assets/f733e2f9-8174-4f8f-8069-fae7e36d3044)
