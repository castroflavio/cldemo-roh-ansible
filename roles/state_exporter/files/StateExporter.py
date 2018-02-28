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
        neighbors = lastCol[1:-3]
        excluded = set(["Connect", "Active", "Idle"])
        GoodNeighbors = [p for p in neighbors if p not in excluded ]
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
