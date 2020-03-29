from django.shortcuts import render,redirect
from shortener.models import UrlTable
from django.contrib.auth.models import User
import hashlib


def dashboard(request):
	user=request.user
	long_url=UrlTable.objects.filter(user=user)
	return render(request, "dashboard.html",{"long_url":long_url})


def hashurl(key): 
	m= hashlib.md5(key)
	return m.hexdigest()[:5]




def create_short_url(request):
	if request.method=="POST":
		title=request.POST.get("title")
		long_url=request.POST.get("long_url")
		user=request.user
		short_hash=hashurl(long_url.encode())

		links=UrlTable.objects.create(
			title=title,
			long_url=long_url,
			short_hash=short_hash,
			user=user
			)

		return redirect("/dashboard/")


def redirect_to_long_url(request,hashcode):
	url=UrlTable.objects.get(short_hash=hashcode)
	long_url=url.long_url
	url.no_clicks+=1
	url.save()

	return redirect(long_url)




