#coding:utf-8
from django.http import HttpResponse
from TestPlatform.models import IndexImage,Course,User,LibraryFile,MyCollection,MyUploaded,PendingFile

from django.shortcuts import render
import json

import decimal
class DecimalJSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			return str(o)
		return super(DecimalJSONEncoder, self).default(o)

import urllib
from django.db import models
from django.core.exceptions import ObjectDoesNotExist



'''
自在悦学的主页-----此函数已处理好
'''
def index(request):
	return render(request, 'index.html')

'''
返回显示在主页的图片Url以及点击图片所链接的Url-----此函数已处理好
'''
def getPictures(request):
	List = list(IndexImage.objects.values('imageUrl','onclickUrl'))
	return HttpResponse(json.dumps(List,ensure_ascii=False))

'''
返回所有学校所有学院所有的课程-----此函数已处理好
'''
def getLists(request):
	List_school= list(Course.objects.values('school').distinct())
	for school_item in List_school:
		List_college = list(Course.objects.filter(school=school_item['school']).distinct().values('college'))
		
		for college_item in List_college:
			List_course = list(Course.objects.filter(school=school_item['school'],college=college_item['college']).distinct().values('course'))
			temp=[]
			for course_item in List_course:
				temp.append(course_item['course'])
			college_item['name']=college_item['college']
			del college_item['college']
			college_item['course']=temp
			
		school_item['college']=List_college

	return HttpResponse(json.dumps(List_school,ensure_ascii=False))

'''
返回用户的信息-----此函数已处理好
'''
def getUserDetail(request):
	UID = request.GET.get('uid')
	List = list(User.objects.filter(uid=UID).values('name','level','point','school','college'))
	#将List列表中的每一个字典中的每一个键值对转化为字符串类型
	for item in List:
		item['point']=str(item['point'])
		item['level']=str(item['level'])
	return HttpResponse(json.dumps(List,ensure_ascii=False))

'''
获取用户的收藏列表-----此函数已处理好
'''
def getFavourites(request):
	UID = request.GET.get('uid')

	List = list(MyCollection.objects.filter(uid=UID).values('fid'))

	Res=[]

	for item in List:
		Res.append(getFileDetail(item['fid']))

	return HttpResponse(json.dumps(Res,ensure_ascii=False,cls=DecimalJSONEncoder))

'''
获取用户的上传列表-----此函数已处理好
'''
def getUploads(request):
	UID = request.GET.get('uid')

	List = list(MyUploaded.objects.filter(uid=UID).values('fid'))

	Res=[]

	for item in List:
		Res.append(getFileDetail(item['fid']))
	
	

	return HttpResponse(json.dumps(Res,ensure_ascii=False,cls=DecimalJSONEncoder))

'''
根据fid，返回一个字典，表示该文件的文件详情-----此函数已处理好
'''
def getFileDetail(FID):
	List = list(LibraryFile.objects.filter(fid=FID).values('fid','price','name','brief','uid','size','page','download','isfavourite'))
	
	if len(List)>0:
		UID=List[0]['uid']
		List_User = list(User.objects.filter(uid=UID).values('name'))
		if len(List_User)>0:
			nickname=List_User[0]['name']
			
			for item in List:
				del item['uid']
				item['source']=nickname

			#将List列表中的每一个字典中的每一个键值对转化为字符串类型
			for item in List:
				item['fid']=str(item['fid'])
				item['price']=str(item['price'])
				item['size']=str(item['size'])+'m'
				item['page']=str(item['page'])
				item['download']=str(item['download'])
				item['isfavourite']=str(item['isfavourite'])
			return List[0]
	else:
		temp=[]
		return temp

'''
根据学校，学院，课程查询所有相关的文件详情-----此函数已处理好
'''
def getArticles(request):
	school=request.GET.get('school')
	college=request.GET.get('college')
	course=request.GET.get('course')

	List = list(LibraryFile.objects.filter(school=school,college=college,course=course).values('fid'))

	Res=[]

	for item in List:
		Res.append(getFileDetail(item['fid']))
	
	

	return HttpResponse(json.dumps(Res,ensure_ascii=False,cls=DecimalJSONEncoder))

'''
更改用户的学校和学院-----此函数已处理好
'''
def setCollege(request):
	school=request.GET.get('school')
	college=request.GET.get('college')
	UID=request.GET.get('uid')

	temp=User.objects.get(uid=UID)


	temp.school=school
	temp.college=college
	temp.save()

	flag="yes"

	return HttpResponse('{"status":"yes"}')

'''
用户增加一个文件到自己的收藏列表中
'''
def addFavourite(request):
	uid=request.GET.get('uid')
	fid=request.GET.get('fid')
	intuid=int(uid)
	intfid=int(fid)

	try:
		MyCollection.objects.get(uid=intuid,fid=intfid)
	except ObjectDoesNotExist:
		temp=MyCollection(uid=intuid,fid=intfid)
		temp.save()
		return HttpResponse('{"status":"yes"}')
	else:
		return HttpResponse('{"status":"no"}')

'''
用户从自己的收藏列表中删除一个文件
'''
def rmFavourite(request):
	uid=request.GET.get('uid')
	fid=request.GET.get('fid')
	intuid=int(uid)
	intfid=int(fid)

	try:
		MyCollection.objects.get(uid=intuid,fid=intfid)
	except ObjectDoesNotExist:
		return HttpResponse('{"status":"no"}')
	else:
		temp=MyCollection.objects.get(uid=intuid,fid=intfid)
		temp.delete()
		return HttpResponse('{"status":"yes"}')














