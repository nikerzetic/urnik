import datetime


def teden_dneva(dan):
    ponedeljek = dan - datetime.timedelta(days=dan.weekday())
    nedelja = ponedeljek + datetime.timedelta(days=6)
    return (ponedeljek, nedelja)

def teden_int_v_datetime(teden):
    teden = datetime.datetime.strptime(teden, "%Y-%m-%d")
    return teden_dneva(teden)
