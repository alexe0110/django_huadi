from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет МИР")


def test(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Тест</title>
        </head>
        <body>
            <h1>Это тетовая старница</h1>
            <h3>Проверка</h3>
        </body>
        </html>
    """)
