import falcon
import json


class CompaniesResource(object):
    companies = [{"id": 1, "name": "Company one"},
                 {"id": 2, "name": "Company two"}]

    def on_get(self, req, resp):
        resp.body = json.dumps(self.companies)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201
        resp.body = json.dumps({"success": True})


api = falcon.API()
companies_endpoint = CompaniesResource()
api.add_route('/companies', companies_endpoint)
