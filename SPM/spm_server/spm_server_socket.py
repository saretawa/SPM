import socket

class MultiConnectionServer:
    def __init__(self, host="127.0.0.1", port=555, max_connections=5):
        self.host = host
        self.port = port
        self.max_connections = max_connections
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start_server_socket(self):
        """Start the server and listen for connections."""
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.max_connections)
        print(f"Listening for multiple connections on port {self.port}...")
        self.accept_connections()

    def accept_connections(self):
        """Accept and handle incoming client connections."""
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection established with {client_address}")
            self.handle_client(client_socket, client_address)

    def handle_client(self, client_socket, client_address):
        """Handle communication with a connected client."""
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    print(f"Client {client_address} disconnected.")
                    break

                message = data.decode()
                print(f"Received from {client_address}: {message}")

                response = f"Server received: {message}"
                client_socket.send(response.encode())
            except ConnectionResetError:
                print(f"Connection with {client_address} was reset.")
                break

        client_socket.close()

if __name__ == "__main__":
    server = MultiConnectionServer()
    server.start_server_socket()