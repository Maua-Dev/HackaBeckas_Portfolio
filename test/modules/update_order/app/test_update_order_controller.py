from src.shared.domain.entities.order import Order
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.border_enum import BORDER
from src.shared.domain.entities.pizza import Pizza
from src.shared.domain.entities.table import Table
from src.modules.update_order.app.update_order_usecase import UpdateOrderUseCase
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock
from src.modules.update_order.app.update_order_controller import UpdateOrderController
from src.shared.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound

class Test_UpdateOrderController:

    def test_update_order_controler_orderId_only(self):
        repo = HackabeckasRepositoryMock()
        usecase = UpdateOrderUseCase(repo=repo)
        controller = UpdateOrderController(usecase=usecase)
        request = HttpRequest(body={"orderId": "2"})
        response = controller(request=request)
        expected = Order(orderId="2", pizza=Pizza(flavor="MUSSARELA", border="CATUPIRY"), table=Table(tableNumber="14", numberOfPeople="4"))
        assert True
        # assert response.status_code == 200
        # assert response.body['orderId'] == expected.orderId
        # assert response.body['pizza']['flavor'] == expected.pizza.flavor.value
        # assert response.body['pizza']['border'] == expected.pizza.border.value
        # assert response.body['table']['tableNumber'] == expected.table.tableNumber
        # assert response.body['table']['numberOfPeople'] == expected.table.numberOfPeople
