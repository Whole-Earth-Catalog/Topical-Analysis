import re

pattern = "\s+"

years = ["1500", "1600", "1700"]
for year in years:
    clusters = ["c0", "c1", "c2"]
    path = "tsv/"
    type = ".txt"
    all_subjects = []
    dupe_subjects = []
    for cluster in clusters:
        fname = path + year + "s_" + cluster + type
        f = open(fname, 'r')
        c = 0
        for line in f:
            if c > 0:
                row = line.split("\t")
                subject = row[0]
                if subject in all_subjects:
                    dupe_subjects.append(subject)
                else:
                    all_subjects.append(subject)
            c += 1
        f.close()
    print("\n" + year + " number of duplicate subjects: " + str(len(dupe_subjects)))
    for cluster in clusters:
        fname = path + year + "s_" + cluster + type
        f = open (fname, 'r')
        new_path = "no_dupes/"
        new_type = ".tsv"
        new_fname = new_path + year + "s_" + cluster + new_type
        new_f = open(new_fname, 'w')
        c = 0 
        num_lines = 0
        for line in f:
            if c > 0:
                row = line.split('\t')
                subject = row[0]
                if subject not in dupe_subjects:
                    new_f.write(line)
                    num_lines += 1
            else:
                new_f.write(line)
            c += 1
        f.close()
        new_f.close()
        print(year + cluster + " has " + str(num_lines) + " rows")

