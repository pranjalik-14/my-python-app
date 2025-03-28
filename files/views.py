from django.http import Http404, HttpResponse, Http404
from django.shortcuts import render, redirect

from .forms import UploadForm
from .models import File
def index(request):
    return render(request, 'files/index.html')

def files(request):
    data = File.objects.all()
    return render(request, 'files/files.html', {"files": data, 'form': UploadForm})

def file(request, file_id):
    f = File.objects.get(pk=file_id)
    if f:
        return render(request, 'files/file.html', {'file' : f})
    else:
        raise Http404('File does not exists')

def edit(request, file_id):
    name = request.POST.get('name')
    file_type = request.POST.get('type')
    f = File.objects.get(pk=file_id)
    print(name, file_type, f)

    if f:
        if name:
            f.name = name
        if file_type:
            f.file_type = file_type
        f.save()
        return redirect(files)
    else:
        return redirect(files)

def delete(request, file_id):
    f = File.objects.get(pk=file_id)
    if f:
        f.delete()
        return redirect(files)
    else:
        return redirect(files)

def upload(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect(files)