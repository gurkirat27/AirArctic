from django import forms
from .models import Passengers, CardDetails, Booking, Passport, Baggage, CheckIn

class PassangersForm(forms.ModelForm):
    class Meta:
        model = Passengers
        fields = '__all__'

class CardDetailsForm(forms.ModelForm):
    class Meta:
        model = CardDetails
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = '__all__'

class BaggageForm(forms.ModelForm):
    class Meta:
        model = Baggage
        fields = '__all__'

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = '__all__'