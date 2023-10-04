# How to Use
From the project's root directory, run the following command to launch the local server:
python manage.py runserver

From here you will be able to access each table and the data loaded onto it through https://127.0.0.1:8000/mainsearchpage

This page will bring up a search bar (to search based on patent numbers), where users can enter and search for records relating to a specified patent number. By default, results will yield the fields of the main table related to the given patent number, and will also pull records linked to the given patent number from the claim, priority claim, disclosure, abstract, ipc classification, and interested party relations.

The app also has the functionality for dynamic field selection. In the URL of a search, a 'fields' parameter can be used to specify which fields/relations you would like to display in the search result, and those not specified are not displayed. The fields parameter is designed to be a comma-separated list. For example: https://127.0.0.1:8000/ftsearch-main/?query=3014914&fields=patentnumber,apptypecode,claim will yield results for the fields patentnumber and apptypcode related to patent 3014914 and all related records in the claims relation.

The following urls can be used to access the relevant tables in their entirety. Note that these pages will take a long time to load, as it loads ALL the entries.
* https://127.0.0.1:8000/api/pt_main
* https://127.0.0.1:8000/api/pt_disclosure
* https://127.0.0.1:8000/api/pt_claim
* https://127.0.0.1:8000/api/pt_priority_claim
* https://127.0.0.1:8000/api/pt_interested_party
* https://127.0.0.1:8000/api/pt_ipc_classification
* https://127.0.0.1:8000/api/pt_abstract

# Tables and How to Modify Them
In the models.py file under the patents directory, you will find a class for each model representing
a table in the PostgreSQL database. It is best that if you need to make modifications to the database, or the table structure that you do it by making changes to this file, and making the migrations (i.e. executing 'python manage.py makemigrations' then 'python manage.py migrate') opposed to making changes
through postgres. 

# Work in Progress
Currently, to improve the API, the dynamic field selection should be selectable not just through manually typing each desired field into the URL as this would be inefficient and difficult for those who are not privy to all available fields. To remove this, we will work on adding checkbox forms to the search page for each field on the same page the searches are made.

We will also be working on adding dynamic field selection for the records pulled from each of the claim, disclosure, priority claim, interested party, ipc classification, and abstract relations. 