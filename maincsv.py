import glob
import csv

csvfiles = glob.glob('D:\Merge\*.csv')
wf = csv.writer(open('D:\Merge\output.csv','w',encoding="utf8"),delimiter = ',')

for files in csvfiles:
    #print(files)
    rd = csv.reader(open(files,encoding="utf8"),delimiter = ',')
    for row in rd:
        print(row)
        wf.writerow(row)

