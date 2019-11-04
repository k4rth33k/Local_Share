from django.shortcuts import render, redirect
from app.models import Links
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os, shutil
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def home(req):
	if req.method == 'POST':
		link = req.POST['link']
		print(link)
		new_link = Links(link=link.strip())
		new_link.save()
	
	orm_data = Links.objects.all()

	if len(orm_data) > 10:
		Links.objects.filter(id_s=orm_data[0].id_s).delete()

	data = {link_.id_s : link_.link for link_ in Links.objects.all()}
	# print('----------------------------')
	# for link_ in Links.objects.all():
	# 	print(link_.id_s, link_.link)
	# print('----------------------------')

	return render(req, 'index.html', {'data' : data})

def clear(req):
	Links.objects.all().delete()
	return redirect('/')


def files(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # return render(request, 'upload.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })

    path = settings.MEDIA_ROOT
    list_ = os.listdir(path)
    return render(request, 'upload.html', {'data' : list_})

    

def clear_files(request):
	folder = settings.MEDIA_ROOT
	for the_file in os.listdir(folder):
	    file_path = os.path.join(folder, the_file)
	    try:
	        if os.path.isfile(file_path):
	            os.unlink(file_path)
	    except Exception as e:
	        print(e)

	return HttpResponseRedirect(reverse('files'))


def download(request):
    path = request.GET['name']
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404