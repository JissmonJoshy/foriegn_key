from django.shortcuts import render, redirect
from .models import Course, Student


def home(request):
    return render(request, 'home.html')



def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        fee = request.POST['fee']
        Course.objects.create(name=name, fee=fee)
        return redirect('add_course')
    return render(request, 'add_course.html')




def add_student(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        age = request.POST['age']
        date_of_birth = request.POST['date_of_birth']
        course_id = request.POST['course']
        course = Course.objects.filter(id=course_id).first()

        if course:
            Student.objects.create(name=name, address=address, age=age, 
                                   date_of_birth=date_of_birth, 
                                   course=course)
            return redirect('show_student_details')
    return render(request, 'add_student.html', {'courses': courses})



def show_student_details(request):
    students = Student.objects.all()
    return render(request, 'show_student_details.html', {'students': students})




def edit_student(request, id):
    student = Student.objects.filter(id=id).first()
    if student:
        courses = Course.objects.all()
        if request.method == 'POST':
            student.name = request.POST['name']
            student.address = request.POST['address']
            student.age = request.POST['age']
            student.date_of_birth = request.POST['date_of_birth']
            course_id = request.POST['course']
            course = Course.objects.filter(id=course_id).first()
            if course:
                student.course = course
                student.save()
                return redirect('show_student_details')
        return render(request, 'edit_student.html', {'student': student, 'courses': courses})
    return redirect('show_student_details')




def delete_student(request, id):
    student = Student.objects.filter(id=id).first()
    if student:
        student.delete()
    return redirect('show_student_details')
