from django.db import models



class Company(models.Model):
	name				= models.CharField(max_length=200)
	category 			= models.CharField(max_length=100)

	def __str__(self):
		return self.name
	class Meta:
	    verbose_name_plural = "Companies"

class Ad(models.Model):
	Company 			= models.ForeignKey(Company,on_delete=models.CASCADE)
	ad_path 			= models.CharField(max_length=200)
	def __str__(self):
		return self.ad_path
	class Meta:
	    verbose_name_plural = "Ads"

class Click(models.Model):
	user_id 			= models.IntegerField()
	company_id 			= models.IntegerField()
	ad_id				= models.IntegerField()
	date_click			= models.DateTimeField(verbose_name="date_click",auto_now_add=True)
	def __str__(self):
		return "{}|{}|{}".format(self.user_id,self.company_id,self.ad_id)
	class Meta:
	    verbose_name_plural = "Clicks"
