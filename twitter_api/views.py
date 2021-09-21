from django.shortcuts import render
from django.template import RequestContext
from .models import Document
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import pandas  as pd
import numpy as np
import json
import os
from django.conf import settings
from django.http import HttpResponse, Http404


def index(request):
    return render(request,'index.html')



def download(request,path):
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                        return response
        raise Http404


