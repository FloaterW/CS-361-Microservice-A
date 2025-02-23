import zmq

def request_quote():
    """
    Sends a request to the microservice and prints the received quote.
    Handles errors gracefully if the server is unavailable.
    """
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    try:
        socket.connect("tcp://localhost:5555")
    except Exception as e:
        print(f"Error: Could not connect to server. Make sure the microservice is running. ({e})")
        return  # Exit the function

    while True:
        user_input = input("Press Enter to get a quote, or type 'exit' to quit: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break  # Exit loop

        try:
            socket.send_string("request_quote")  # Send request
            quote = socket.recv_string()  # Receive response
            print(f"Received Quote: {quote}")
        except Exception as e:
            print(f"Error: Could not communicate with the server. ({e})")
            break  # Exit the loop if an error occurs

if __name__ == "__main__":
    request_quote()
