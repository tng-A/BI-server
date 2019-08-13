""" Analysis helper file"""

def income_stream_okr(queryset, *args, **kwargs):
    start = kwargs.get('start', None)
    end = kwargs.get('end', None)
    filtered_okr = []
    for okr in queryset:
        if okr.period >= start and okr.period <= end:
            filtered_okr.append(okr)
    return filtered_okr
