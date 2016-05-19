import elementtree.ElementTree as ET  ###INSTALL is required###
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='MRemoteNG XML Parser')
parser.add_argument('--list', '-l', action='store_true',help='List Available Connections')
parser.add_argument('--connect', '-c', nargs=1, help='Connect by number', type=int)
args = parser.parse_args()
tree = ET.parse('/tmp/confCons.xml')
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

global name, hostname, protocol, username, port, i

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
                         break
                     else:
                         os.system ('rdesktop -u %s %s'  % (username, hostname))
                         break

                 else:
                     print(" ~In this version only ssh2 and rdesktop")
                     break
            #else:
            #    print (" ~Connection number not found")
            #    break


if args.list:
        tree_parser_list()
if args.connect:
        tree_connect()
else:
    print ("~ No Arg")
