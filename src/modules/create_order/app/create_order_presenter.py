from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from .create_order_usecase import CreateOrderUseCase
from .create_order_controller import CreateOrderController
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

def lambda_handler(event, context):
    repo = HackabeckasRepositoryMock()
    usecase = CreateOrderUseCase(repo=repo)
    controller = CreateOrderController(usecase=usecase)
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code,
        body=response.body,
        headers=response.headers
    )
    return httpResponse.toDict()
    