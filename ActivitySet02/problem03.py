

def get_cs():
    cs=input('enter the string')
    return cs


def cs_to_lot(cs):
    # """convert connected string to list of strings"""
    lot=cs.split(';')
    z=list()
    for i in lot:
        x=tuple(i.split('='))
        z.append(x)
    return z

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
