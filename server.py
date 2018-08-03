# -*- coding:utf-8 -*-

from flask import Flask,request,render_template
import config,json

app = Flask(__name__)
delay = []
for i in config.server_list.keys():
    init = {"source": "%s" %i}
    delay.append(init)

@app.route('/')
def display():
#    print delay
    dest = delay[0].keys()
    del dest[dest.index('source')]
    source = []
    values = []
    for i in  delay:
        source.append(i['source'])
        #source = sorted(source)
        value = []
        for j in i.keys():
            if j != 'source':
                value.append(i[j])
        values.append(value)
    return render_template('index.html',dest= dest,source=source,values=values)


@app.route('/data',methods=["POST"])
def recv_data():
    data = json.loads(request.get_data())
    for i in xrange(len(delay)):
        if str(delay[i]['source']) == str(data['source']):
            delay[i] = data
            break
    print data
    return 'success'


@app.route('/server_list')
def server_list():
    source = request.remote_addr
    server_list= config.server_list
 #   print server_list
    for i in server_list.keys():
        if str(server_list[i]) == str(source):
            source = i
            break
    server_list['source'] = source
#    server_list = sorted(server_list)
    return json.dumps(server_list)

if __name__ == '__main__':
    app.run(port=9092,host='0.0.0.0',debug=False)
