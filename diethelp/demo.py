import json, sys

def recurse(t, c, p, f):
    for key in sorted(c.keys()):
        if key in p.keys():
            f.write('\n' + t + key + ':\n')
            if type(c[key]) != dict:
                # print("\nyes")
                f.write(t + c[key][p[key]] + '\n')
            else:
                recurse(t + '\t', c[key][p[key]], p, f)
                # print(c[key][p[key]])
                # print(type(c[key][p[key]]))
                # print('\n')

# Patient file provided as console input 
patientDict = json.loads(open(sys.argv[1], 'r').read())
# Cancer field of patient file ({A,B,C,D}-Carcinoma.json)
cancerDict = json.loads(open(patient["cancer"]+'.json', 'r').read())

# Patient name taken from file (Patient-{A,B,C})
patientName = sys.argv[1].split('.')[0]
report = open("report_" + patientName + ".txt", 'w')
recurse('', cancerDict, patientDict, report)
report.close()

