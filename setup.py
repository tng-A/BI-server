"""
Install project requirements.
"""

from setuptools import setup, find_packages

setup(
    name="bi-server",
    version="0.1.1",
    description='Business Intelligence Backend Service',
    packages=find_packages(),  
    include_package_data=True,
    scripts=["manage.py"],
    install_requires=[
        "Django==2.2.4",
        "djangorestframework==3.10.2",
        "python-decouple==3.1",
        "dj-database-url==0.5.0",
        "whitenoise==4.1.3",
        "psycopg2-binary==2.8.3",
        "django-rest-swagger==2.1.2",
        "gunicorn==19.9.0",
        "django-cors-middleware==1.4.0",
        "whitenoise==4.1.3",
        "python-dateutil==2.8.0",
        "requests==2.22.0",
        "apscheduler==3.6.1",
        "django-cors-headers==3.1.0",
        "djangorestframework-jwt==1.11.0",
        "django-grappelli=="
    ]
)
