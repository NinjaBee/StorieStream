from django.shortcuts import render

import os

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

from .models import

def index(request):
    return HttpResponse('hi')


@require_POST
def uploads(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
    path = default_storage.save(save_path, request.FILES['file'])
    document = Document.objects.create(document=path, upload_by=request.user)
    return JsonResponse({'document': document.id})

