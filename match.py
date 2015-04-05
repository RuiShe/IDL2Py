## python version of IDL procedure match.pro

def match(a,b):
    "This is a function to match two numpy arrays."
    na = len(a)
    nb = len(b)
    ind = np.concatenate(( np.arange(na) , np.arange(nb) ))
    vec = np.concatenate(( np.zeros(na) , np.ones(nb) ))
    c = np.concatenate((a,b))
    ## sort
    sub = c.argsort()
    c = c[sub]
    ind = ind[sub]
    vec = vec[sub]
    ## find duplicated 
    n = na + nb
    firstdup = np.where( (c == np.roll(c,-1)) * ( vec != np.roll(vec,-1)) )
    nd = len(firstdup[0])

    dup = np.zeros( nd * 2 , dtype='int')
    even = np.arange(0, nd) * 2 
    dup[even] = firstdup
    dup[even + 1] = firstdup[0] + 1 
    ind = ind[dup]
    vec = vec[dup]
    subb = ind[ np.where( vec == 0 )]
    suba = ind[ np.where( vec == 1 )]
    ## a[subb] = b[suba]
    return (suba, subb)
