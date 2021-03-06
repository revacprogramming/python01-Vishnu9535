

def get_cs():
    """get string input"""
    cs=input('ENTER THE STRING')
    return cs

def cs_to_dict(cs):
    """convert connect string to a dictionary"""
    iot=dict()
    k=list()
    d=cs.split(';')
    for i in d:
        x=i.split('=')
        k.append(x)
    for i in k:
        iot[i[0]]=i[1]
    return iot
             
            
def dict_to_cs(iot):
    """convert a dictionary to connect string"""
    v=list()
    for key in iot:
        k=key+'='+iot[key]
        v.append(k)
    cs=''
    for i in v:
        cs=cs+i+';'
    return cs
    
def main():
    cs = get_cs()

    d = cs_to_dict(cs) # convert connect string to a dictionary
    print(d)

    cs = dict_to_cs(d)
    print(cs)


if __name__ == '__main__':
    main()
