import falcon
import json


class CompaniesResource(object):
    companies = [{"id": 1, "name": "Company one"},
                 {"id": 2, "name": "Company two"}]

    def on_get(self, req, resp):
        resp.body = json.dumps(self.companies)


api = falcon.API()
companies_endpoint = CompaniesResource()
api.add_route('/companies', companies_endpoint)
