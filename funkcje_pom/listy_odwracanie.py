def reverse(wsk):
    if wsk == None:
        return None

    if wsk.next == None:
        return wsk

    p, q, r = None, wsk, wsk.next

    while q != None:
        q.next = p
        p = q
        q = r
        if r != None:
            r = r.next

    return p