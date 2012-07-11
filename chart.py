#!/usr/bin/env python

import datetime
import time


def load_stats(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            nl_index = line.find("\n")
            if nl_index != -1:
                line = line[:nl_index]

            chunk = line.split(", ")
    
            data.append(chunk)
    return data

def load_template(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

def save(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)


if __name__=="__main__":
    path = "[PATH]/stats.txt"
    template_path = "[PATH]/template.html"
    out_path = "[PATH]/index.html"

    data = load_stats(path)

    chart1 = []
    chart2 = []
    for item in data:
        dt = datetime.datetime.strptime(item[0], '%Y-%m-%dT%H:%M:%S.%f')
        item[0] = time.mktime(dt.timetuple())
        item[1] = int(item[1])
        item[2] = int(item[2])
        
        chart1.append([item[0], item[1]])
        chart2.append([item[0], item[2]])

    # convert and snip the outer brackets so its just the children
    chart1 = str(chart1)[1:-1]
    chart2 = str(chart2)[1:-1]
    
    template = load_template(template_path)
    template = template.format(chart1, chart2)

    save(out_path, template)
    