from django.urls import path
from myapp.views import hello, goodbye

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    # myapp/goodbye/<str:name>
    path('goodbye/<str:name>', goodbye, name='goodbye'),
    # myapp/<str:name>
    path('<str:name>', hello, name='hello_name'),

]
