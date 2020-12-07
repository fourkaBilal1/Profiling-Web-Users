from django.shortcuts import render,redirect
from company.models import Company,Ad,Click
import random 

def getSixAds_view(request):
	context = {}
	companiesx = Company.objects.all()
	context["companies"] = random.sample(list(companiesx),6)
	context["images"] = []

	companies= ["cocacola","netflix","spotify","tesla","vichy","apple"]
	for company in companies:
		context["images"].append("ads/{}/{}1.png".format(company,company))

	return render(request, "personal/home.html",context)


def click_view(request,user_id,company_id,ad_id):
	context = {}
	c = Click()
	c.user_id= user_id
	c.company_id= company_id
	c.ad_id= ad_id
	c.save()
	print("user id: ",user_id,"   -  company id: ",company_id,"    -   ad id: ",ad_id)
	return redirect("home")