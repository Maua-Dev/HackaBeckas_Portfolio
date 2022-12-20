from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from .get_order_controller import GetOrderController
from .get_order_usecase import GetOrderUsecase

def lambda_handler(event, context):
    repo = HackabeckasRepositoryMock()
    usecase = GetOrderUsecase(repo=repo)
    controller = GetOrderController(usecase=usecase)
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    return httpResponse.toDict()
    
