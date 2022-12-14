from src.shared.helpers.http.http_models import HttpRequest
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.create_order.app.create_order_usecase import CreateOrderUseCase
from src.modules.create_order.app.create_order_controller import CreateOrderController

class TestCreateOrderController:
    def test_create_order_controller(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "tableNumber" : "1",
                "numberOfPeople" : "1",
                "flavor" : "CALABRESA",
                "border" : "CATUPIRY"
            }
        ) 
        response = controller(request=request)
        assert response.status_code == 201

    def test_create_order_controller_border_is_missing(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "tableNumber" : "1",
                "numberOfPeople" : "1",
                "flavor" : "CALABRESA"
            }
        ) 
        response = controller(request=request)
        assert response.status_code == 201
        
    def test_create_order_controller_orderId_is_missing(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "tableNumber" : "1",
                "numberOfPeople" : "1",
                "flavor" : "CALABRESA",
                "border" : "CATUPIRY"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field orderId is missing'
    
    def test_create_order_controller_tableNumber_is_missing(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "numberOfPeople" : "1",
                "flavor" : "CALABRESA",
                "border" : "CATUPIRY"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field tableNumber is missing'
    
    def test_create_order_controller_numberOfPeople_is_missing(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "tableNumber" : "1",
                "flavor" : "CALABRESA",
                "border" : "CATUPIRY"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
    def test_create_order_controller_flavor_is_missing(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "tableNumber" : "1",
                "numberOfPeople" : "1",
                "border" : "CATUPIRY"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field flavor is missing'

    def test_create_order_controller_orderId_not_decimal(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "Um",
                "tableNumber" : "1",
                "numberOfPeople" : "1",
                "flavor" : "CALABRESA",
                "border" : "CATUPIRY"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field orderId is not valid'
    def test_create_order_controller_orderId_not_decimal(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "tableNumber" : "Um",
                "numberOfPeople" : "1",
                "flavor" : "CALABRESA",
                "border" : "CATUPIRY"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field tableNumber is not valid'
    def test_create_order_controller_orderId_not_decimal(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "tableNumber" : "1",
                "numberOfPeople" : "Um",
                "flavor" : "CALABRESA",
                "border" : "CATUPIRY"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field numberOfPeople is not valid'
    def test_create_order_controller_flavor_not_enum(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "tableNumber" : "1",
                "numberOfPeople" : "1",
                "flavor" : "Vitor",
                "border" : "CATUPIRY"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field flavor is not valid'
    def test_create_order_controller_flavor_not_enum(self):
        repo = HackabeckasRepositoryMock()
        usecase = CreateOrderUseCase(repo=repo)
        controller = CreateOrderController(usecase=usecase)
        request = HttpRequest(
            body= {
                "orderId" : "1",
                "tableNumber" : "1",
                "numberOfPeople" : "1",
                "flavor" : "CALABRESA",
                "border" : "Vitor"
            }
        )
        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field border is not valid'
    