
with open("/usr/share/doc/mpv/input.conf", 'r') as f:
    lines = f.readlines()


a = """qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?"""
b = """йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"""


di = {f"#{k} ": f"{v} " for k, v in zip(a, b)}

print(*lines, sep='\n')
for line in lines:
    src = line[:3]
    if src in di:
        print(line.replace(src, di[src]))
