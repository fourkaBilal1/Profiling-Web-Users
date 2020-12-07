from django.shortcuts import render,redirect
from account.models import Account
from company.models import Company,Ad
import random


def home_screen_view(request):


	if(request.user.is_authenticated):
		context = {}
		accounts = Account.objects.all()
		context["accounts"] = accounts
		context["images"] = []
		companiesx = Company.objects.all()
		companiesx = random.sample(list(companiesx),6)
		companies = []

		for company in companiesx: 
			i= random.randint(1, 6)
			ad_element = random.sample(list(Ad.objects.filter(Company_id=company.id)),1)
			# ad_element = random.sample(list(company.ad),1)
			print(" ad element :  ",ad_element)
			context["images"].append("ads/{}/{}{}.png".format(company,company,i))
			company.image = "ads/{}/{}{}.png".format(company,company,int(ad_element[0].ad_path.split(".")[0][-1]))
			company.user_id = request.user.id
			company.ad_id = ad_element[0].id
			companies.append(company)
		context["list"] = companies
		print("heere")
		return render(request, "personal/home.html",context)
	else:
		return redirect("login")
	
	

