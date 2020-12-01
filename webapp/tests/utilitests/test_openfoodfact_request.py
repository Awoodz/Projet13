import requests

from webapp.utilities.api.externals.openfoodfact_request import Openfoodfact_request


class MockResponse:
    @staticmethod
    def json():
        return {"mock": "fake"}


def test_does_openfoodfact_class_makes_product_requests(monkeypatch):
    def mock_request(mock):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_request)

    mock_result = Openfoodfact_request.product_request("mock1")
    print(mock_result)
    assert mock_result["mock"] == "fake"


def test_does_openfoodfact_class_makes_category_requests(monkeypatch):
    def mock_request(mock):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_request)

    mock_result = Openfoodfact_request.category_request("mock1", "mock2")
    print(mock_result)
    assert mock_result["mock"] == "fake"
