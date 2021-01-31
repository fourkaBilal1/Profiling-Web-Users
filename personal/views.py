from django.shortcuts import render,redirect
from account.models import Account
from company.models import Company,Ad, Click
from personal.models import Search_input
import random
import requests
import json # will be needed for saving preprocessing details
import numpy as np # for data manipulation
import pandas as pd # for data manipulation
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

def home_screen_view(request):
	
	if(request.user.is_authenticated):

		context = {}
		accounts = Account.objects.all()
		Adsx = random.sample(list(Company.objects.all()),3)
		Ads = []
		Ads_id_used = []
		Ads_listf = []

		# redundancy up to 5 clicks 
		MostClickedAd = MostClickedAdFucntion(request.user.id)
		Ads.extend(AddAdToCompanies(request,2,[MostClickedAd]))
		for ADss in Ads:
			Ads_id_used.append(ADss.id)
		#Ads_id_used= Ads.values_list('id', flat=True)

		# Machine learning model on all users
		profile_classifier_result = getClassML(request.user.id)
		print(profile_classifier_result)
			
		while True:
			print("p")
			pp =[]
			Ads_listf = AddAdToCompanies(request,1,[profile_classifier_result["label"]])

			for ADss in Ads_listf:
				pp.append(ADss.id)
			print(pp)
			print("dd ",Ads_id_used)
			print(intersection(pp,Ads_id_used))
			if len(intersection(pp,Ads_id_used))==0:
				break

		Ads.extend(Ads_listf)
		Ads_id_used = []
		for ADss in Ads:
			Ads_id_used.append(ADss.id)
		#Ads_id_used= Ads.values_list('id', flat=True)

		while True:
			print("pp")
			pp =[]
			Ads_listf = AddAdToCompanies(request,3)

			for ADss in Ads_listf:
				pp.append(ADss.id)
			print(pp)
			print("dd ",Ads_id_used)
			print(intersection(pp,Ads_id_used))
			if len(intersection(pp,Ads_id_used))==0:
				break
		Ads.extend(Ads_listf)

		#Ads.extend(AddAdToCompanies(request,3))
		context["list"] = Ads
		context["user_id"] = request.user.id
		#print("heere")
		print(Ads)
		for ady in Ads:
			print(ady.id ," - ",ady.ad_path)
		return render(request, "personal/home.html",context)
	else:
		return redirect("login")

def search_view(request):
	context = {}
	print("search view")
	print(request.GET.get('search_text'))
	searched_text = request.GET.get('search_text')
	S = Search_input()
	S.user_id= request.user.id
	S.Text= searched_text
	S.save()
	context["searched_text"] = searched_text
	return render(request, "personal/search.html",context)

def AddAdToCompanies(request = None, Nb=1, category = list(Company.objects.all().values_list('category', flat=True))):
	# redundancy up to 5 clicks 
	#print("------")
	#print(category)
	company_list = Company.objects.filter(category__in = category)
	Ads = []
	Companies_IDS = company_list.values_list('id', flat=True)
	#print("companies ids")
	#print(Companies_IDS)
	AdList = list(Ad.objects.filter(Company_id__in = list(Companies_IDS) ))
	#print("AdList ********************************************************************")
	#print(AdList)
	for i in range(Nb):
		ad_element = [AdList.pop(random.randrange(len(AdList))) for _ in range(1)]
		#print(" ad element :  ",ad_element[0].ad_path)
		Ads.append(ad_element[0])
	return Ads

	
