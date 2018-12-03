changes = []
total = 0
with open('input', 'rb') as f:
    for line in f:
        delta = int(line)
        total += delta
        changes.append(delta)


def find_repeat(deltas, limit):
    loops = 0
    seen = set()
    seen.add(0)
    cur_sum = 0
    while loops <= limit:
        print '-- loop', loops, ' SUM: ', cur_sum
        for delta in deltas:
            cur_sum += delta
            # print cur_sum
            if cur_sum in seen:
                print "FOUND IT in", loops, "loops"
                return cur_sum
            seen.add(cur_sum)
        loops += 1
    print "NOTHING FOUND!", loops, "loops"


print 'REPEATED', find_repeat(changes, 200)
# print 'REPEATED', find_repeat([7, 7, -2, -7, -4], 100)
