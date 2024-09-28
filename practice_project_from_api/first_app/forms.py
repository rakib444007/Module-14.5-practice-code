from django import forms 
import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
ch = [('b','Blue'),('g','Green'),('b','Black')]
CHOICES = (
    (1, "A"), 
    (2, "B"), 
    (3, "C"), 
    (4, "D"), 
    (5, "E"), 
)
class ContactForm(forms.Form):

    # date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    # name = forms.CharField(label='UserName' , help_text='Enter your Name' ,required=True)
    # comment = forms.CharField(widget=forms.Textarea)
    # email = forms.EmailField(label='Email')
    # agree = forms.BooleanField()
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # value = forms.DecimalField()
    # message= forms.CharField(max_length=10)
    # first_name = forms.CharField(initial='Rakibul Hasan')
    # day = forms.DateField(initial=datetime.date.today)
    # favorite_color = forms.ChoiceField(choices=ch)
    # favorite_color = forms.ChoiceField(choices=ch,widget=forms.RadioSelect)
    # favorite_color = forms.MultipleChoiceField(choices=ch,widget=forms.CheckboxSelectMultiple)
    # roll_number = forms.IntegerField(help_text='Enter 6 digit roll number ')
    # password = forms.CharField(widget=forms.PasswordInput())
    # Option = forms.TypedChoiceField(choices=CHOICES, coerce=str)
    # Duration = forms.DurationField()
    # file  = forms.FileField()
    # file = forms.FilePathField('./first_app/upload/')
    # FloatValue= forms.FloatField()
    # file = forms.ImageField()
    # Name = forms.RegexField(regex = "R.*b") 
    # EnterTime = forms.TimeField()
    EnterUrl = forms.URLField()



class PasswordValidationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        clean_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_compass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_pass != val_compass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError('Name must be at least 15 characters')




