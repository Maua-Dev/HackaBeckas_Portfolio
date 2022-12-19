from .delete_order_viewmodel import DeleteOrderViewmodel
from .delete_order_usecase import DeleteOrderUsecase
from src.shared.helpers.errors.domain_errors import EntityError, TypeError
from src.shared.helpers.http.http_models import BadRequest, HttpRequest, HttpResponse, OK, InternalServerError, NotFound
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter

class DeleteOrderController:
    def __init__(self, usecase: DeleteOrderUsecase):
        self.usecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.body.get('orderId') == None:
                raise MissingParameters('orderId')
            if type(request.body.get('orderId')) != str:
                raise WrongTypeParameter(
                    fieldName="orderId",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.body.get('orderId').__class__.__name__
                )
            if not request.body["orderId"].isdecimal():
                raise EntityError('orderId')
            
            order = self.usecase(orderId=int(request.body.get('orderId')))
            viewmodel = DeleteOrderViewmodel(order=order)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err.args[0])