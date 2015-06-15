from django.shortcuts import render

def server_monitor(request):

    return render(request, 'servermon/base.html', {})
