s = 'python'
sub = 'on'
def find_first(s, sub):
    if sub not in s:
        return None
    else:
       return s.find(sub)

def find_last(s, sub):
    if sub not in s:
        return None
    else:
        return s.rfind(sub)
print(find_last(s,sub))
print(find_first(s, sub))
