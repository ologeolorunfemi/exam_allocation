from django.shortcuts import render

# Create your views here.

from .models import Hall, Student, SeatAllocation
import random

def allocate_view(request):
    halls = Hall.objects.all()
    students = Student.objects.all().order_by('?') # shuffle to mix departments
    
    if request.method == "POST":
        # Clear old allocation
        SeatAllocation.objects.all().delete()
        
        # Mix students properly - sort by dept then shuffle to avoid same dept together
        student_list = list(Student.objects.all())
        random.shuffle(student_list)
        # sort by department to spread them
        student_list.sort(key=lambda x: x.department)
        # now interleave
        student_list = student_list[::2] + student_list[1::2]
        random.shuffle(student_list)

        seat_index = 0
        hall_list = list(Hall.objects.all())
        
        # Create flat list of all seats: [(Hall, seat_no), ...]
        all_seats = []
        for hall in hall_list:
            for i in range(1, hall.capacity + 1):
                all_seats.append((hall, i))
        
        for student in student_list:
            if seat_index >= len(all_seats):
                break # hall full
            hall, seat_no = all_seats[seat_index]
            SeatAllocation.objects.create(student=student, hall=hall, seat_no=seat_no)
            seat_index += 1
            
        allocations = SeatAllocation.objects.all()
        return render(request, "exam_hall/result.html", {"allocations": allocations})

    return render(request, "exam_hall/index.html", {"halls": halls, "students": students, "total_capacity": sum(h.capacity for h in halls)})

def hall_view(request, hall_id):
    hall = Hall.objects.get(id=hall_id)
    allocations = SeatAllocation.objects.filter(hall=hall)
    return render(request, "exam_hall/hall.html", {"hall": hall, "allocations": allocations})
