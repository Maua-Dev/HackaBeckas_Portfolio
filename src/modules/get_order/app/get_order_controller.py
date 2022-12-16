from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.modules.get_order.app.get_order_usecase import GetOrderUsecase
from src.shared.helpers.http.http_models import HttpRequest, HttpResponse, OK, NotFound, BadRequest, InternalServerError
from src.modules.get_order.app.get_order_viewmodel import GetOrderViewmodel

class GetOrderController:
    
    def __init__(self, usecase: GetOrderUsecase):
        self.usecase = usecase
        
    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get("orderId") is None:
                raise MissingParameters('orderId')
            if type(request.query_params.get('orderId')) != str:
                raise WrongTypeParameter(
                    fieldName="orderId",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.query_params.get('orderId').__class__.__name__
                )
            if not request.query_params["orderId"].isdecimal():
                raise EntityError('orderId')
            order = self.usecase(
                orderId=int(request.query_params.get('orderId'))
            )
            
            viewmodel = GetOrderViewmodel(order=order)
            
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