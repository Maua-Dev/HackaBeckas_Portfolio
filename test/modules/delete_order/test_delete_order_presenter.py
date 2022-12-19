import json
from src.modules.delete_order.app.delete_order_presenter import lambda_handler

class Test_DeleteOrderPresenter:

    def test_delete_order(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                    }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "http": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body" : '{"orderId" : "1", "tableNumber" : "1", "numberOfPeople" : "1", "flavor" : "CALABRESA", "border" : "CATUPIRY"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None 
        }
        
        expected = {'message': 'The order has been created', 
                    'orderId': 1, 
                    'pizza': {'border': 'CATUPIRY', 'flavor': 'CALABRESA'}, 
                    'table': {'numberOfPeople': 1, 'tableNumber': 1}}
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 201
        assert json.loads(response["body"]) == expected