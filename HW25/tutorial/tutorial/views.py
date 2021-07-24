from django.http import HttpResponse
import random


def status(request):
    return HttpResponse("OK")


def random_color(request):
    r = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (r(), r(), r())
    html = f"<html><body bgcolor={color}>Random color: {color}</body></html>"
    return HttpResponse(html)
