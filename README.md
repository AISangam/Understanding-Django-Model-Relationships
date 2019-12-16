# Understanding-Django-Model-Relationships
<strong>Understanding Django Model Relationships</strong>  

This small code will help you understand where to use ManyToManyField and where to use ForeignKey. AI Sangam tries hard to explain the concept by taking the example of a parent (father) which has multiple childrens and each child is playing different game. Please see the below screenshot to understand the things in a better way.  

<strong>Understanding Foreign key</strong>   

![ForeignKey_relationship](https://user-images.githubusercontent.com/35392729/70925652-9c9a0200-2051-11ea-9e3a-4961a8658b9b.png)  


<strong>Understanding ManyToManyField</strong>  

![Many_to_Many_relationship](https://user-images.githubusercontent.com/35392729/70925753-c94e1980-2051-11ea-8705-aa79d6f71213.png)  

For migrating databas, please execute below steps  

To migrate the tables which django provides by default, please execute the below command     
```
python3 manage.py migrate  
```
To make migrations for your created classes in the file model.py, please execute the below command  
```
python3 manage.py makemigrations  
```

To migrate user created classes, please execute the below command    

```
python3 manage.py migrate  
```  

Please see the below screenhots  

<strong>Django default tables migrate</strong>
  
![django_migrate](https://user-images.githubusercontent.com/35392729/70926032-5db87c00-2052-11ea-8e7c-043e4b416a6c.png)  

Make Migrations of newly created classes in file models.py  

![makemigrations](https://user-images.githubusercontent.com/35392729/70926155-9c4e3680-2052-11ea-8271-6a2a7190ca1b.png)  

Migrating new classes along with django tables  

![migrating_new_class](https://user-images.githubusercontent.com/35392729/70926190-aff99d00-2052-11ea-868f-04ae19c780cf.png)

## Creating Superuser  

To create Superuser, please execute the below command  
```
python3 manage.py createsuperuser  
```

## How to run the code  

```
python3 manage.py runserver  
```   

## Where to find the file manage.py  

Once you clone this repository, please open the path of this reposiotry in terminal and you will find the file manage.py. Please install all the requirements to run this code from the requirements.txt file provided along with this repository.  

Happy Coding!!!!

