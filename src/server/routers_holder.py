from .router import Router
from .resolver import Resolver
from .routers_resolvers.auth_router import AuthRouter
from src.database.models import *

UserRouter = AuthRouter("Users", Users)
clientRouter = Router("client", client)
contractRouter = Router("contract", contract)
objectRouter = Router("object", object)
CompanyRouter = Router("Company", Company)
working_hoursRouter = Router("working_hours", working_hours)
warehouseRouter = Router("warehouse", warehouse)
providerRouter = Router("provider", provider)
workerRouter = Router("worker", worker)
productRouter = Router("product", product)
departmentsRouter = Router("departments", departments)
positionsRouter = Router("positions", positions)

routers = (UserRouter.router, clientRouter.router, contractRouter.router, objectRouter.router, CompanyRouter.router, working_hoursRouter.router, warehouseRouter.router, providerRouter.router, workerRouter.router, productRouter.router, departmentsRouter.router, positionsRouter.router)
