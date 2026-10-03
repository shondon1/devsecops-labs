"""
I'm just building a simple app that essentially greets the user and handles the greeting request.

"""

from http.server import BaseHTTPRequestHandler, HTTPServer

def greet(name: str) -> str:
    """
    Function to generate a greeting message for the user.

    Args:
        name (str): The name of the user.

    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"

class Handler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler to process incoming requests and respond with a greeting.
    """

    def do_GET(self):
        """
        Handle GET requests. Responds with a greeting message based on the 'name' query parameter.
        """
        
        # Generate the greeting message
        greeting_message = greet(name)
        body = greet("SHONDOOOONNNNNNN!!!").encode('utf-8')

        # Send response status code
        self.send_response(200)
        
        # Send headers
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # Write the greeting message to the response body
        self.wfile.write(body)
if __name__ == "__main__":
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()