from ninja import NinjaAPI

from reports.api import router as reports_router

api = NinjaAPI()

api.add_router("/reports/", reports_router)
api.add_router("/profiles/", "profiles.api.router")
