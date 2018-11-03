from django.db import models
from Users.models import Profile,User
# Create your models here.

'''
class Auction_Details(models.Model):

    auction_id = models.IntegerField(blank=False, unique=True, db_index=True)
    creator_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.CharField(blank=False, max_length=20)
    scheduled_date = models.DateTimeField(blank=False)

class Auction_Bidder(models.Model):

    auction_id = models.ForeignKey(Auction_Details, on_delete=models.CASCADE)
    bidder_id = models.ForeignKey(Profile,  on_delete=models.CASCADE)

class Item_User(models.Model):

    auction_id = models.ForeignKey(Auction_Details, on_delete=models.CASCADE)
    item_id = models.IntegerField(blank=False)
    bidder_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.BinaryField(blank=False,default=0)
    updated_price = models.FloatField(blank=False)

class Item_Details(models.Model):

    item_id = models.ForeignKey(Item_User,on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    item_name = models.CharField(max_length=20, blank=False)
    status = models.BinaryField(blank=False,default=0)
    base_price = models.FloatField(blank=False)

class Keywords(models.Model):

    item_id = models.ForeignKey(Item_Details, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=20, blank=False)

'''



class Auction(models.Model):

    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()

    OPTIONS = (
        ('1', 'Electronics'),
        ('2', 'Automobiles'),
        ('3', 'Fashion'),
        ('4', 'Sports'),
        ('5', 'Art'),
        ('6', 'Books'),
        ('7', 'Furniture'),
        ('8', 'Antiques'),
        ('9', 'Musical Equipment'),
        ('10', 'Industrial Equipment'),
        ('11', 'Gaming'),
        ('12', 'Stationary'),
        ('13', 'Industrial Equipment'),
        ('14', 'Gaming'),
        ('15', 'Jewellery'),
        ('16', 'Miscellaneous'),
    )

    category = models.CharField(max_length=200, choices=OPTIONS)

class AuctionBidders(models.Model):

    auction = models.OneToOneField(Auction,on_delete=models.CASCADE,null=True)
    bidders = models.ForeignKey(Profile,on_delete=models.CASCADE)




class ItemSet(models.Model):
    ItemList = models.OneToOneField(Auction,on_delete=models.CASCADE)

class Item(models.Model):

    item = models.ForeignKey(ItemSet, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=40,null=True)
    description = models.TextField()
    base_price = models.FloatField()
    keywords = models.CharField(max_length=255)
    status = models.BinaryField(default=False)
    updated_price =  models.FloatField(default=0,blank=False)
    bidder = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.item