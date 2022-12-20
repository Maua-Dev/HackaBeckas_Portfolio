from src.shared.domain.entities.order import Order
from src.shared.domain.enums.flavor_enum import FLAVOR
from src.shared.domain.enums.border_enum import BORDER
from .create_order_viewmodel import CreateOrderViewModel
from .create_order_usecase import CreateOrderUseCase
from src.shared.helpers.http.http_models import Created, HttpRequest, HttpResponse, BadRequest, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.domain.entities.table import Table
from src.shared.domain.entities.pizza import Pizza

class CreateOrderController:
    createOrderUseCase : CreateOrderUseCase
    
    def __init__(self, usecase: CreateOrderUseCase):
        self.createOrderUseCase = usecase
    
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get("orderId") is None:
                raise MissingParameters('orderId')
            if request.body.get("tableNumber") is None:
                raise MissingParameters('tableNumber')
            if request.body.get("numberOfPeople") is None:
                raise MissingParameters('numberOfPeople')
            if request.body.get("flavor") is None:
                raise MissingParameters('flavor')
            if not request.body["orderId"].isdecimal():
                raise EntityError('orderId')
            if not request.body["tableNumber"].isdecimal():
                raise EntityError('tableNumber')
            if not request.body["numberOfPeople"].isdecimal():
                raise EntityError('numberOfPeople')
            
            flavors = [flavor.value for flavor in FLAVOR]
            if request.body["flavor"] not in flavors:
                raise EntityError('flavor')
            
            borders = [border.value for border in BORDER]
            if request.body.get("border") != None:
                if request.body.get("border") not in borders:
                    raise EntityError('border')

            tableParam = Table(tableNumber=int(request.body["tableNumber"]), numberOfPeople=int(request.body["numberOfPeople"]))
            
            pizzaParam = Pizza(flavor=FLAVOR[request.body["flavor"]],
                               border=None if request.body.get("border") == None else BORDER[request.body.get("border")])
            
            order = Order(orderId=int(request.body["orderId"]), table=tableParam, pizza=pizzaParam)
            
            viewmodel = CreateOrderViewModel(order=order)
            
            return Created(viewmodel.to_dict())
                
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])