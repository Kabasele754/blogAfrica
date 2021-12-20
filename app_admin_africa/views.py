from django.http import JsonResponse
from django.shortcuts import render
from .forms import AdminForm
from .models import Admin
from django.views.decorators.csrf import csrf_exempt


def index(request):
    form = AdminForm()
    stu = Admin.objects.all()
    context = {'form':form, 'stu':stu}
    return render(request, 'admin_africa/index.html', context)

def home(request):
    form = AdminForm()
    stu = Admin.objects.all()
    context = {'form':form, 'stu':stu}
    return render(request, 'admin_africa/home.html', context)


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            course = request.POST['course']
            print('student id',sid)

            if(sid == ''):
                s = Admin(name=name, email=email, course=course)
            else:
                s = Admin(id=sid, name=name, email=email, course=course)
            s.save()

            stu = Admin.objects.values()
            student_data = list(stu)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        s = Admin.objects.get(pk=id)
        s.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print('Student ID',id)
        student = Admin.objects.get(pk=id)
        student_data = {'id':student.id, 'name':student.name, 'email':student.email, 'course':student.course}
        return JsonResponse(student_data)
















