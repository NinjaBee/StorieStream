from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        file = request.FILES['file']
        model = SavedFile(name=name, file=file)
        model.save()
    files = SavedFile.objects.all()
    print(files[0].file.size)
    return render(request, 'uploads/index.html', {'files': files})


