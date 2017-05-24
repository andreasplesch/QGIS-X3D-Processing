'''
QGIS Processing script
(c) 2017 Andreas Plesch
launch webserver in background with given folder as root
'''
##X3D=group
##launch_webserver=name
##root_folder=folder
##port=number 8000
##pid=output number
'''
import os
import SimpleHTTPServer
import SocketServer
import threading
'''
import sys
from PyQt4.QtCore import QProcess

p = QProcess()
p.setWorkingDirectory(root_folder)

http_server = ('SimpleHTTPServer','http.server')[sys.version_info.major == 2]
args = ('-m', http_server, str(port))

state, pid= p.startDetached(sys.executable, args, root_folder)

print ("webserver process started at pid %s, status %s" % (pid, state))
if state: progress.setInfo("webserver process started serving from port:", port)
'''
def webserver (root, PORT):

    os.chdir(root)
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print ("serving at port", PORT)
    httpd.serve_forever()

t=threading.Thread(target=webserver, args=(root_folder, port))
t.daemon=False
t.start() # crashes
if t.isAlive(): progress.setInfo("webserver thread started ar port:", port)
'''