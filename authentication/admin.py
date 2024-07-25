# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Student, Unit

# class CustomUserAdmin(UserAdmin):
#     model = Student
#     list_display = ['username', 'email', 'full_name', 'admission_number', 'course', 'year_of_study', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         ('Student Details', {'fields': ('full_name', 'admission_number', 'course', 'year_of_study')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('full_name', 'admission_number', 'course', 'year_of_study')}),
#     )

# class UnitAdmin(admin.ModelAdmin):
#     list_display = ['student', 'unit_name', 'result']
#     search_fields = ('student__username', 'unit_name')

# admin.site.register(Student, CustomUserAdmin)
# admin.site.register(Unit, UnitAdmin)



from django.contrib import admin
from .models import Student, Unit, SchoolFees

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 1  # Allows one extra form to add more units

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'admission_number', 'course', 'year_of_study')
    inlines = [UnitInline]


class SchoolFeesInline(admin.TabularInline):
    model = SchoolFees
    extra = 1  # Allows one extra form to add more fees details

    
admin.site.register(Student, StudentAdmin)
admin.site.register(Unit)
admin.site.register(SchoolFees)
