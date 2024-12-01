from django.shortcuts import render


def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')
    elif request.method == 'POST':
        return render(request, 'dashboard.html')

