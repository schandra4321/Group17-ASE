from django import forms
from Auctions.models import *

'''

class AuctionCreationForm(forms.Form):
    category = forms.CharField(required=True)
    no_of_items = forms.IntegerField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        no_of_items = cleaned_data.get('no_of_items')

        if no_of_items > 20:
            self.add_error('no_of_items', 'Sorry, No Of Items Cannot Exceed 20 !')


class ItemDetailsForm(forms.Form):

    description = forms.CharField(required=True)
    item_name = forms.CharField(required=True)
    base_price = forms.FloatField(required=True)
    keywords = forms.CharField(required=True)

'''

'''
class ItemDetailsForm(forms.ModelForm):

    class Meta:
        model = Item_Details
        exclude = ['item_id']

class AuctionCreationForm(forms.ModelForm):

    class Meta:
        model = Auction_Details
        exclude = ['creator_id','auction_id']

class KeywordInputForm(forms.ModelForm):

    class Meta:
        model = Keywords

'''

class AuctionCreationForm(forms.ModelForm):

    class Meta:
        model = Auction
        exclude = ['creator']


class ItemDetailsForm(forms.ModelForm):

    class Meta:
        model = Item
        #exclude = ['bidder','updated_price','status','item']
        fields = ['item_name','base_price','description','keywords']
        widgets = {
            'item_name': forms.TextInput(attrs={'required': True}),
            'base_price': forms.TextInput(attrs={'required': True}),
            'description': forms.TextInput(attrs={'required': True}),
            'keywords':forms.TextInput(attrs={'required': True}),
        }
    def clean(self):

        cleaned_data = super().clean()
        keywords = cleaned_data.get('keywords')

        if keywords :
            if len(keywords.split(',') ) == 1:
                self.add_error('keywords','Enter More Than 1 Keyword')



