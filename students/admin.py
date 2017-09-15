from django.contrib import admin

from .models.students import Student
from .models.groups import Group
from .models.exams import Exam
from .models.exams_results import Exam_result

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Exam)
admin.site.register(Exam_result)

