from django.http import HttpResponse, Http404
from django.shortcuts import render
import json

colors_list = ['yellow', 'green', 'red', 'blue']


def index(request):
    return HttpResponse("Welcome to colors app")


def list(request):
    return render(request, 'colors/list.html', {'colors': colors_list})


def add(request):
    color_to_add = request.GET.get('color')
    if color_to_add in colors_list:
        response_data = {'message': '{} already in the list'.format(color_to_add)}
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=409)
    elif color_to_add is None:
        return HttpResponse("Please add a color")
    else:
        colors_list.append(color_to_add)
        response_data = {'colors': colors_list,
                         'message': '{} successfully added to the list'.format(color_to_add)}
    return render(request, 'colors/list.html', {'colors': colors_list}, status=201)


def get(request):
    color = request.GET.get('color')
    if color in colors_list:
        return HttpResponse("{}".format(color))
    else:
        raise Http404("{} does not exist in our database".format(color))
