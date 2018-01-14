from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.api.rest.events.event import Event
from app.api.db import get_data,insertupdate,read

@rest_resource
class SquiryPicksEvents(BaseResource):
    """ /api/squirypicksevents """
    endpoints = ['/squirypicksevents']

    def get(self):        
        return get_data(0,4)

@rest_resource
class TopEvents(BaseResource):
    """ /api/topevents """
    endpoints = ['/topevents/','/topevents/<string:category>']

    def get(self,category = None):        
        return get_data(5,10)

@rest_resource
class EventCategories(BaseResource):
    """ /api/eventcategories """
    endpoints = ['/eventcategories']

    def get(self,category = None):                
        categories = read("select * from category")  
        print("Categories")
        print(categories)
        return categories