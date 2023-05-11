import names as nm
def getNames(size):
    names = []
    while size > 0:
        names.append(nm.get_first_name())
        size-=1
    return names