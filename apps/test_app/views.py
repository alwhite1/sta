from django.shortcuts import render


def test_app(request):
    return render(request, 'test.html')
    pass
