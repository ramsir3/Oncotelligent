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

patient = json.loads(open(sys.argv[1], 'r').read())
cancer = json.loads(open(patient["cancer"]+'.json', 'r').read())


fn = sys.argv[1].split('.')
report = open("report_" + fn[0] + ".txt", 'w')
recurse('', cancer, patient, report)
report.close()

