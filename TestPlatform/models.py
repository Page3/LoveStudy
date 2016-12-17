from django.db import models

# Create your models here.

class User(models.Model):
	uid     =models.IntegerField(u'Uid',primary_key=True)
	name    =models.CharField(u'昵称',max_length=30)
	level   =models.IntegerField(u'等级')
	point   =models.IntegerField(u'积分')
	school  =models.CharField(u'所在大学',max_length=30)
	college =models.CharField(u'所在学院',max_length=30)

	def __str__(self):
		return self.name

class IndexImage(models.Model):
	imageUrl     =models.CharField(u'图片来源',primary_key=True,max_length=200)
	onclickUrl   =models.CharField(u'广告指向地址',max_length=200)

	def __str__(self):
		return self.imageUrl

class MyCollection(models.Model):
	uid=models.IntegerField(u'Uid')
	fid=models.IntegerField(u'Fid')

	def __iter__(self):
		return [ self.uid, 
				 self.fid ] 

class MyUploaded(models.Model):
	uid=models.IntegerField(u'Uid')
	fid=models.IntegerField(u'Fid')

	def __iter__(self):
		return [ self.uid, 
				 self.fid ] 

class Course(models.Model):
	school    =models.CharField(u'所在大学',max_length=30)
	college   =models.CharField(u'所在学校',max_length=30)
	course    =models.CharField(u'课程名称',max_length=30)

	def __iter__(self):
		return [ self.school, 
				 self.college, 
				 self.course ] 

class PendingFile(models.Model):
	fid       =models.IntegerField(u'文件Fid',primary_key=True)
	fhash     =models.CharField(u'文件哈希值',max_length=50)
	uid       =models.IntegerField(u'上传者Uid')
	school    =models.CharField(u'所在大学',max_length=30)
	college   =models.CharField(u'所在学院',max_length=30)
	course    =models.CharField(u'所属课程',max_length=30)
	name      =models.CharField(u'标题',max_length=50)
	brief     =models.CharField(u'简介',max_length=200)
	filetype    =models.CharField(u'文件类型',max_length=10)
	extension   =models.CharField(u'文件扩展名',max_length=10)
	uploadtime  =models.DateTimeField(u'上传时间')
	size        =models.DecimalField(u'文件大小',max_digits=10, decimal_places=3)
	page         =models.IntegerField(u'文件页数')
	
	def __iter__(self):
		return [ self.fid] 

class LibraryFile(models.Model):
	fid       =models.IntegerField(u'文件Fid',primary_key=True)
	fhash     =models.CharField(u'文件哈希值',max_length=50)
	uid       =models.IntegerField(u'上传者Uid')
	school    =models.CharField(u'所在大学',max_length=30)
	college   =models.CharField(u'所在学院',max_length=30)
	course    =models.CharField(u'所属课程',max_length=30)
	name      =models.CharField(u'标题',max_length=50)
	brief     =models.CharField(u'简介',max_length=200)
	filetype    =models.CharField(u'文件类型',max_length=10)
	extension   =models.CharField(u'文件扩展名',max_length=10)
	uploadtime  =models.DateTimeField(u'上传时间')
	size        =models.DecimalField(u'文件大小',max_digits=10, decimal_places=3)
	page        =models.IntegerField(u'文件页数')
	
	download    =models.IntegerField(u'下载次数')
	price       =models.IntegerField(u'价格')
	isfavourite =models.IntegerField(u'是否本人上传')
	
	def __iter__(self):
		return [ self.fid] 