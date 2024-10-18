from django.urls import path, include
from . import views

urlpatterns = [

path('members/',views.retrieveAllMembers),
#path('memberLoyalty/',views.retrieveMemberLoyalty),
path('member/<int:id>',views.retrieveSingleMember),
path('validateMember/',views.validatelMember),
path('earn/<int:id>',views.earnRewards),
path('redeem/<int:id>',views.redeemRewards),

]