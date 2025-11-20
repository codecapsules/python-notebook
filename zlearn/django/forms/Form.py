from django import forms


class PostCreateForm(forms.forms):
    STATUS_CHOICES = (
        ("draft", "draft"),
        ("inprogress", "in progress"),
        ("published", "published")
    )

    title      = forms.CharField(max_length=200)
    content    = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
    status     = forms.ChoiceField(choices=STATUS_CHOICES)
    word_count = forms.IntegerField()