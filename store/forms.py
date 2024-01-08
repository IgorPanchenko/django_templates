from django import forms

from store.models import Message


class MessageForm(forms.ModelForm):
    first_name = forms.CharField(label="имя",
                                widget=forms.TextInput(attrs={
                                                            "type":"text",
                                                            "class": "form-control",
                                                            "placeholder": "Имя"}))
    last_name = forms.CharField(label="фамилия",
                                widget=forms.TextInput(attrs={
                                                            "type":"text",
                                                            "class": "form-control",
                                                            "placeholder": "Фамилия"}))
    email = forms.EmailField(label="почтовый адрес",
                                widget=forms.EmailInput(attrs={
                                                            "type":"text",
                                                            "class": "form-control",
                                                            "placeholder": "Электронный адрес"}))
    message = forms.Field(label="сообщение",
                                widget=forms.Textarea(attrs={
                                                            "type":"text",
                                                            "class": "form-control",
                                                            "placeholder": "Сообщение",
                                                            "cols": "30",
                                                            "rows": "10"}))
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'message']
    

class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(label="Почтовый адрес",
                                widget=forms.EmailInput(attrs={
                                                            'type':"text",
                                                             'class':"form-control rounded-0 border-secondary text-white bg-transparent",
                                                             'placeholder':"Электронная почта",
                                                             'aria-label':"Введите адрес почты",
                                                             'aria-describedby':"button-addon2"}))