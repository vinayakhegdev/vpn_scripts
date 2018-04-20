#!/usr/bin/env python

import sys
import os
import subprocess
import json

def cloud_start_vpn_server(arg_dict={}):
    cmd="/usr/local/cloud/start_vpn_server -d "+arg_dict["share"]+" -g "+arg_dict["public_ip"]+" -l "+arg_dict["logfile"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_start_vpn_bridge(arg_dict={}):
    cmd="/usr/local/cloud/start_vpn_bridge -d "+arg_dict["share"]+" -g "+arg_dict["public_ip"]+" -l "+arg_dict["logfile"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_start_dhcp_server(arg_dict={}):
    cmd="/usr/local/cloud/start_dhcp_server -d "+arg_dict["share"]+" -i "+arg_dict["container_image"]+" -l "+arg_dict["logfile"]+" -s "+arg_dict["subnet"]+" -n "+arg_dict["netmask"]+" -a "+arg_dict["range_start"]+" -z "+arg_dict["range_end"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_start_dhcp_relay(arg_dict={}):
    cmd="/usr/local/cloud/start_dhcp_relay -d "+arg_dict["share"]+" -g "+arg_dict["ip"]+" -i "+arg_dict["container_image"]+" -l "+arg_dict["logfile"]+" -s "+arg_dict["subnet"]+" -n "+arg_dict["netmask"]+" -v "+arg_dict["vlan"]+" -c "+arg_dict["cust_id"]+" -a "+arg_dict["range_start"]+" -z "+arg_dict["range_end"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_restart_vpn_bridge(arg_dict={}):
    cmd="/usr/local/cloud/restart_vpn_bridge -d "+arg_dict["share"]+" -g "+arg_dict["public_ip"]+" -l "+arg_dict["logfile"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_restart_vpn_server(arg_dict={}):
    cmd="/usr/local/cloud/restart_vpn_server -d "+arg_dict["share"]+" -g "+arg_dict["public_ip"]+" -l "+arg_dict["logfile"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_restart_dhcp_server(arg_dict={}):
    cmd="/usr/local/cloud/restart_dhcp_server -d "+arg_dict["share"]+" -i "+arg_dict["container_name"]+" -l "+arg_dict["logfile"]+" -s "+arg_dict["subnet"]+" -n "+arg_dict["netmask"]+" -a "+arg_dict["range_start"]+" -z "+arg_dict["range_end"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_restart_dhcp_relay(arg_dict={}):
    cmd="/usr/local/cloud/restart_dhcp_relay -d "+arg_dict["share"]+" -g "+arg_dict["public_ip"]+" -i "+arg_dict["container_name"]+" -l "+arg_dict["logfile"]+" -s "+arg_dict["subnet"]+" -n "+arg_dict["netmask"]+" -v "+arg_dict["vlan"]+" -c "+arg_dict["cust_id"]+" -a "+arg_dict["range_start"]+" -z "+arg_dict["range_end"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_add_nic(arg_dict={}):
    cmd="/usr/local/cloud/add_nic -d "+arg_dict["share"]+" -p "+arg_dict["interface"]+" -i "+arg_dict["container_image"]+" -l "+arg_dict["logfile"]+" -g "+arg_dict["ip"]+" -v "+arg_dict["vlan"]+" -s "+arg_dict["subnet"]+" -n "+arg_dict["netmask"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def cloud_allow_vlan(arg_dict={}):
    cmd="/usr/local/cloud/allow_vlan_trunks -d "+arg_dict["share"]+" -v "+arg_dict["vlan"]+" -l "+arg_dict["logfile"]
    os.system(cmd)
    cmd="cat "+arg_dict["share"]+"/"+"logs/status.txt"
    ob=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    status=ob.communicate()
    j_status=json.loads(status[0])
    return j_status

def create_bridge():
   cmd="ovs-vsctl add-br ovs-br1"
   os.system(cmd)
