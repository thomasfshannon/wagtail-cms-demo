from django.conf.urls import url
from django.forms import ModelForm
from django.http import JsonResponse

from .models import ContactSubmission

class ContactForm(ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['email', 'message']

def test(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 201, 'message': 'success'})
        else:
            return JsonResponse({'status': 500, 'message': 'Something went wrong.'})

urlpatterns = [
    url(r'^test', test, name="submit"),
]
