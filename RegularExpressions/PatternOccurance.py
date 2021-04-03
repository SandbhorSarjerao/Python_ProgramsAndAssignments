import re
count = 0
# pattern = re.compile('ab')
# matcher = pattern.finditer('abaababa')
matcher = re.finditer('ab', 'abaababa')
for match in matcher:
    count += 1
    print('Match is available at start index: ', match.start())
    # print('start: {}, end: {}, group: {}'.format(match.start(), match.end(), match.group()))
print('The Number of Occurrences: ', count)