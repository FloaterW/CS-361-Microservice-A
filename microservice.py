import zmq
import random
import os

QUOTE_FILE = "quotes.txt"

DEFAULT_QUOTES = [
    "Believe in yourself and all that you are.",
    "Your only limit is your mind.",
    "Dream big and dare to fail.",
    "Push yourself because no one else is going to do it for you.",
    "Hardships often prepare ordinary people for an extraordinary destiny."
]

def load_quotes():
    """
    Loads quotes from the file if available; otherwise, uses default quotes.
    """
    if os.path.exists(QUOTE_FILE):
        with open(QUOTE_FILE, "r", encoding="utf-8") as file:
            quotes = [line.strip() for line in file if line.strip()]
            return quotes if quotes else DEFAULT_QUOTES
    return DEFAULT_QUOTES

def start_server():
    """
    Starts the ZeroMQ server that listens for quote requests.
    """
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    
    print("Quote microservice is running... Waiting for requests")
    
    while True:
        message = socket.recv_string()
        if message.lower() == "request_quote":
            quotes = load_quotes()
            quote = random.choice(quotes)
            socket.send_string(quote)

if __name__ == "__main__":
    start_server()