# SECTION 6 - ADMIN  Data & Model SQL Query to database


- django-admin startproject book_store
- django-admin startapp book_outlet
- create file db.sqlite3
- build model class property in book_outlet - models.py
  ( reference in google : Django model reference fieldtypes )
- project setting - add installed apps
- do migrations, a feature for define steps for database
  
    "python manage.py makemigrations"
    to create migration file on apps - migrations will creted

    "python manage.py migrate"
    to execute migration file

- run interactive shell to work with database
    "python manage.py shell"
    ( make sure you run this command on rigth project folder )

- Import model class
    "from book_outlet.models import Book"

- add a data 
    harry_potter = Book(title="Harry Potter 1 - Th Philoshoper's Stone", rating=7)

- run build in save method
    "harry_potter.save()"
    python in background will make a query like INSERT INTO books ( title, rating ) VALUES ( "Harry Potter 1 - Th Philoshoper's Stone", 7 )

- get query data object
    Book.objects.all()

# Routing & View
1. Create Template folder and file.html for view, and call if there is a base html
2. add class/function on view.py that reference to its file.html
3. create the url.py file on apps project that routing the url with the class/function in the view.py
4. call the all apps urls.py on root urls.py project

- Call the model on view app

# SECTION 7 - ADMIN 

- python manage.py createsuperuser
create username & password,
can pass password

- register Book models on :
app book_outlet folder - from .models import Book - admin.site.register(Book)


# SECTION 8 - Relations 

- One to Many
create class Author
and then connect the author on Book models
author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

- One to One
create class Address
and then connect the address on Author models
address = models.OneToOneField(Address, on_delete=models.SET, null=True)


- Many to Many
create class Country
and then connect the Country on Book models
published_countries = models.ManyToManyField(Country)