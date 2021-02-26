import re


pattern = r'(.+)>(?P<grp1>[0-9]{3})(\|)(?P<grp2>[a-z]{3})\3(?P<grp3>[A-Z]{3})\3(?P<grp4>[^<>]{3})<\1'

n = int(input())
for _ in range(n):
    pw = re.search(pattern, input())
    if pw:
        encrypted_pw = pw.group('grp1') \
                       + pw.group('grp2') \
                       + pw.group('grp3') \
                       + pw.group('grp4')
        print(f'Password: {encrypted_pw}')
    else:
        print('Try another password!')

