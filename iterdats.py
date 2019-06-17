def iterdate(year=2000, month=1, day=1, hours=0, mins=0, **kwargs):
    """
    iterdate([year,[month,[day,[hours,[mins]]]]])
    A generator function that generate date by an increment pass in the by parameter

    Parameters
    ----------
 
    year, month, day, hours, mins: int;
        datetime parameters to start with
    
    **kwargs:
    ---------
    change: str,
        choose {'months','weeks','days','hours','min'} to change !!!!
    by: int,
        number to change the change parameter by !!!!S
    """
    def chgcheck(chg,iby,num):
        chg = chg+by
        while chg > num:
            chg = chg-num
        return chg

    import datetime
    from collections import defaultdict
    def_k = defaultdict(lambda : 0)
    for n in kwargs.keys():
        def_k[n] = kwargs[n]
    if kwargs:
        start = datetime.datetime(year, month, day, hours, mins)
    else:
        start = datetime.date(year, month, day)
        
    yield (str(start))
    
    if def_k['by'] == 0:
        by=1
    else:
        by = def_k['by']
    while True:
        if def_k['change'] == 'mins': start = start + datetime.timedelta(minutes=by)
        elif def_k['change'] == 'hours': start = start + datetime.timedelta(hours=by)
        elif def_k['change'] == 'days': start = start + datetime.timedelta(days=by)
        elif def_k['change'] == 'weeks': start = start + datetime.timedelta(days= 7*by)
        elif def_k['change'] == 'months':
            dl = list(start.timetuple())[0:6]
            chg = chgcheck(dl[1],by,12)
            start = datetime.datetime(dl[0],chg,dl[2],dl[3],dl[4],dl[5])
        else: start = start + datetime.timedelta(days=1)
        m = str(start)
        yield m

if __name__ == "__main__":
    g =iterdate(2019,6,16,23,59,change='hours', by=28)
    print([next(g) for x in range(20)])