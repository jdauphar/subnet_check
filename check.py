import pandas as pd
import numpy as np
import math
import os
import config

def ping(ip):
    response = os.system("fping " + ip + " > log.txt")
    up_and_running = 0
    return response == up_and_running
    
def extract_ips(filename):
    fields = ['IP Address', 'Name','MAC Address']
    
    df = pd.read_csv(filename, skipinitialspace=True, usecols=fields)
    df.columns = ['IP', 'Name','MAC']
    df.drop(df[df.MAC == np.nan].index, inplace=True)
    #df = remove_MACless(df)

    ips = df.values.tolist()
    
    return ips

def remove_MACless(df):
    df.drop(df[df.MAC == np.nan].index, inplace=True)
    return df

def concat_ips(ips):
    ip_str = ""
    for ip in ips:
        ip[0].strip()
        ip_str += ip[0] + " "
    return ip_str
        
def check(ip_str=None):
    if ip_str is None:
        ips = extract_ips(config.input_file)
        bad_ips=[]
        
        #for ip in ips:
        #    print(ip)
        ip_str = concat_ips(ips)
        os.system("fping " + ip_str + " > " + config.work_dir + "log.txt")
    else:
        os.system("fping " + ip_str + " > " + config.work_dir + "log.txt")
        
#main()
check()


