# How to Use
From the project's root directory, run the following command to launch the local server:
python manage.py runserver

From here you will be able to access each table and the data loaded onto it through https://127.0.0.1:8000/

The following urls can be used to access the relevant tables in their entirety. Note that these pages will take a long time to load, as it loads ALL the entries.
* https://127.0.0.1:8000/api/pt_main
* https://127.0.0.1:8000/api/pt_disclosure
* https://127.0.0.1:8000/api/pt_claim
* https://127.0.0.1:8000/api/pt_priority_claim
* https://127.0.0.1:8000/api/pt_interested_party
* https://127.0.0.1:8000/api/pt_ipc_classification
* https://127.0.0.1:8000/api/pt_abstract

To make page load times faster, there is a search function that has been implemented, so that the  entries that should be loaded can be filtered through first. Each table has its own search path that can be used as follows:
* https://127.0.0.1:8000/mainsearchpage
* https://127.0.0.1:8000/abstractsearchpage
* https://127.0.0.1:8000/claimsearchpage
* https://127.0.0.1:8000/disclosuresearchpage
* https://127.0.0.1:8000/priorityclaimsearchpage
* https://127.0.0.1:8000/interestedpartysearchpage
* https://127.0.0.1:8000/ipcsearchpage

Each page is set up with a search bar where queries can be entered and then loaded.

Keep in mind that in the views.py file in the patents directory, there is a function for each table's search functionality, each with it's own search_vector variable specifying the columns that each search term will be applied to. Not all of the columns are being searched through so as to reduce the time needed to perform a search, but also because for many tables, there are only a few columns that have information that can be valuably searched. Improvements can be made to make searching through all columns separately possible, along with filtering all entries by certain characteristics of different columns (i.e. there are some columns that contain values out of a set of a handful of different "codes").

# Tables and How to Modify Them
In the models.py file under the patents directory, you will find a class for each model representing
a table in the PostgreSQL database. It is best that if you need to make modifications to the database, or the table structure that you do it by making changes to this file, and making the migrations (i.e. executing 'python manage.py makemigrations' then 'python manage.py migrate') opposed to making changes
through postgres. 

# Deploying with Heroku
The Heroku official website has a good article on how to deploy a django app (https://devcenter.heroku.com/articles/getting-started-with-python), however in order to install Heroku it requires admin credentials. So a request must be made to install/use this software and deploy the app.