from webapp.utilities.api.product_data import Product_data

fakejson = {
    "code": "fakecode",
    "product": {
        "product_name_fr": "fakeprod",
    }
}


def test_product_data():
    product = Product_data(fakejson)
    assert product.product_id == "fakecode"
    assert product.name == "fakeprod"
    assert product.url == "https://fr.openfoodfacts.org/produit/fakecode"
