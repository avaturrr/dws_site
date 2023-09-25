from django import forms


class OrderForm(forms.Form):
    company_name = forms.CharField(max_length=100, label="название организации")
    company_tax_id = forms.CharField(max_length=15, label="УНП")
    legal_adress = forms.CharField(widget=forms.Textarea, label="юридический адрес")
    post_adress = forms.CharField(widget=forms.Textarea, label="почтовый адрес")
    company_email = forms.EmailField(max_length=100, label="эл почта")
    phone_number = forms.CharField(max_length=100, label="телефон для связи")
    delivery_adress = forms.CharField(widget=forms.Textarea, label="адрес доставки")
    position = forms.CharField(max_length=200, label="должность для договора")
    position_name = forms.CharField(max_length=100, label="ФИО для договора")
    bank_details = forms.CharField(widget=forms.Textarea, label="банковские реквизиты")
    comments = forms.CharField(widget=forms.Textarea, label="комментарии к заказу")
