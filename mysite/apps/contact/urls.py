from django.conf.urls import url

def test():
    return True

urlpatterns = [
    url(r'^test/', test, name="submit"),
]
