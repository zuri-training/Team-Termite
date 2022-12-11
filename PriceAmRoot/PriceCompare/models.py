from django.db import models

# Create your models here.
class user(models.Model):
    first_name =models.CharField(max_length =200, null = True)
    last_name =models.CharField(max_length =200, null = True)
    user_name =models.CharField(max_length =200, null = True)
    email =models.EmailField(max_length =200, null = True)
    password =models.CharField(max_length =200, null = True)
    user_id =models.BigAutoField(primary_key=True)
    date_joined =models.DateField(max_length =200, null =True)

    def __str__(self):
        return self.first_name,self.last_name 


class product(models.Model):
    product_id =models.BigAutoField(primary_key =True)
    productname =models.CharField(max_length =200, null = True)
    productdescription =models.CharField(max_length =200, null = True)
    category_id =models.CharField(max_length =200, null = True)
    price =models.FloatField(max_length =200, null = True)

    def __str__(self):
        return self.productname

     
    
class category(models.Model):
    category_id =models.BigAutoField(primary_key = True)
    categoryname =models.CharField(max_length =200, null = True)
    user_id =models.ForeignKey(user,on_delete=models.CASCADE)

    def __str__(self):
        return self.categoryname

class Vendor(models.Model):
    vendor_id =models.BigAutoField(primary_key= True)
    vendor_link=models.URLField(max_length =200, null = True)
    category_id =models.ForeignKey(category,on_delete=models.CASCADE)


class comment(models.Model):
    comment_id =models.BigAutoField(primary_key= True)
    comment =models.CharField(max_length=200,null = True)
    created_on =models.DateField(max_length=200,null = True)
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    product_id =models.ForeignKey(product,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    



