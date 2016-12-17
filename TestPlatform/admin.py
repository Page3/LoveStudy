from django.contrib import admin
from TestPlatform.models import User,IndexImage,MyCollection,MyUploaded,Course,PendingFile,LibraryFile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('uid','name','level','point','school','college')
admin.site.register(User,UserAdmin)

class IndexImageAdmin(admin.ModelAdmin):
	list_display = ('imageUrl','onclickUrl')
admin.site.register(IndexImage,IndexImageAdmin)

class MyCollectionAdmin(admin.ModelAdmin):
	list_display = ('uid','fid')
admin.site.register(MyCollection,MyCollectionAdmin)

class MyUploadedAdmin(admin.ModelAdmin):
	list_display = ('uid','fid')
admin.site.register(MyUploaded,MyUploadedAdmin)

class CourseAdmin(admin.ModelAdmin):
	list_display = ('school','college','course')
admin.site.register(Course,CourseAdmin)

class PendingFileAdmin(admin.ModelAdmin):
	list_display = ('fid','fhash','uid','school','college','course','name','brief','filetype','extension','uploadtime','size','page')
admin.site.register(PendingFile,PendingFileAdmin)

class LibraryFileAdmin(admin.ModelAdmin):
	list_display = ('fid','fhash','uid','school','college','course','name','brief','filetype','extension','uploadtime','size','page','download')
admin.site.register(LibraryFile,LibraryFileAdmin)