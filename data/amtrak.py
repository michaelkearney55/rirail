import datetime as dt
import os
import json

format = '%I:%M%p'

try:
    os.remove('marey-trips.json')
except OSError:
    pass

try:
    os.remove('marey-trips-all.json')
except OSError:
    pass

try:
    os.remove('marey-trips-nb.json')
except OSError:
    pass

try:
    os.remove('marey-trips-sb.json')
except OSError:
    pass

try:
    os.remove('marey-trips-sb-amtk.json')
except OSError:
    pass

try:
    os.remove('marey-trips-nb-amtk.json')
except OSError:
    pass

try:
    os.remove('marey-trips-amtk.json')
except OSError:
    pass

nb_stops = ["place-alfcl", "place-jfk", "place-asmnl"]
sb_stops = ["place-asmnl", "place-jfk", "place-alfcl"]

day = dt.date(2014, 2, 3)

nb_trips = []
sb_trips = []

with open('amtrak.txt', 'r') as amtrak_in:
    line = amtrak_in.readline()
    while line:
        things = line.split(',')
        stopnames = nb_stops if things[1] == 'northbound' else sb_stops
        times = list()
        for i in range(2,5):
            time = dt.datetime.strptime(things[i], format)
            mydt = dt.datetime.combine(day, time.time())
            times.append(int(mydt.timestamp()))
        out = dict()
        out["trip"] = things[0]
        out["line"] = "red"
        out["begin"] = times[0]
        out["end"] = times[2]
        stops = list()
        for i in range(0,3):
            stops.append({"stop": stopnames[i], "time": times[i]})
        out["stops"] = stops
        nb_trips.append(out) if things[1] == 'northbound' else sb_trips.append(out)
        line = amtrak_in.readline()

with open('marey-trips-nb-amtk.json', 'x') as amtrak_out:
    amtrak_out.write(json.dumps(nb_trips))

with open('marey-trips-sb-amtk.json', 'x') as amtrak_out:
    amtrak_out.write(json.dumps(sb_trips))

with open('marey-trips-amtk.json', 'x') as amtrak_out:
    amtrak_out.write(json.dumps(nb_trips+sb_trips))

nb_stops = ["place-alfcl", "place-asmnl", "place-brntn"]
sb_stops = ["place-brntn", "place-asmnl", "place-alfcl"]

count = 0

nb_starts = [1391423520,1391424720,1391427120,1391428320,1391429520,1391430720,1391431920,1391433120,1391434020,1391436720,1391437920,1391441820,1391442720,1391443920,1391446320,1391449920,1391451120,1391452320,1391454600,1391457120,1391458320,1391460720,1391461920,1391463120,1391467020,1391467920,1391468940,1391471520,1391472540,1391474640]

for i in nb_starts:
    times = [i, i + 60*60, i + 82*60]
    out = dict()
    out["trip"] = "nb_" + str(count)
    out["line"] = "red"
    out["begin"] = times[0]
    out["end"] = times[2]
    stops = list()
    for i in range(0,3):
        stops.append({"stop": nb_stops[i], "time": times[i]})
    out["stops"] = stops
    nb_trips.append(out)
    count += 1

count = 0

sb_starts = [1391422320,
             1391423520,
             1391426820,
             1391428020,
             1391430020,
             1391431320,
             1391434020,
             1391435040,
             1391438040,
             1391439240,
             1391441820,
             1391444520,
             1391445720,
             1391448120,
             1391449020,
             1391451420,
             1391452320,
             1391454720,
             1391455920,
             1391457120, #20
             1391459520,
             1391460520,
             1391462520,
             1391463420,
             1391464320,
             1391465520,
             1391466720,
             1391467920,
             1391469120,
             1391471820,
             1391473020,
             1391473920]

for i in sb_starts:
    times = [i, i + 22*60, i + 82*60]
    out = dict()
    out["trip"] = "sb_" + str(count)
    out["line"] = "red"
    out["begin"] = times[0]
    out["end"] = times[2]
    stops = list()
    for i in range(0,3):
        stops.append({"stop": sb_stops[i], "time": times[i]})
    out["stops"] = stops
    sb_trips.append(out)
    count += 1

with open('marey-trips-nb.json', 'x') as amtrak_out:
    amtrak_out.write(json.dumps(nb_trips))

with open('marey-trips-sb.json', 'x') as amtrak_out:
    amtrak_out.write(json.dumps(sb_trips))

with open('marey-trips-all.json', 'x') as amtrak_out:
    amtrak_out.write(json.dumps(nb_trips+sb_trips))



