from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.delete_order.app.delete_order_usecase import DeleteOrderUsecase
from src.modules.delete_order.app.delete_order_viewmodel import DeleteOrderViewmodel
from src.modules.delete_order.app.delete_order_controller import DeleteOrderController



class Test_DeleteOrderController:
    
    def test_delete_order_controller(self):
        repo = HackabeckasRepositoryMock()
        lenBefore = len(repo.orders)
        usecase = DeleteOrderUsecase(repo=repo)
        controller = DeleteOrderController(usecase=usecase)
        request = HttpRequest(body={
            "orderId" : 2
        })
        response = controller(request=request)
        expected = {
            "orderId" : 2,
            "table" : {
                "numberOfPeople" : 4,
                "tableNumber" : 14
            },
            "pizza" : {
                "flavor" : "MUSSARELA",
                "border" : "CATUPIRY"
            },
            "message" : "The order has been deleted"
        }
        
        assert response.status_code == 200
        assert len(repo.orders) == lenBefore - 1
        assert response.body == expected
        
    def test_delete_order_no_items_found(self):
        repo = HackabeckasRepositoryMock()
        usecase = DeleteOrderUsecase(repo=repo)
        controller = DeleteOrderController(usecase=usecase)
        
        request = HttpRequest(body={
            "orderId" : 90210
        })
        response = controller(request=request)
        
        assert response.body == "No items found for orderId"
        assert response.status_code == 404
    
    def test_delete_order_missing_orderId(self):
        repo = HackabeckasRepositoryMock()
        usecase = DeleteOrderUsecase(repo=repo)
        controller = DeleteOrderController(usecase=usecase)

        request = HttpRequest(body={
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field orderId is missing"
    
    def test_delete_order_bad_request_str(self):
        repo = HackabeckasRepositoryMock()
        usecase = DeleteOrderUsecase(repo=repo)
        controller = DeleteOrderController(usecase=usecase)

        request = HttpRequest(body={
            "orderId" : "2"
        })
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == "orderId must be int"
        