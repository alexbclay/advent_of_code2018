from collections import defaultdict

lines = []
with open('input', 'rb') as input_file:
    for line in input_file:
        lines.append(line.replace('\n', ''))


twos = 0
threes = 0
for line in lines:
    cur_dict = defaultdict(lambda: 0)
    for char in line:
        cur_dict[char] += 1
    if 2 in cur_dict.values():
        twos += 1
    if 3 in cur_dict.values():
        threes += 1

print 'CHECKSUM', twos * threes
print len(lines)


# ----------------------------
def find_it(strings):
    seen = []
    for line in lines:
        print '-' * 25
        for other in seen:
            print line
            print other
            diffs = 0
            mismatch = 0
            for i in range(len(line)):
                if line[i] != other[i]:
                    diffs += 1
                    print 'mismatch at', i
                    mismatch = i
                if diffs > 1:
                    break
            if diffs == 1:
                print 'Found it!'
                return line[:mismatch] + line[mismatch+1:]
        seen.append(line)


print find_it(lines)
