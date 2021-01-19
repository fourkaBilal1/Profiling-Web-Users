from django.db import models

# PRIORITY = [("L","Low"),
# 			("M","Medium"),
# 			("H","High")]

# class Question(models.Model):
# 	title 		= models.CharField(max_length=68)
# 	question 	= models.TextField(max_length=400)
# 	priority 	= models.TextField(max_length=1,choices=PRIORITY)

# 	def __str__(self):
# 		return self.title
# 	class Meta:
# 		verbose_name = "The Question"
# 		verbose_name_plural = "Peoples Questions"

class Search_input(models.Model):
	user_id 			= models.IntegerField()
	Text				= models.CharField(max_length=200)
	date_search			= models.DateTimeField(verbose_name="date_search",auto_now_add=True)

	def __str__(self):
		return "{} | {}".format(self.user_id,self.Text)
	class Meta:
	    verbose_name_plural = "Search_inputs"





