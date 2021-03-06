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
    pid = int(server_pid)
    try:
        if sys.platform.startswith('win'):
            print('TASKKILL /PID %s' % pid)
            print(QProcess.execute('TASKKILL /PID %s' % pid))
        else:
            os.kill(pid,  11)
    except:
        print('pid %s killed already' % pid)

p = QProcess()
p.setWorkingDirectory(root_folder)

http_server = ('SimpleHTTPServer', 'http.server')[sys.version_info.major == 3]
args = ('-m', http_server, str(port))

exec_dir = os.path.dirname(sys.executable)
executable = os.path.join(exec_dir, ('python2', 'python-qgis.bat')[sys.platform.startswith('win')])

state, pid = p.startDetached(executable, args, root_folder)

print ("webserver process started at pid %s, status %s" % (pid, state))

if state:
    s.setValue("X3DProcessing/server_pid", pid)
    iface.messageBar().pushMessage("X3D Processing","webserver process started serving %s from port: %s" % (root_folder, port), level=QgsMessageBar.INFO,duration=10)
    
    
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