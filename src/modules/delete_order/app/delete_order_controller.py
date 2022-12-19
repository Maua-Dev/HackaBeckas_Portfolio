from .delete_order_viewmodel import DeleteOrderViewmodel
from .delete_order_usecase import DeleteOrderUsecase
from src.shared.helpers.errors.domain_errors import EntityError, TypeError
from src.shared.helpers.http.http_models import BadRequest, HttpRequest, HttpResponse, OK, InternalServerError, NotFound
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters

class DeleteOrderController:
    def __init__(self, usecase: DeleteOrderUsecase):
        self.usecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('orderId') == None:
                raise MissingParameters('orderId')
            if type(request.body.get('orderId')) is not int:
                raise TypeError('orderId', 'int')
            
            order = self.usecase(orderId=request.body.get('orderId'))
            return OK(DeleteOrderViewmodel(order=order).to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except TypeError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])