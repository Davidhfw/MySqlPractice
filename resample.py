import re

s = 'djdjj677ddd678jbdjd48'
pattern = re.compile(r'(\d+)')
sub = pattern.search(s).group(1)
print('sub is ', sub)
num = re.sub(sub, "@", s)
print('num is ', num)