from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

def index(request):
    if request.method == 'POST':
        assignment = float(request.POST.get('assignment', 0))
        quiz = float(request.POST.get('quiz', 0))
        mids = float(request.POST.get('mids', 0))
        finals = request.POST.get('finals', None)
        desired_gpa = request.POST.get('desired_gpa', None)
        lab_mid = request.POST.get('lab-mid', None)
        lab_final = request.POST.get('lab-final',None)
        lab_assg = request.POST.get('lab-assg',None)
        if finals is not None:
            finals = float(finals)
            total_marks = assignment + quiz + mids + finals
            if total_marks>=84.5:
                gpa = 4
            elif 84.5>total_marks>=79.5:
                gpa = 3.7
            elif 79.5>total_marks>=74.5:
                gpa = 3.3
            elif 74.5>total_marks>=69.5:
                gpa = 3.0
            elif 69.5>total_marks>=64.5:
                gpa = 2.7
            elif 64.5>total_marks>=59.5:
                gpa = 2.3
            elif 59.5>total_marks>=54.5:
                gpa = 2.0
            elif 54.5>total_marks>=49.5:
                gpa = 1.7
            elif 49.5>total_marks>=44.5:
                gpa = 1.3
            elif 44.5>total_marks>=39.5:
                gpa = 1.0

            if lab_mid is not None:
                lab_mid = float(lab_mid)
                lab_final = float(lab_final)
                lab_assg = float(lab_assg)
                lab_marks = lab_mid + lab_final + lab_assg
                total_lab = ((75/100)*total_marks) + ((25/100)*lab_marks)
                if total_lab>=84.5:
                    gpa = 4
                elif 84.5>total_lab>=79.5:
                    gpa = 3.7
                elif 79.5>total_lab>=74.5:
                    gpa = 3.3
                elif 74.5>total_lab>=69.5:
                    gpa = 3.0
                elif 69.5>total_lab>=64.5:
                    gpa = 2.7
                elif 64.5>total_lab>=59.5:
                    gpa = 2.3
                elif 59.5>total_lab>=54.5:
                    gpa = 2.0
                elif 54.5>total_lab>=49.5:
                    gpa = 1.7
                elif 49.5>total_lab>=44.5:
                    gpa = 1.3
                elif 44.5>total_lab>=39.5:
                    gpa = 1.0

            return render(request, 'result.html', {'gpa': gpa})    
        
        elif desired_gpa is not None:
            desired = float(desired_gpa)
            total_marks = mids + quiz + assignment
            lab_mid = float(lab_mid)
            lab_final = float(lab_final)
            lab_assg = float(lab_assg)
            lab_marks = lab_mid + lab_final + lab_assg

            if desired>=4:
                finals = ((84.5 - lab_marks) * (100/75)) - total_marks
            elif 4>desired>=3.7:
                finals = ((79.5 - lab_marks) * (100/75)) - total_marks
            elif 3.7>desired>=3.3:
                finals = ((74.5 - lab_marks) * (100/75)) - total_marks
            elif 3.3>desired>=3.0:
                finals = ((69.5 - lab_marks) * (100/75)) - total_marks
            elif 3.0>desired>=2.7:
                finals = ((64.5 - lab_marks) * (100/75)) - total_marks
            elif 2.7>desired>=2.3:
                finals = ((59.5 - lab_marks) * (100/75)) - total_marks
            elif 2.3>desired>=2.0:
                finals = ((54.5 - lab_marks) * (100/75)) - total_marks
            elif 2.0>desired>=1.7:
                finals = ((49.5 - lab_marks) * (100/75)) - total_marks
            elif 1.7>desired>=1.0:
                finals = ((44.5 - lab_marks) * (100/75)) - total_marks
            elif 1.0>desired>=39.5:
                finals = ((39.5 - lab_marks) * (100/75)) - total_marks
            return render(request, 'result.html', {'finals': finals})
        
    return render(request,'calculate.html')



def about(request):
    return render(request,"about.html")

def home(request):
    return render(request,"index.html")