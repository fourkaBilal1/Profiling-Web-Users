"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier # import ExtraTrees ML algorithm
from apps.ml.profile_classifier.random_forestN import RandomForestClassifierN
from apps.ml.profile_classifier.extra_treesN import ExtraTreesClassifierN # import ExtraTrees ML algorithm
try:
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="ab_testing",
                            algorithm_version="0.0.1",
                            owner="Bilal Fourka",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
    # Extra Trees classifier
    et = ExtraTreesClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="ab_testing",
                            algorithm_version="0.0.1",
                            owner="Bilal Fourka",
                            algorithm_description="Extra Trees with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
    rfN = RandomForestClassifierN()
    # add to ML registry
    registry.add_algorithm(endpoint_name="profile_classifier",
                            algorithm_object=rfN,
                            algorithm_name="random forest N",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Bilal Fourka",
                            algorithm_description="Random Forest",
                            algorithm_code=inspect.getsource(RandomForestClassifierN))
    #Extra Trees classifier
    etN = ExtraTreesClassifierN()
    # add to ML registry
    registry.add_algorithm(endpoint_name="profile_classifier",
                            algorithm_object=etN,
                            algorithm_name="extra trees N",
                            algorithm_status="ab_testing",
                            algorithm_version="0.0.1",
                            owner="Bilal Fourka",
                            algorithm_description="Extra Trees",
                            algorithm_code=inspect.getsource(RandomForestClassifierN))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))