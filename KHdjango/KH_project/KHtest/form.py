from django import forms

class BankdataForm(forms.Form):
	id = forms.IntegerField(
		widget=forms.Textarea(attrs={'rows':2,'class' : 'form-control', 'placeholder' : '編號\n(請輸入是第幾位訪客)'}))

	name = forms.CharField(max_length = 20,
		widget=forms.Textarea(attrs={'rows':2,'class' : 'form-control', 'placeholder' : '姓名\n(請輸入姓名)'}))

	age = forms.IntegerField(
		widget=forms.Textarea(attrs={'rows':2,'class' : 'form-control', 'placeholder' : '年齡\n(請輸入整數)'}))

	marital = forms.CharField(max_length = 20,
		widget=forms.Textarea(attrs={'rows':4,'class' : 'form-control', 'placeholder' : '婚姻狀況\n(請輸入其中一項：married,single,divorced,unknown)'}))

	education = forms.CharField(max_length = 20,
		widget=forms.Textarea(attrs={'rows':4,'class' : 'form-control', 'placeholder' : '教育程度\n(請輸入其中一項：MS,PhD,BS,unknown)'}))

	balance	= forms.IntegerField(
		widget=forms.Textarea(attrs={'rows':2,'class' : 'form-control', 'placeholder' : '存款餘額\n(請輸入整數)'}))

	housing = forms.CharField(max_length = 20,
		widget=forms.Textarea(attrs={'rows':2,'class' : 'form-control', 'placeholder' : '房貸\n(請輸入其中一項：yes,no,unknown)'}))

	loan = forms.CharField(max_length = 20,
		widget=forms.Textarea(attrs={'rows':2,'class' : 'form-control', 'placeholder' : '貸款\n(請輸入其中一項：yes,no,unknown)'}))

	duration = forms.IntegerField(
		widget=forms.Textarea(attrs={'rows':2,'class' : 'form-control', 'placeholder' : '上次電訪時間長度\n(請輸入秒數)'}))