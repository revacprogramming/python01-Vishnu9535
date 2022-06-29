def get_cs():
    cs=input('Enter the string')
    return cs    

def cs_to_lot(cs):
    lot=cs.split(';')
    
    z=list()
    for i in lot:
        x=tuple(i.split('='))
        z.append(x)
    return z



def lot_to_cs(z):
    """convert list of strings to connected string"""
    k=list()
    for i in z:
        m=i[0]+'='+i[1]
        k.append(m)
    f=";".join(k)
        
    return f
def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()


# def get_cs():
#     """get string input"""


# def cs_to_lot(cs):
#     """convert connected string to list of strings"""


# def lot_to_cs(lot):
#     """convert list of strings to connected string"""


# def main():
#     cs=get_cs()

#     lot=cs_to_lot(cs)  # convert connect string to list of tuples
#     print(lot)

#     cs=lot_to_cs(lot)  # convert list of strings to connect string
    
#     print(cs)


# if __name__ == '__main__':
#     main()
