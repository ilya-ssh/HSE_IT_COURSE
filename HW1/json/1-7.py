import json
complexn = 4 + 3j
if isinstance(complexn, complex):
    serialized = [complexn.real, complexn.imag]
else:
    raise TypeError(f"{complexn} is not a complex number")
res = json.dumps(serialized)
print(res)
