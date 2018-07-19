# -*- coding:utf-8 -*-

import httplib,ping,json

server='127.0.0.1'


def get_server_list():
    url = "http://%s/server_list" % server
    conn = httplib.HTTPConnection(server,port=5000)
    conn.request(method="GET",url=url)
    response = conn.getresponse()
    return response


def post_data(post_data):
    url = "http://%s/data" % server
    conn = httplib.HTTPConnection(server,port=5000)
    conn.request(method="POST", url=url, body=post_data)
    response = conn.getresponse().read()
    return response

def get_delay():
    server_list=json.load(get_server_list())
    #print server_list
    for i in server_list.keys():
        if i != 'source':
            pinger = ping.Pinger(target_host=server_list[i])
            server_list[i]=pinger.ping()
    #print server_list
    return server_list


if __name__ == '__main__':
    post_data(json.dumps(get_delay()))

