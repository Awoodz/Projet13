from dal import autocomplete
from django import forms

from prodapp.models import IndustrialProduct


class ProductForm(forms.ModelForm):
    """autocomplete search form"""

    product_search = forms.ModelChoiceField(
        label=False,
        queryset=IndustrialProduct.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="autocomplete",
            attrs={
                # Set some placeholder
                "data-placeholder": "Recherchez un produit",
                # Only trigger autocompletion after 3 character has been typed
                "data-minimum-input-length": 3,
            },
        ),
    )

    class Meta:
        model = IndustrialProduct
        fields = ("product_search",)

