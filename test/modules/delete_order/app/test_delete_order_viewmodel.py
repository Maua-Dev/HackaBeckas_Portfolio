from src.modules.delete_order.app.delete_order_viewmodel import DeleteOrderViewmodel
from src.shared.infra.repositories.hackabeckas_repository_mock import HackabeckasRepositoryMock


class Test_DeleteOrderViewmodel:
    def test_delete_order_viewmodel(self):
        repo = HackabeckasRepositoryMock()
        order = repo.orders[1]
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
        
        orderViewModel = DeleteOrderViewmodel(order).to_dict()
        
        assert orderViewModel == expected