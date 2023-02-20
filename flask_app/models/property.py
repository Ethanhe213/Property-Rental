from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash,session
from flask_app.models import user
DB='pr'

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
        self.description=data['description']
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
    @classmethod
    def pr_city(cls,city,state):
        data={
            'city':city,
            'state':state,
        }
        list=[]
        query='''SELECT * FROM properties join users on users.id=properties.user_id
        WHERE city=%(city)s and state=%(state)s '''
        result=connectToMySQL(DB).query_db(query,data)
        if len(result) < 1:
            return False
        for i in result:
            a=cls(i)
            a.user=user.User({
                'id':i['user_id'],
                'first_name':i['first_name'],
                'last_name':i['last_name'],
                'email':i['email'],
                'password':i['password'],
                'phone_number':i['phone_number'],
                'created_at':i['users.created_at'],
                'updated_at':i['users.updated_at']
            })
            list.append(a)
        return list