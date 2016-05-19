import elementtree.ElementTree as ET
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='MRemoteNG XML Parser')
parser.add_argument('--list', '-l', action='store_true',help='List Available Connections')
parser.add_argument('--connect', '-c', nargs=1, help='Connect by number', type=int)
args = parser.parse_args()
tree = ET.parse('/tmp/confCons.xml')
root = tree.getroot()
global name, hostname, protocol, username, port, i

def tree_parser_list():
    """Parse confCons.xml from variable tree
       =)"""
    i = 0
    for node in tree.getiterator('Node'):
        name = node.get('Name')
        hostname = node.get('Hostname')
        protocol = node.get('Protocol')
        username = node.get('Username')
        port = node.get('Port')
        if name and hostname:
            i += 1
            conninfo = '    %i :: %s :: %s :: %s :: %s :: %s' % (i, name, hostname, protocol, username, port)
            print conninfo.encode('utf-8')
        else:
            print 'This is group ' + name

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
