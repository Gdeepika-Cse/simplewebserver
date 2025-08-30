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