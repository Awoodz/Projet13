from webapp.utilities.api.requester import Requester
from webapp.utilities.api.externals.openfoodfact_request import Openfoodfact_request
import webapp.utilities.data as dt


def mock_openfoodfact_category_request(text, mock):
    return {"products": [{"_id": "12345"}, {"_id": "67890"},]}


def mock_openfoodfact_product_request(mock):
    return "i am a product !"


def test_product_id_requester_return_product_id_list(monkeypatch):
    monkeypatch.setattr(
        Openfoodfact_request, "category_request", mock_openfoodfact_category_request
    )
    monkeypatch.setattr("webapp.utilities.data.MAX_PAGE", 1)
    assert Requester.product_id_requester("self", "fake_txt") == ["12345", "67890"]


def test_product_data_requester_get_product_data(monkeypatch):
    monkeypatch.setattr(
        Openfoodfact_request, "product_request", mock_openfoodfact_product_request
    )
    assert Requester.product_data_requester("mock") == "i am a product !"
