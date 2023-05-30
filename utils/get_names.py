import names as nm
def get_names(size):
    names = []
    while size > 0:
        names.append(nm.get_first_name())
        size-=1
    return names