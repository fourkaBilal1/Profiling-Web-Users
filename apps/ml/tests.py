from django.test import TestCase

from apps.ml.profile_classifier.random_forestN import RandomForestClassifierN

# add at the beginning of the file:
import inspect
from apps.ml.registry import MLRegistry

from django.test import TestCase
from rest_framework.test import APIClient

from apps.ml.profile_classifier.extra_treesN import ExtraTreesClassifierN



class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            'postcode': '54000', 
            'Text': 'five', 
            'latitude': 48.69127075918047, 
            'longitude': 6.1810051232421745, 
            'date_click_year': 2020, 
            'date_click_month': 11, 
            'date_click_week': 47, 
            'date_click_day': 17, 
            'date_click_hour': 15, 
            'date_click_minute': 45, 
            'date_click_dayofweek': 1, 
            'date_joined_year': 2020, 
            'date_joined_month': 11, 
            'date_joined_week': 46, 
            'date_joined_day': 14, 
            'date_joined_hour': 16, 
            'date_joined_minute': 42, 
            'date_joined_dayofweek': 5, 
            'last_login_year': 2021, 
            'last_login_month': 1, 
            'last_login_week': 53, 
            'last_login_day': 2, 
            'last_login_hour': 20, 
            'last_login_minute': 23, 
            'last_login_dayofweek': 5, 
            'birthDate_year': 2020, 
            'birthDate_month': 12, 
            'birthDate_week': 50, 
            'birthDate_day': 7, 
            'birthDate_hour': 18, 
            'birthDate_minute': 53, 
            'birthDate_dayofweek': 0, 
            'date_search_year': 2021, 
            'date_search_month': 1, 
            'date_search_week': 2, 
            'date_search_day': 13, 
            'date_search_hour': 15, 
            'date_search_minute': 12, 
            'date_search_dayofweek': 2
        }
        my_alg = RandomForestClassifierN()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K', response['label'])

    # def test_registry(self):
    #     registry = MLRegistry()
    #     self.assertEqual(len(registry.endpoints), 0)
    #     endpoint_name = "income_classifier"
    #     algorithm_object = RandomForestClassifier()
    #     algorithm_name = "random forest"
    #     algorithm_status = "production"
    #     algorithm_version = "0.0.1"
    #     algorithm_owner = "Bilal Fourka"
    #     algorithm_description = "Random Forest with simple pre- and post-processing"
    #     algorithm_code = inspect.getsource(RandomForestClassifier)
    #     # add to registry
    #     registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
    #                 algorithm_status, algorithm_version, algorithm_owner,
    #                 algorithm_description, algorithm_code)
    #     # there should be one endpoint available
    #     self.assertEqual(len(registry.endpoints), 1)

    def test_et_algorithm(self):
        input_data = {
            'postcode': '54000', 
            'Text': 'five', 
            'latitude': 48.69127075918047, 
            'longitude': 6.1810051232421745, 
            'date_click_year': 2020, 
            'date_click_month': 11, 
            'date_click_week': 47, 
            'date_click_day': 17, 
            'date_click_hour': 15, 
            'date_click_minute': 45, 
            'date_click_dayofweek': 1, 
            'date_joined_year': 2020, 
            'date_joined_month': 11, 
            'date_joined_week': 46, 
            'date_joined_day': 14, 
            'date_joined_hour': 16, 
            'date_joined_minute': 42, 
            'date_joined_dayofweek': 5, 
            'last_login_year': 2021, 
            'last_login_month': 1, 
            'last_login_week': 53, 
            'last_login_day': 2, 
            'last_login_hour': 20, 
            'last_login_minute': 23, 
            'last_login_dayofweek': 5, 
            'birthDate_year': 2020, 
            'birthDate_month': 12, 
            'birthDate_week': 50, 
            'birthDate_day': 7, 
            'birthDate_hour': 18, 
            'birthDate_minute': 53, 
            'birthDate_dayofweek': 0, 
            'date_search_year': 2021, 
            'date_search_month': 1, 
            'date_search_week': 2, 
            'date_search_day': 13, 
            'date_search_hour': 15, 
            'date_search_minute': 12, 
            'date_search_dayofweek': 2
        }
        my_alg = ExtraTreesClassifierN()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K', response['label'])
        
# class EndpointTests(TestCase):

#     def test_predict_view(self):
#         client = APIClient()
#         input_data = {
#             'postcode': '54000', 
#             'Text': 'five', 
#             'latitude': 48.69127075918047, 
#             'longitude': 6.1810051232421745, 
#             'date_click_year': 2020, 
#             'date_click_month': 11, 
#             'date_click_week': 47, 
#             'date_click_day': 17, 
#             'date_click_hour': 15, 
#             'date_click_minute': 45, 
#             'date_click_dayofweek': 1, 
#             'date_joined_year': 2020, 
#             'date_joined_month': 11, 
#             'date_joined_week': 46, 
#             'date_joined_day': 14, 
#             'date_joined_hour': 16, 
#             'date_joined_minute': 42, 
#             'date_joined_dayofweek': 5, 
#             'last_login_year': 2021, 
#             'last_login_month': 1, 
#             'last_login_week': 53, 
#             'last_login_day': 2, 
#             'last_login_hour': 20, 
#             'last_login_minute': 23, 
#             'last_login_dayofweek': 5, 
#             'birthDate_year': 2020, 
#             'birthDate_month': 12, 
#             'birthDate_week': 50, 
#             'birthDate_day': 7, 
#             'birthDate_hour': 18, 
#             'birthDate_minute': 53, 
#             'birthDate_dayofweek': 0, 
#             'date_search_year': 2021, 
#             'date_search_month': 1, 
#             'date_search_week': 2, 
#             'date_search_day': 13, 
#             'date_search_hour': 15, 
#             'date_search_minute': 12, 
#             'date_search_dayofweek': 2
#         }
#         classifier_url = "/api/v1/profile_classifier/predict"
#         response = client.post(classifier_url, input_data, format='json')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data["label"], "<=50K")
#         self.assertTrue("request_id" in response.data)
#         self.assertTrue("status" in response.data)


# {
#       "postcode": "54000", 
#       "Text": "five", 
#       "latitude": 48.69127075918047, 
#       "longitude": 6.1810051232421745, 
#       "date_click_year": 2020, 
#       "date_click_month": 11, 
#       "date_click_week": 47, 
#       "date_click_day": 17, 
#       "date_click_hour": 15, 
#       "date_click_minute": 45, 
#       "date_click_dayofweek": 1, 
#       "date_joined_year": 2020, 
#       "date_joined_month": 11, 
#       "date_joined_week": 46, 
#       "date_joined_day": 14, 
#       "date_joined_hour": 16, 
#       "date_joined_minute": 42, 
#       "date_joined_dayofweek": 5, 
#       "last_login_year": 2021, 
#       "last_login_month": 1, 
#       "last_login_week": 53, 
#       "last_login_day": 2, 
#       "last_login_hour": 20, 
#       "last_login_minute": 23, 
#       "last_login_dayofweek": 5, 
#       "birthDate_year": 2020, 
#       "birthDate_month": 12, 
#       "birthDate_week": 50, 
#       "birthDate_day": 7, 
#       "birthDate_hour": 18, 
#       "birthDate_minute": 53, 
#       "birthDate_dayofweek": 0, 
#       "date_search_year": 2021, 
#       "date_search_month": 1, 
#       "date_search_week": 2, 
#       "date_search_day": 13, 
#       "date_search_hour": 15, 
#       "date_search_minute": 12, 
#       "date_search_dayofweek": 2
# }