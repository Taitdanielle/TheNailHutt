from django import forms


class PartiesForm(forms.Form):
    """
    A form for parties page
    """

    full_name = forms.CharField(
         label="Full Name"
    )
    email = forms.EmailField(
        label="Email"
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "rows": 8,
        })
    )

    class Meta:
        fields = ['full_name', 'email', 'message']