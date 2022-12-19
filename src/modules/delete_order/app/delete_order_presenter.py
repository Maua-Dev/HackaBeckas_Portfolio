from .delete_order_controller import DeleteOrderController
from .delete_order_usecase import DeleteOrderUsecase
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.shared.helpers.http.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

def lambda_handler(event, context):
    repo = HackabeckasRepositoryMock()
    usecase = DeleteOrderUsecase(repo=repo)
    controller = DeleteOrderController(usecase=usecase)
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code,
        body=response.body,
        headers=response.headers
    )
    return httpResponse.toDict()

    