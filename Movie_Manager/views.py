from django.shortcuts import render
from . models import Moviedata
from . Form import MovieFrom
# Create your views here.

def Creat(request):
    frm=MovieFrom()
    if request.POST:
        frm=MovieFrom(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
    else:
        frm=MovieFrom()
    return render(request,'Create.html',{'frm':frm}) 
def List(request):
    Movie_set=Moviedata.objects.all()
    print(Movie_set)
    return render(request,'List.html',{'Movie_list':Movie_set})
def Edit(request,pk):
    instance_to_b_edited = Moviedata.objects.get(pk=pk)
    if request.POST:
        frm = MovieFrom(request.POST,instance=instance_to_b_edited)
        if frm.is_valid():
            instance_to_b_edited.save()
    else:
        frm = MovieFrom(instance = instance_to_b_edited)
    return render(request,'Create.html',{'frm':frm})

def delete(request,pk):
    instance=Moviedata.objects.get(pk=pk)
    instance.delete()
    movie_set=Moviedata.objects.all()
    return render(request, 'List.html',{'movies': movie_set})