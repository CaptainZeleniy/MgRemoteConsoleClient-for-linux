#! /usr/bin/python
# coding: latin-1

import elementtree.ElementTree as ET  ###INSTALL is required###
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='MRemoteNG XML Parser')
parser.add_argument('--list', '-l', action='store_true', help='List Available Connections')
parser.add_argument('--connect', '-c', nargs=1, help='Connect by number', type=int)
parser.add_argument('--remove', '-r', nargs=1, help='Remove by number', type=int)
parser.add_argument('--file', '-f',  nargs=1, help='Filename', type=str)
parser.add_argument('--add', '-a', nargs=4,help='Add new host (name, username, ip,type)',type=str)
parser.add_argument('--copysshkey', '-cp', action='store_true', help='Add keys to all hosts')

args = parser.parse_args()

global tree, name, hostname, protocol, username, port, i

if args.file:
    filename = str(args.file[0])
    tree = ET.parse(filename)
else:
   if os.path.isfile('confCons2.xml'):
      tree = ET.parse('confCons2.xml')
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
    #Parse confCons.xml from variable tree
    i = 0
    print color.BOLD+"    # :: Name :: Hostname :: Protocol :: Username :: Port "+color.END
    for node in tree.getiterator('Node'):
        name = node.get('Name')
        hostname = node.get('Hostname')
        protocol = node.get('Protocol')
        username = node.get('Username')
        port = node.get('Port')
        typec = node.get('Type')
        if typec == 'Connection':
        #if name and hostname:
            i += 1
            conninfo = '    %s :: %s :: %s :: %s :: %s :: %s' % (color.GREEN+color.BOLD+str(i)+color.END+color.END, name, color.BOLD+hostname+color.END, protocol, username, port)
            print conninfo.encode('utf-8')
        else:
            print color.RED + color.BOLD + 'Group: ' + name + color.END + color.END

def tree_connect():
      i = 0
      for node in tree.getiterator('Node'):
        name = node.get('Name')
        hostname = node.get('Hostname')
        protocol = node.get('Protocol')
        username = node.get('Username')
        port = node.get('Port')
        domain = node.get('Domain')
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
                         os.system ('rdesktop -g 1720x968  -k en-us %s -d %s' % (hostname, domain))
                     else:
                         os.system ('rdesktop -g 1720x968 -k en-us -u %s %s -d %s'  % (username, hostname, domain))

                 else:
                     print(" ~In this version only ssh2 and rdesktop")
            #else:
            #    print (" ~Connection number not found")
            #    break
