import os, time
from flask import Flask

neighbors = 0

app = Flask(__name__)

@app.route("/")
def bgp():
        bgp_summary=os.popen("vtysh -c 'show ip bgp summary'").read()
        s=bgp_summary.split("Neigh")[1]
        lines=s.split("\n")
        lastCol=[l.split(" ")[-1] for l in lines]
        GoodNeighbors = lastCol[1:-3]
        remove( GoodNeighbors, "Connect" )
        remove( GoodNeighbors, "Active" )
        remove( GoodNeighbors, "Idle" )
        neighbors = len(GoodNeighbors)
        return str(neighbors)

def remove(list, item):
    try:
        list.remove(item)
    except:
        a="1"#Do nothing
    return list

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
