from src.shared.domain.entities.table import Table
from src.shared.domain.entities.order import Order
from src.shared.domain.entities.pizza import Pizza
from .update_order_viewmodel import UpdateOrderViewModel
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.http.http_models import OK, BadRequest, Conflict, HttpRequest, HttpResponse, InternalServerError, NotFound
from .update_order_usecase import UpdateOrderUseCase
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.border_enum import BORDER

class UpdateOrderController:
    def __init__(self, usecase: UpdateOrderUseCase):
        self.updateOrderUseCase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get("orderId") is None:
                raise MissingParameters('orderId')

            order = self.updateOrderUseCase(
                orderId=request.body.get("orderId"), 
                new_flavor=FLAVOR[request.body.get("flavor")], new_border=None if request.body.get("border") == None else BORDER[request.body.get("border")], 
                new_table=int(request.body.get("tableNumber"), new_numberOfPeople=int(request.body.get("numberOfPeople"))))

            viewmodel = UpdateOrderViewModel(order)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except DuplicatedItem as err:
            return Conflict(body=err.message) 

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
