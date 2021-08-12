from django.shortcuts import render
from .model import cruds
from .forms import crudFoms
from django.contrib import messages
def all(request):
    result=cruds.objects.all()
    return render(request, 'index.html',{"cruds":result})
def save_record(request):
    if request.method=="POST":
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('address') and request.POST.get('phone') and request.POST.get('gender'):
            student=cruds()
            student.name=request.POST.get('name')
            student.email=request.POST.get('email')
            student.phone=request.POST.get('phone')
            student.addess=request.POST.get('address')
            student.gender=request.POST.get('gender')
            student.save()
            messages.success(request,"the record of "+student.name+" saved successfuly")
            return render(request,'create.html')
    else:
        return render(request, 'create.html')

def edit(request, id):
    student=cruds.objects.get(id=id)
    return render(request,'edit.html', {"cruds":student})
def update(request,id):
    studenobj=cruds.objects.get(id=id)
    form=crudFoms(request.POST,instance=studenobj)
    if form.is_valid():
        form.save()
        messages.success(request,"student record is updated successfully")
    return render(request,'edit.html',{"cruds":studenobj})

def deleteRecord(request, id):
    student=cruds.objects.get(id=id)
    student.delete()
    result = cruds.objects.all()
    return render(request, 'index.html', {"cruds": result})