def gfbn(num):
    def mb(value):
        return num * value
    return mb
nds = gfbn(6)
print("5 * 10", nds(10))
