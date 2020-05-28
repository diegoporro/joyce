from django import forms


class Contact(forms.Form):
    Full_Name = forms.CharField(required=True, max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' ', }))
    Email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', }))
    Phone_number = forms.CharField(required=True, max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', }))
    Message = forms.CharField(required=True, max_length=200,
                                widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message...', }))

    def clean(self):
        Full_Name = self.cleaned_data.get("Full_Name")
        Email = self.cleaned_data.get("Email")
        Phone_number = self.cleaned_data.get("Phone_number")
        Message = self.cleaned_data.get("Message")

        return super(Contact, self).clean()
