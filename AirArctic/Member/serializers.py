from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member

        fields = ['memberId', 'firstName', 'lastName', 'contactNumber', 'emailAddress', 'dateRegistered','rewardsLevel','totalPoints']



'''
class LoyaltySerializer(serializers.ModelSerializer):


    memberDetail = MemberSerializer(read_only=True)

    class Meta:
        model = LoyaltyProgram
        fields = ['id', 'memberDetail', 'rewardsLevel', 'totalPoints']
        
'''
