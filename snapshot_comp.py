
base_snap_file = "./snapshots/snapshot_base.csv"
ref_snap_file = "./snapshots/snapshot_2023_08_15.csv"

indicator_config = {
    "Price": {
        "factor": -5
    },
    "Target Price": {
        "factor": 5
    },
    "P/E": {
        "factor": -5
    },
    "Forward P/E": {
        "factor": -5
    },
    "P/B": {
        "factor": -1
    },
    "PEG": {
        "factor": -1
    },
    "P/FCF": {
        "factor": -1
    },
    "Dividend %": {
        "factor": 5
    },
    "Debt/Eq": {
        "factor": -5
    },
    "Payout": {
        "factor": -5
    },
    "EPS next 5Y": {
        "factor": 5
    },
    "EPS growth next Y": {
        "factor": 3
    }
}


def readSnapshot(snap_file):
    header = []
    snapshot = {}
    with open(snap_file, 'r') as file:
        line = file.readline()
        header = line.split(";");
        line = file.readline()
        while line:
            splitted = line.split(";");
            snapshot[splitted[0].strip()] = {}
            for i in range(1, len(header)):
                snapshot[splitted[0].strip()][header[i]] = splitted[i].strip().replace("%", "")

            snapshot[splitted[0].strip()]["fitness"] = 0
            line = file.readline()
            

    return [header, snapshot]


header , base_snap = readSnapshot(base_snap_file)
header2 , ref_snap = readSnapshot(ref_snap_file)


for ticker, indicators in base_snap.items():
    for h in header:
        if h  in indicator_config:
            if indicators[h] == "-" or ref_snap[ticker][h] == "-":
                if indicators[h] != ref_snap[ticker][h] and ref_snap[ticker][h] == "-":
                    ref_snap[ticker]["fitness"] -= 1
            else:
                if float(ref_snap[ticker][h]) > float(indicators[h]):  
                    ref_snap[ticker]["fitness"] += indicator_config[h]["factor"]
                    #print(f"{ticker}:{h} {indicators[h]} --> {ref_snap[ticker][h]} + {indicator_config[h]['factor']}")
                else:
                    ref_snap[ticker]["fitness"] -= indicator_config[h]["factor"]
                    #print(f"{ticker}:{h} {indicators[h]} --> {ref_snap[ticker][h]} - {indicator_config[h]['factor']}")


sorted_snap = {k: v for k, v in sorted(ref_snap.items(), key=lambda item: item[1]["fitness"], reverse=True)}
for ticker in sorted_snap.keys():
    print(f"{ticker} --> {ref_snap[ticker]['fitness']}")
