from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
    create_endpoint = "/store/order"
    created_payload = {"pet_id": 0}

    create_resp = api_helpers.post_api_data(create_endpoint, created_payload)
    assert create_resp.status_code == 201

    order = create_resp.json()
    assert "id" in  order
    order_id = order["id"]

    patch_endpoint = f"/store/order/{order_id}"
    patch_payload = {"status": "sold"}

    patch_resp = api_helpers.patch_api_data(patch_endpoint, patch_payload)
    assert patch_resp.status_code == 200

    body = patch_resp.json()

    assert "message" in body
    assert body["message"] == "Order and pet status updated successfully"
