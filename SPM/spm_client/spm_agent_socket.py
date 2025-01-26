import socket

class Client_Socket:
    def __init__(self, server_ip="127.0.0.1", server_port=555):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_client_socket(self):
        """initiate connection to the server."""
        self.connect_to_server()
        self.communicate()
        self.close_connection()

    def connect_to_server(self):
        """Connect to the server."""
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            print(f"Connected to server at {self.server_ip}:{self.server_port}")
        except ConnectionRefusedError:
            print(f"Failed to connect to server at {self.server_ip}:{self.server_port}")

    def communicate(self):
        """Send and receive messages to/from the server."""
        while True:
            message = input('Send Message or type exit to exit: ')
            if message.lower() == 'exit':
                break

            self.client_socket.send(message.encode())
            print(f"Sent: {message}")

            response = self.client_socket.recv(1024)
            print(f"Received: {response.decode()}")

    def close_connection(self):
        """Close the connection to the server."""
        self.client_socket.close()
        print("Connection closed.")



def start_socket():
    client = Client_Socket()
    client.start_client_socket()
