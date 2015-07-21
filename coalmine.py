import commands
import socket
import httplib
import urllib2
import os.path

def check_service_status(service):
    result = commands.getoutput('ps -A')
    if service == 'apache2':
        if 'apache2' in result:
            return True
        else:
            return False
    else:
        return False

def check_running_service_pid(service):
    payload = '''netstat -anp | grep %(svc)s | awk {'print $7}' | cut -d / -f 1''' % {'svc': service}
    result = commands.getoutput(payload)
    if len(result) == 0:
        return False
    else:
        return True, result

def check_remote_host_port(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))
        return True
    except socket.error, e:
        return False

def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None

def check_http_page(url):
    try:
        urllib2.urlopen(url)
        return True
    except urllib2.HTTPError, e:
        print(e.code)
        return False
    except urllib2.URLError, e:
        print(e.args)
        return False

def check_file_exists(file):
        return os.path.isfile(file)