def getClassML(id):
	url = 'http://localhost:8000/api/v1/profile_classifier/predict'
	df_account = Account.objects.filter(id=id)
	df_account = pd.DataFrame([t.__dict__ for t in df_account ])
	df_account = df_account.drop(
	    ["password","is_admin","is_staff","is_superuser","is_active","email","username"], axis=1
	)
	df = df_account
	df_searched = Search_input.objects.filter(user_id=id)
	df_searched = pd.DataFrame([t.__dict__ for t in df_searched ])
	df_searched = df_searched.sort_values(by=['date_search'], ascending=False).drop_duplicates(subset=['user_id'])
	df = df.merge(df_searched.drop(['id'],axis=1),left_on="id",right_on="user_id",how="left")
	df['date_joined'] = pd.to_datetime(df['date_joined'])
	df['last_login'] = pd.to_datetime(df['last_login'])
	df['birthDate'] = pd.to_datetime(df['birthDate'])
	df['date_search'] = pd.to_datetime(df['date_search'])
	df['location'] = df.streetNumber.map(str) + " , " + df.streetName + " , " + df.postcode + " , " + df.city + " , " + df.country
	locator = Nominatim(user_agent="myGeocoder")
	df['locatioan'] = locator.geocode(df['location'][0])
	df['latitude'] = None
	df['longitude'] = None
	for i in range(len(df)):
	    #print("{} , {}".format(i,df['location'][i]))

	    if locator.geocode(df['location'][i]) == None:
	        #print("{} , {}".format(i,df['location'][i].split(', ', 1)[1]))
	        df['location'][i] = df['location'][i].split(', ', 1)[1]
	        if locator.geocode(df['location'][i]) == None:
	            df['location'][i] = df['location'][i].split(', ', 1)[1]
	            if locator.geocode(df['location'][i]) == None:
	                print()
	            else:
	                #print("found 2 {}".format(i))
	                location = locator.geocode(df['location'][i])
	                #print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
	                df['latitude'][i] = location.latitude
	                df['longitude'][i] = location.longitude
	        else:
	            #print("found 1 {}".format(i))
	            location = locator.geocode(df['location'][i])
	            #print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
	            df['latitude'][i] = location.latitude
	            df['longitude'][i] = location.longitude
	    else:
	        #print("found 0 {}".format(i))
	        location = locator.geocode(df['location'][i])
	        #print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
	        df['latitude'][i] = location.latitude
	        df['longitude'][i] = location.longitude
	df = df.drop(["city","country","streetName","streetNumber","location","locatioan"],axis=1)
	df["date_joined_year"] = df["date_joined"].dt.year
	df["date_joined_month"] = df["date_joined"].dt.month
	df["date_joined_week"] = df["date_joined"].dt.week
	df["date_joined_day"] = df["date_joined"].dt.day
	df["date_joined_hour"] = df["date_joined"].dt.hour
	df["date_joined_minute"] = df["date_joined"].dt.minute
	df["date_joined_dayofweek"] = df["date_joined"].dt.dayofweek

	df["last_login_year"] = df["last_login"].dt.year
	df["last_login_month"] = df["last_login"].dt.month
	df["last_login_week"] = df["last_login"].dt.week
	df["last_login_day"] = df["last_login"].dt.day
	df["last_login_hour"] = df["last_login"].dt.hour
	df["last_login_minute"] = df["last_login"].dt.minute
	df["last_login_dayofweek"] = df["last_login"].dt.dayofweek

	df["birthDate_year"] = df["birthDate"].dt.year
	df["birthDate_month"] = df["birthDate"].dt.month
	df["birthDate_week"] = df["birthDate"].dt.week
	df["birthDate_day"] = df["birthDate"].dt.day
	df["birthDate_hour"] = df["birthDate"].dt.hour
	df["birthDate_minute"] = df["birthDate"].dt.minute
	df["birthDate_dayofweek"] = df["birthDate"].dt.dayofweek

	df["date_search_year"] = df["date_search"].dt.year
	df["date_search_month"] = df["date_search"].dt.month
	df["date_search_week"] = df["date_search"].dt.week
	df["date_search_day"] = df["date_search"].dt.day
	df["date_search_hour"] = df["date_search"].dt.hour
	df["date_search_minute"] = df["date_search"].dt.minute
	df["date_search_dayofweek"] = df["date_search"].dt.dayofweek
	df = df.drop(['date_joined','last_login','birthDate','date_search','id','user_id'],axis=1)
	today = pd.to_datetime(str(datetime.now()))
	#print(today)
	df["date_click_year"] = today.year
	df["date_click_month"] = today.month
	df["date_click_week"] = today.week
	df["date_click_day"] = today.day
	df["date_click_hour"] = today.hour
	df["date_click_minute"] = today.minute
	df["date_click_dayofweek"] = today.dayofweek
	dt_json = df.loc[0].to_json()
	dt_json = json.loads(dt_json) 
	del dt_json['_state_x']
	del dt_json['_state_y']
	print("start  **************************************")
	x = requests.post(url, json= dt_json)
	print("finish **************************************")
	profile_classifier_result = json.loads(x.text)
	return profile_classifier_result
def MostSearchedAdFucntion(id):
	df_account = Account.objects.filter(id=id)
	df_account = pd.DataFrame([t.__dict__ for t in df_account ])
	df_searched = Search_input.objects.filter(user_id=id)
	df_searched = pd.DataFrame([t.__dict__ for t in df_searched ])
	df_searched = df_searched.sort_values(by=['date_search'], ascending=False).drop_duplicates(subset=['user_id'])
	df = df_account.merge(df_searched.drop(['id'],axis=1),left_on="id",right_on="user_id",how="left")
	df['date_joined'] = pd.to_datetime(df['date_joined'])
	df['last_login'] = pd.to_datetime(df['last_login'])
	df['birthDate'] = pd.to_datetime(df['birthDate'])
	df['date_search'] = pd.to_datetime(df['date_search'])
	today = pd.to_datetime(str(datetime.now()))
	df['ts'] = pd.Timestamp(df.date_search.values.astype(np.int64)[0])
	dateFromLastSearch = today - df['ts']
	print(dateFromLastSearch.dt.days[0])
	if dateFromLastSearch.dt.days[0] <= 10:
		print("we are less than 10 days")
		print("we will try to give you something that corresponds to your search")
	return None

def MostClickedAdFucntion(id):
	df_account = Account.objects.filter(id=id)
	df_account = pd.DataFrame([t.__dict__ for t in df_account ])

	df_click = Click.objects.filter(user_id=id)
	df_click = pd.DataFrame([t.__dict__ for t in df_click ])
	df_click = df_click.sort_values(by=['date_click'], ascending=False)

	df_company = Company.objects.all()
	df_company = pd.DataFrame([t.__dict__ for t in df_company ])
	df = df_company.merge(df_click,left_on="id",right_on="company_id")
	df.dtypes
	df = df.drop(['id_x','id_y'],axis=1).sort_values(by=['date_click'],ascending=False)
	df = df.head()
	df = df['category'].value_counts().reset_index()
	df = df['index'][0]
	print(df)

	return df


def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

