# from django.contrib import admin
# from django.db import models
# from .models import Student, Alumni
# from image_uploader_widget.widgets import ImageUploaderWidget

# class StudentAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['user']  # Replaces dropdown with search box
#     list_display = ['first_name', 'last_name', 'usn', 'batch', 'email']
#     list_filter = ['batch']  # Add filter by batch (you can add more fields)

# class AlumniAdmin(admin.ModelAdmin):
#     autocomplete_fields = ['user']
#     list_display = ['first_name', 'last_name', 'usn', 'batch']
#     search_fields = ['first_name', 'last_name', 'usn', 'batch', 'email']  # Define fields to search by
#     list_filter = ['batch','graduation_year']  # Add filter by batch (you can add more fields)

# admin.site.register(Alumni, AlumniAdmin)
# admin.site.register(Student, StudentAdmin)

# @admin.register(Alumni)
# class AlumniAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.ImageField: {'widget': ImageUploaderWidget},
#     }



from django.contrib import admin
from django.db import models
from .models import Student, Alumni
from image_uploader_widget.widgets import ImageUploaderWidget

class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']  # Replaces dropdown with search box
    list_display = ['first_name', 'last_name', 'usn', 'batch', 'email']
    list_filter = ['batch']  # Add filter by batch (you can add more fields)

class AlumniAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['first_name', 'last_name', 'usn', 'batch']
    search_fields = ['first_name', 'last_name', 'usn', 'batch', 'email']  # Define fields to search by
    list_filter = ['batch', 'graduation_year']  # Add filter by batch (you can add more fields)
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget},
    }

admin.site.register(Student, StudentAdmin)
admin.site.register(Alumni, AlumniAdmin)
