from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


def test_top_product():
    with open('products.csv', 'rb') as body:
        response = client.post("/top_product?name_column=product_name&rating_column=customer_average_rating", files={'file':('products.csv',  body, "application/vnd.ms-excel")})
        assert response.status_code == 200
        assert response.json() == [{"top_product":"Massoub gift card","product_rating":5.0}]

def test_top_product_wrong_file():
    with open('data.txt', 'rb') as body:
        response = client.post("/top_product?name_column=product_name&rating_column=customer_average_rating", files={'file':('data.txt',  body, "text/plain")})
        assert response.status_code == 400
        assert response.json() == {'detail': "Invalid data type"}

def test_top_product_empty_file():
    with open('empty.csv', 'rb') as body:
        response = client.post("/top_product?name_column=name&rating_column=rating", files={'file':('empty.csv',  body, "application/vnd.ms-excel")})
        assert response.status_code == 404
        assert response.json() == {'detail': "Invalid data"}

def test_top_product_no_data_file():
    with open('dataTest.csv', 'rb') as body:
        response = client.post("/top_product?name_column=name&rating_column=rating", files={'file':('dataTest.csv',  body, "application/vnd.ms-excel")})
        assert response.status_code == 404
        assert response.json() == {'detail': "Empty file - There is no data"}

def test_top_product_wrong_column():
    with open('products.csv', 'rb') as body:
        name_column='product_name'
        rating_column='rating'
        url='/top_product?name_column={}&rating_column={}'.format(name_column, rating_column)
        response = client.post(url, files={'file':('products.csv',  body, "application/vnd.ms-excel")})
        assert response.status_code == 404
        assert response.json() == {'detail': "Entered columns are not found in the data"}