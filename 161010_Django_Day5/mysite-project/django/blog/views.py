from django.shortcuts import render, HttpResponse


def test(request):
    return HttpResponse('Test! %s' % post_id)