def add_node():
    name = args.add[0]
    username = args.add[1]
    hostname = args.add[2]
    protocol = args.add[3]
    #ToDo variable "name" must be unique
    nodestr = '    <Node Name=\"%s\" Type=\"Connection\" Descr=\"\" Icon=\"mRemoteNG\" Panel=\"Главная\" Username=\"%s\" Domain=\"\" Password=\"\" Hostname=\"%s\" Protocol=\"%s\" PuttySession=\"Default Settings\" Port=\"22\" ConnectToConsole=\"False\" UseCredSsp=\"True\" RenderingEngine=\"IE\" ICAEncryptionStrength=\"EncrBasic\" RDPAuthenticationLevel=\"NoAuth\" LoadBalanceInfo=\"\" Colors=\"Colors16Bit\" Resolution=\"FitToWindow\" AutomaticResize=\"True\" DisplayWallpaper=\"False\" DisplayThemes=\"False\" EnableFontSmoothing=\"False\" EnableDesktopComposition=\"False\" CacheBitmaps=\"True\" RedirectDiskDrives=\"False\" RedirectPorts=\"False\" RedirectPrinters=\"False\" RedirectSmartCards=\"False\" RedirectSound=\"DoNotPlay\" RedirectKeys=\"False\" Connected=\"False\" PreExtApp=\"\" PostExtApp=\"\" MacAddress=\"\" UserField=\"\" ExtApp=\"\" VNCCompression=\"CompNone\" VNCEncoding=\"EncHextile\" VNCAuthMode=\"AuthVNC\" VNCProxyType=\"ProxyNone\" VNCProxyIP=\"\" VNCProxyPort=\"0\" VNCProxyUsername=\"\" VNCProxyPassword=\"\" VNCColors=\"ColNormal\" VNCSmartSizeMode=\"SmartSAspect\" VNCViewOnly=\"False\" RDGatewayUsageMethod=\"Never\" RDGatewayHostname=\"\" RDGatewayUseConnectionCredentials=\"Yes\" RDGatewayUsername=\"\" RDGatewayPassword=\"\" RDGatewayDomain=\"\" InheritCacheBitmaps=\"False\" InheritColors=\"False\" InheritDescription=\"False\" InheritDisplayThemes=\"False\" InheritDisplayWallpaper=\"False\" InheritEnableFontSmoothing=\"False\" InheritEnableDesktopComposition=\"False\" InheritDomain=\"False\" InheritIcon=\"False\" InheritPanel=\"False\" InheritPassword=\"False\" InheritPort=\"False\" InheritProtocol=\"False\" InheritPuttySession=\"False\" InheritRedirectDiskDrives=\"False\" InheritRedirectKeys=\"False\" InheritRedirectPorts=\"False\" InheritRedirectPrinters=\"False\" InheritRedirectSmartCards=\"False\" InheritRedirectSound=\"False\" InheritResolution=\"False\" InheritAutomaticResize=\"False\" InheritUseConsoleSession=\"False\" InheritUseCredSsp=\"False\" InheritRenderingEngine=\"False\" InheritUsername=\"False\" InheritICAEncryptionStrength=\"False\" InheritRDPAuthenticationLevel=\"False\" InheritLoadBalanceInfo=\"False\" InheritPreExtApp=\"False\" InheritPostExtApp=\"False\" InheritMacAddress=\"False\" InheritUserField=\"False\" InheritExtApp=\"False\" InheritVNCCompression=\"False\" InheritVNCEncoding=\"False\" InheritVNCAuthMode=\"False\" InheritVNCProxyType=\"False\" InheritVNCProxyIP=\"False\" InheritVNCProxyPort=\"False\" InheritVNCProxyUsername=\"False\" InheritVNCProxyPassword=\"False\" InheritVNCColors=\"False\" InheritVNCSmartSizeMode=\"False\" InheritVNCViewOnly=\"False\" InheritRDGatewayUsageMethod=\"False\" InheritRDGatewayHostname=\"False\" InheritRDGatewayUseConnectionCredentials=\"False\" InheritRDGatewayUsername=\"False\" InheritRDGatewayPassword=\"False\" InheritRDGatewayDomain=\"False\" />\n</Connections>' % (name, username, hostname, protocol)

    f = open("confCons2.xml","r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        #Remove last string from XML 0_o Velosiped
        if i != "</Connections>":
            f.write(i)
        else:
            break
    f.write(nodestr)
    f.truncate()
    f.close()

#Remove connection string from XML file
def remove_node():
    i = 0
    number = args.remove[0]
    iter = root.getiterator('Node')

    for node in iter:

         name = node.get('Name')
         hostname = node.get('Hostname')
         typec = node.get('Type')

         if typec == 'Connection':
            i+=1
            if int(number) == int(i):
                f = open("confCons2.xml","r+")
                d = f.readlines()
                f.seek(0)
                for a in d:
                    if hostname not in a and name not in a:
                         f.write(a)

                f.truncate()
                f.close
                print 'Remove ' + name.encode('utf-8') + ' ' + hostname.encode('utf-8') + ' from list' + typec
                    #tree.write('confCons2.xml')
def copy_ssh_key():
    i = 0
    print color.BOLD+"    # :: Name :: Hostname :: Protocol :: Username :: Port "+color.END
    for node in tree.getiterator('Node'):
        name = node.get('Name')
        hostname = node.get('Hostname')
        protocol = node.get('Protocol')
        username = node.get('Username')
        port = node.get('Port')
        typec = node.get('Type')
        if typec == 'Connection':
            if protocol == 'SSH2':
                os.system ('ssh-copy-id %s@%s -p %s'  % (username, hostname, port))
                i += 1
                conninfo = '    %s :: %s :: %s :: %s :: %s :: %s' % (color.GREEN+color.BOLD+str(i)+color.END+color.END, name, color.BOLD+hostname+color.END, protocol, username, port)
                print conninfo.encode('utf-8')
        

if args.list:
        tree_parser_list()
        exit()
if args.connect:
        tree_connect()
        exit()
if args.add:
        add_node()
        exit()
if args.remove:
        remove_node()
        exit()
if args.copysshkey:
        copy_ssh_key()
        exit()
else:
    tree_parser_list()
