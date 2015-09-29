s = 'azcbobobegghakl'

sub_string = 'bob'
sub_count = 0

for i in range(len(s)):
    i = s.find(sub_string)
    if i > -1:
        sub_count += 1
        s = s[i+len(sub_string)-1:]

print 'Number of times %s occurs is: %d' % (sub_string, sub_count)
