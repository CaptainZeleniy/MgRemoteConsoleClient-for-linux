import elementtree.ElementTree as ET  ###INSTALL is required###
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='MRemoteNG XML Parser')
parser.add_argument('--list', '-l', action='store_true',help='List Available Connections')
parser.add_argument('--connect', '-c', nargs=1, help='Connect by number', type=int)
parser.add_argument('--file', '-f',  nargs=1, help='Filename', type=str)
args = parser.parse_args()

global tree, name, hostname, protocol, username, port, i

if args.file:
    filename = str(args.file[0])
    tree = ET.parse(filename)
else:
   if os.path.isfile('/tmp/confCons.xml'):
      tree = ET.parse('/tmp/confCons.xml')
   else:
       print ('Error file confCons.xml not found, please put him into /tmp or use -f option')
       exit()

root = tree.getroot()
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def tree_parser_list():
    """Parse confCons.xml from variable tree
       =)"""
    i = 0
    print color.BOLD+"    # :: Name :: Hostname :: Protocol :: Username :: Port "+color.END
    for node in tree.getiterator('Node'):
        name = node.get('Name')
        hostname = node.get('Hostname')
        protocol = node.get('Protocol')
        username = node.get('Username')
        port = node.get('Port')
        if name and hostname:
            i += 1
            conninfo = '    %s :: %s :: %s :: %s :: %s :: %s' % (color.GREEN+color.BOLD+str(i)+color.END+color.END, name, color.BOLD+hostname+color.END, protocol, username, port)
            print conninfo.encode('utf-8')
        else:
            print color.RED + color.BOLD + 'This is group ' + name + color.END + color.END

def tree_connect():
      i = 0
      for node in tree.getiterator('Node'):
        name = node.get('Name')
        hostname = node.get('Hostname')
        protocol = node.get('Protocol')
        username = node.get('Username')
        port = node.get('Port')
        if name and hostname:
            i += 1
            if int(args.connect[0]) == i:
                 print (name, hostname, protocol,username)
                 if protocol == 'SSH2':
                     if not username:
                         os.system ('ssh %s -p %s'  % (hostname, port))
                         break
                     else:
                         os.system ('ssh %s@%s -p %s'  % (username, hostname, port))
                         break
                 elif  protocol == 'RDP':
                     if not username:
                         os.system ('rdesktop %s'  % (hostname))
                     else:
                         os.system ('rdesktop -u %s %s'  % (username, hostname))

                 else:
                     print(" ~In this version only ssh2 and rdesktop")
            #else:
            #    print (" ~Connection number not found")
            #    break


if args.list:
        tree_parser_list()
        exit()
if args.connect:
        tree_connect()
        exit()
else:
    print ("~ No Arg")
    print ("If script running without parameters it's show list of connections")
    print ("from /tmp/confCons.xml")
    print ("=========================================================")
    print ("=========================================================")
    print ("=========================================================")
    tree_parser_list()   
