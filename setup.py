from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
   name='wagtail2-ckeditor',
   version='2.0',
   description='CKEditor widget for Wagtail 2 CMS',
   author='Maxime Klampas',
   author_email='mklampas@gmail.com',
   packages=['wagtail2_ckeditor'],
   install_requires=['wagtail'],
)
