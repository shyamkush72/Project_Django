from django.db import models
from django.contrib.auth.models import User



STATE_CHOICES = (('Andaman & Nicobar','Andaman & Nicobar'),
                 ('Andhra Pradesh','Andhra Pradesh'),
                 ('Arunachal Pradesh','Arunachal Pradesh'),
                 ('Assam','Assam'),
                 ('Bihar','Bihar'),
                 ('Chhatisgarh','Chhatisgarh'),
                 ('Goa','Goa'),
                 ('Gujarat','Gujarat'),
                 ('Haryana','Haryana'),
                 ('Himachal Pradesh','Himachal Pradesh'),
                 ('Jammu and Kashmir','Jammu and Kashmir'),
                 ('Jharkhand','Jharkhand'),
                 ('Karnataka','Karnataka'),
                 ('kerala','kerala'),
                 ('Madhya Pradesh','Madhya Pradesh'),
                 ('Maharashtra','Maharashtra'),
                 ('Manipur','Manipur'),
                 ('Meghalaya','Meghalaya'),
                 ('Mizoram','Mizoram'),
                 ('Nagaland','Nagaland'),
                 ('Odisha','Odisha'),
                 ('Punjab','Punjab'),
                 ('Rajasthan','Rajasthan'),
                 ('Sikkim','Sikkim'),
                 ('Tamil Nadu','Tamil Nadu'),
                 ('Telangana','Telangana'),
                 ('Tripura','Tripura'),
                 ('Uttar Pradesh','Uttar Pradesh'),
                 ('Uttarakhand','Uttarakhand'),
                 ('West Bengal','West Bengal'),
                 ('Chandigarh','Chandigarh'),
                 ('Dadra & Haveli','Dadra & Haveli'),
                 ('Daman and Diu','Daman and Diu'),
                 ('pondicherry','pondicherry')
                 )

CATEGORY = (
    ('M','MOBILE'),
    ('L','LAPTOP'),
    ('TW','TOP WEAR'),
    ('BW','BOTTOM WEAR'),
    )


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    
    def __str__(self):
        return str(self.id) 
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY,max_length=10)
    product_image = models.ImageField(upload_to='media\product') 
    
    def __str__(self):
        return str(self.id)   
    
    
    
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    
    def totalCost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = ( ('Accepted','Accepted'),
                   ('Packed','Packed'),
                   ('On the way','On the way'),
                   ('Delivered','Delivered'),
                   ('Cancelled','Cancelled'),
                   
                  )    
    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES,max_length=100,default='pending')
    
    def totalCost(self):
        return self.quantity * self.product.discounted_price