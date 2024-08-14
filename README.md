======Project OverView======
In appAuth app of backend development, I implemented Register, Login, Logout, Reset Password by email verification and implemented Register and Login functionality JWT authentication.
So, a user can Register, Login, Logout, Reset account Password.
I appApi app, I implemented Product List, Create, Update, Delete, Retrieve functionality and Search product functionality.

In frontend development, I implemented Register, Login, Logout, Product Show, Product Create, Product Delete, Product Update, Product Delete according to my backend api.
An unauthorized user can only show Product List and Product Details. An authorized user can use every functionality.


======Technologies=======
Backend - Django Rest Framework, SQLite
Frontend - ReactJs, CSS, Tailwind CSS, FontAwesome
Render tools - "on render" for backend development and "netlify" for frontend developmet

 =======Backend Setup Instruction========
1. pip install djangorestframework
2. pip install drf-spectacular
3. pip install djangorestframework-simplejwt
4. pip install -U django-jazzmin
5. python -m pip install django-cors-headers

======Frontend Setup Instruction=========
I am sharing a file of package.json, for run the frontend code this component should be installed-
https://docs.google.com/document/d/1C7anB_fweniRMTUzvMKRAmvZxhqQIlwkW5m5nBlkBZ0/edit?usp=sharing

=======test backend code======
As I used drf_spectacular in backend develepment, in local host/ deploy host their will show api endpoint. I am sharing image-
![image](https://github.com/user-attachments/assets/c32ef398-657c-4cf9-aaec-b59e20c9deeb)

1. Click to the "Try it out"
![image](https://github.com/user-attachments/assets/015fcb38-ef44-472b-9852-b10a7f991fe2)

2. And give the value as shown in below picture, the click to the execute button and you will see the response-
![image](https://github.com/user-attachments/assets/9d9918a4-239a-4f68-9cc0-8afbf6cbaf31)

=======test frontend ======
1. An authorized user can cerate, delete and update the product. unauthorized user only can view product list and product details




