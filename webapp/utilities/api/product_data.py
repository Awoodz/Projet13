from dictor import dictor


class Product_data:
    """Gathers product data"""

    def __init__(self, product_data):
        self.datas = product_data

    @property
    def product_id(self):
        return dictor(self.datas, "code")

    @property
    def url(self):
        return "https://fr.openfoodfacts.org/produit/" + dictor(
            self.datas,
            "code"
        )

    @property
    def name(self):
        return dictor(self.datas, "product.product_name_fr")
