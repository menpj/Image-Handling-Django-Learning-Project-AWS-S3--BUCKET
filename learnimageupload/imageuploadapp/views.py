#https://youtu.be/lKyH_ZGtvwM
from django.shortcuts import render,get_object_or_404,redirect
from imageuploadapp.forms import DogForm
from imageuploadapp.models import Dog

# Create your views here.
def upload_form(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'index.html',context)

    context = {'form': DogForm()}
    return render(request, 'index.html',context)


def list_dogs(request):
    dogs= Dog.objects.all()
    context={'dogs':dogs}
    return render(request,'list.html',context)

def delete_image(request,pk):
    dog=get_object_or_404(Dog,pk=pk)
    dog.delete()
    return redirect('list_dogs')    