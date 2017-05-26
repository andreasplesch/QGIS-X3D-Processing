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
import os
from PyQt4.QtCore import QProcess, QSettings
from qgis.gui import QgsMessageBar
from qgis.utils import iface

#kill existing server
s = QSettings()
server_pid = s.value("X3DProcessing/server_pid")
if server_pid is not None:
    try:
        os.kill(int(server_pid), 15)
    except:
        print('killed already %s' % server_pid)

p = QProcess()
p.setWorkingDirectory(root_folder)

http_server = ('SimpleHTTPServer','http.server')[sys.version_info.major == 2]
args = ('-m', http_server, str(port))

state, pid= p.startDetached(sys.executable, args, root_folder)

print ("webserver process started at pid %s, status %s" % (pid, state))

if state:
    s.setValue("X3DProcessing/server_pid", pid)
    iface.messageBar().pushMessage("X3D Processing","webserver process started serving %s from port: %s" % (root_folder, port), level=QgsMessageBar.INFO,duration=5)
    
    
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