# How to Use
From the project's root directory, run the following command to launch the local server:
python manage.py runserver

From here you will be able to access each table and the data loaded onto it through https://127.0.0.1:8000/api/pt_main.
This page loads every record in the database.

Searches are now made through this URL path. Specific searches will be made via patent numbers as using the following path https://127.0.0.1:8000/api/pt_main/{patent number}. 

The app also has the functionality for dynamic field selection. In the URL of a search, there are two parameters, 'include' and 'exclude', which can be used to specify which fields/relations you would like to display in the search result, and those not specified are not displayed. To use these paremeters you must set exclude[]='field' if you want to exclude 'field' from the result, and similarly you would set include[]='field' to include a 'field' to the result (in the case 'field' is omitted for a certain reason). The include parameter takes priority over exclude.

This feature is also useful for the nested dynamic field selection of tables like abstract, claim, disclosure, etc. To specify the nested field of a relation, dot notation is used. For example to specify the claimstext field from the claim relation, this is done through claim.claimstext.

For example: http://127.0.0.1:8000/api/pt_main/3014017/?exclude[]=disclosure.*&include[]=disclosure.disclosuretext&exclude[]=interested_party will yield results such that it will return all fields relating to patent number 3014017, except the disclosure relation will only show its disclosuretext field, and the interested_party relation will be omitted.

Full Swagger documentation is available at https://127.0.0.1:8000/swagger/

To take full advantage of the API and utilize the multi-patent search functionality, the url pattern is slightly different. For example the following is a valid multi-patent search:
http://127.0.0.1:8000/api/pt_main/?patentnumber=3014011-3014015,3015000,3017012

This multi-patent search is also compatible with the dynamic field selection also, and can be chained with it using the & operator.

# Tables and How to Modify Them
In the models.py file under the patents directory, you will find a class for each model representing
a table in the PostgreSQL database. It is best that if you need to make modifications to the database, or the table structure that you do it by making changes to this file, and making the migrations (i.e. executing 'python manage.py makemigrations' then 'python manage.py migrate') opposed to making changes
through postgres. 

# Work-in Progress
We are working on developing a system that will continuously and automatically update our database with the weekly XML data so that the data accessible by the API is always up-to date.