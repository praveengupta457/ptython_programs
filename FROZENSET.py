# frozenset is immutable  so we cant add, remove and othr thing
f={10,20,30,40}
fs=frozenset(f)
# fs=frozenset(10,20,30,40) this shows error because at most 1 argument is allowed ,here got 4
print(fs,type(fs))