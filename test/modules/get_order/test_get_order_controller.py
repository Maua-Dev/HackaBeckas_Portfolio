from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.shared.helpers.http.http_models import HttpRequest
from src.modules.get_order.app.get_order_controller import GetOrderController
from src.modules.get_order.app.get_order_usecase import GetOrderUsecase

class Test_GetOrderController:
    def test_get_order_controller(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        
        request = HttpRequest(query_params= {
                'orderId' : str(repo.orders[1].orderId)
            })
        
        response = controller(request=request)
        assert response.status_code == 200
        assert response.body['orderId'] == repo.orders[1].orderId
        assert response.body['table']['numberOfPeople'] == repo.orders[1].table.numberOfPeople
        assert response.body['table']['tableNumber'] == repo.orders[1].table.tableNumber
        assert response.body['pizza']['flavor'] == repo.orders[1].pizza.flavor.value
        assert response.body['pizza']['border'] == repo.orders[1].pizza.border.value
        
    def test_get_order_controller_missing_parameters(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        
        request = HttpRequest(query_params= {})
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field orderId is missing'
    
    def test_get_order_controller_wrong_type_parameter(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        
        request = HttpRequest(query_params= {
                'orderId' : 2
            })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "Field orderId isn't in the right type.\n Received: int.\n Expected: str"
        
    def test_get_order_controller_entity_error(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        
        request = HttpRequest(query_params= {
                'orderId' : 'JoaoBranco&VitorSoller'
            })
        
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field orderId is not valid'
        
    def test_get_order_controller_no_items_found(self):
        repo = HackabeckasRepositoryMock()
        usecase = GetOrderUsecase(repo=repo)
        controller = GetOrderController(usecase=usecase)
        
        request = HttpRequest(query_params= {
                'orderId' : '1914'
            })
        
        response = controller(request=request)
        assert response.status_code == 404
        assert response.body == 'No items found for orderId'