from django.shortcuts import render

def student_form(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        major = request.POST.get('major')
        class_standing = request.POST.get('class_standing')
        languages = request.POST.getlist('languages')
        graduation_year = request.POST.get('graduation_year')
        comments = request.POST.get('comments')

        if not student_name or not student_id:
            error = "Student Name and Student ID are required."
            return render(request, 'studentinfo/student_form.html', {'error': error})

        context = {
            'student_name': student_name,
            'student_id': student_id,
            'major': major,
            'class_standing': class_standing,
            'languages': languages,
            'graduation_year': graduation_year,
            'comments': comments,
        }

        return render(request, 'studentinfo/results.html', context)

    return render(request, 'studentinfo/student_form.html')