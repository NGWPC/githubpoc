import unittest
import threading
import requests
from simple_server.simple_server import SimpleServer


class TestSimpleHTTPRequestHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the server in a separate thread
        cls.server_thread = threading.Thread(target=cls.start_server)
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        # Stop the server thread
        if cls.server_thread.is_alive():
            cls.stop_server(cls.server_thread)

    def test_do_GET_hello(self):
        # Send a GET request to /hello
        response = requests.get('http://localhost:8000/hello')

        # Assert the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'world')

    def test_do_GET_not_found(self):
        # Send a GET request to a path that does not exist
        response = requests.get('http://localhost:8000/not_found')

        # Assert the response status code and content
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.text, 'Not Found')

    @classmethod
    def start_server(cls):
        # Start the server
        cls.server = SimpleServer()
        cls.server.start()

    @classmethod
    def stop_server(cls, server_thread):
        # Stop the server thread
        if server_thread.is_alive():
            cls.server.stop()
            server_thread.join(timeout=1)  # Wait for the thread to finish


if __name__ == "__main__":
    unittest.main()
