from django.urls import path, include
from django.http.response import HttpResponse
urlpatterns = [
    path("", include("app.urls")),
    path("includes/secret.inc",
         lambda request: HttpResponse('<?\n$secret = "opp3nh3im3r";\n?>', content_type='text/plain')),

]
