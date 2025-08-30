# NAME: DEEPIKA G
# REG.NO: 212224040060
# EX01 Developing a Simple Webserver
## Date:30-08-25
## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.
## DESIGN STEPS:
## Step 1: 
HTML content creation.
## Step 2:
Design of webserver workflow.
## Step 3:
Implementation using Python code.
## Step 4:
Import the necessary modules.
## Step 5:
Define a custom request handler.
## Step 6:
Start an HTTP server on a specific port.
## Step 7:
Run the Python script to serve web pages.
## Step 8:
Serve the HTML pages.
## Step 9:
Start the server script and check for errors.
## Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
from http.server import HTTPServer, BaseHTTPRequestHandler
htmlcontent = '''
<!doctype html>
<html>
<head>
    <title>sample</title>
</head>
      <center><font color="red" face="arial" size="70">
        <br>List Of Protocols In TCP/IP Model</br>
   </font></center>
   <center><font color="orange" face="atlas" size="05">
   <br>Application Layer - HTTP, FTP, DNS, TELNET & SSH<br>
   <center><font color="lime" face="atlas" size="05">
   <br>Transport Layer - TCP & UDP<br>
   <center><font color="cyan" face="slider" size="05">
   <br>Network Layer - IPV4/IPV6<br>
   <center><font color="purple" face="slider" size="05">
   <br>Link Layer - Ethernet<br>
   </font>
<body>
<h1></h1>
</body>
</html>
'''
class ServerResponse(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(htmlcontent.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,ServerResponse)
httpd.serve_forever()

## OUTPUT:

<img width="1919" height="1116" alt="Screenshot 2025-08-30 132219" src="https://github.com/user-attachments/assets/afdaa5e5-4ae4-493d-91f9-1dd2fd346e1c" />

<img width="1919" height="850" alt="Screenshot 2025-08-30 131726" src="https://github.com/user-attachments/assets/1c02b220-f042-4d5f-828d-010e7b861145" />

## RESULT:
The program for implementing simple webserver is executed successfully.
