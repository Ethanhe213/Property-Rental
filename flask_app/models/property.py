from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash,session

DB='PR'

class Property:
    def __init__(self, data):
        self.id=data['id']
        self.images=data['images']
        self.address=data['address']
        self.city=data['city']
        self.state=data['state']
        self.zip_code=data['zip_code']
        self.price=data['price']
        self.rent_period=data['rent_period']
        self.updated_at=data['updated_at']
        self.created_at=data['created_at']
        self. user=None
    @staticmethod
    def is_valid(data):
        valid=True
        flash_string='is required'
        if len(data['address'])<1:
            flash('address '+ flash_string,'PR')
            valid=False
        if len(data['city'])<1:
            flash('city '+flash_string,'PR')
            valid=False
        if len(data['state'])<1:
            flash('state '+flash_string,'PR')
            valid=False
        if len(data['zip_code'])<1:
            flash('zip code '+flash_string,'PR')
            valid=False
        if len(data['images'])<1:
            flash('at lease one image has to be uploaded','PR')
            valid=False
        return valid
    @classmethod
    def save_pr(cls,data):
        if not Property.is_valid(data):
            return False
        query='''INSERT INTO properties(images,address,city,state,
        zip_code,price,rent_period,user_id,created_at,updated_at
        VALUES(%(images)s,%(address)s,%(city)s,%(state)s,%(zip_code)s,%(price)s,
        %(rent_period)s,%(user_id)s,NOW(),NOW()
    )'''
