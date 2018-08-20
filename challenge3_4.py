import re
from datetime import datetime

def open_parser(filename):
    with open(filename) as logfile:
        pattern = (r''
                r'(\d+.\d+.\d+.\d+)\s-\s-\s'
                r'\[(.+)\]\s'
                r'"GET\s(.+)\s\w+/.+"\s'     
                r'(\d+)\s'
                r'(\d+)\s'
                r'"(.+)"\s'
                r'"(.+)"'
                )
        parsers = re.findall(pattern,logfile.read())
    return parsers

def main():
    ip_dict_ori = {}
    url_ori = {}
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    for i in logs:
        
        if i[1].find('11/Jan/2017')!=-1:
            ip_dict_ori[i[0]] = ip_dict_ori.get(i[0], 0) + 1
        if i[3]=="404":
            url_ori[i[2]] =url_ori.get(i[2],0)+1

    max_key =  max(ip_dict_ori,key= ip_dict_ori.get)
    max_value = ip_dict_ori.get(max_key)
    max_url_key = max(url_ori,key = url_ori.get)
    max_url_value = url_ori.get(max_url_key)

    ip_dict = {max_key:max_value}
    url_dict = {max_url_key:max_url_value}
    return ip_dict,url_dict

if __name__=='__main__':
    ip_dict,url_dict = main()
    print(ip_dict, url_dict)
