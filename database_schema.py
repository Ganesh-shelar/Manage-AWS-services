'''
User
user_id	number	PK
user_name
first_name
last_name

Services
service_id
Service_name
description
service_keys
service_type

Instances
instance_id
service_id
Instance name
created_on
created_by
tags
Status
updated_on
updated_by
'''

'''
1. Create 10 decorators
2. write a decorator function & 3-4 functions to check user have that permission or not
3. Create list of permissions (at least 15 permissions)
	Create dictionary of users
	user={
	    <email id/phone_no/id):{    
            'roles': [role_id,role_id2],
            'permissions':[permission1,permission2]
            }
        }
create dictionary od role atleast 5-atleast 4 users
roles={
'id:1,
'permissions':['can_create_user,'can_delete_user']
}
Functions
check_permissions=Decorator user, permissions
def create_user(user_name,'can_create_user')
def delete_user(user_name,'can_create_user')
.
.
'''


"""
   Create list of permissions (at least 15 permissions)
"""
permissions = ['can_create_user', 'can_delete_user', 'can_update_user',
                'can_create_service', 'can_delete_service', 'can_update_service',
                'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance']

"""
   Create dictionary of user  (at least 4 users)
   
   Create dictionary of roles (at least 5 roles)
"""
roles = {
        'id': 1,
        'permissions':  ['can_create_user', 'can_delete_user', 'can_update_user',
                        'can_create_service', 'can_delete_service', 'can_update_service',
                        'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'],
        'id': 2,
        'permissions':['can_create_user', 
                        'can_create_service', 'can_delete_service', 'can_update_service',
                        'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'],
        'id': 3,
        'permissions':['can_create_service', 'can_delete_service', 'can_update_service'],
        'id': 4,
        'permissions':[ 'can_update_service'],
                        
        'id': 5,
        'permissions':['can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'],
        'id': 6,
        'permissions':[ 'can_update_service_instance'],
   }

users ={
        'Ganesh' : {
            'roles': [1],
            'permissions': ['can_create_user', 'can_delete_user', 'can_update_user',
                        'can_create_service', 'can_delete_service', 'can_update_service',
                        'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'];
                    };
        'Parth': {
            'roles': [1],
            'permissions': ['can_create_user', 'can_delete_user', 'can_update_user',
                        'can_create_service', 'can_delete_service', 'can_update_service',
                        'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'];
                    };
        'Ritika':{
            'roles': [2],
            'permissions': ['can_create_user', 
                        'can_create_service', 'can_delete_service', 'can_update_service',
                        'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'];
                    };   
        'Shiva':{
            'roles': [2],
            'permissions': ['can_create_user', 
                        'can_create_service', 'can_delete_service', 'can_update_service',
                        'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'];
                    }; 
        'Sandeep':{
            'roles': [3],
            'permissions': ['can_create_service', 'can_delete_service', 'can_update_service'];
                    }; 
        'Srikant':{
            'roles': [4],
            'permissions': ['can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'];
                    }; 
        'Vishal':{
            'roles': [3,5],
            'permissions': [ 
                        'can_create_service', 'can_delete_service', 'can_update_service',
                        'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'];
                    }; 
        'Rita':{
            'roles': [3,5],
            'permissions': [
                        'can_create_service', 'can_delete_service', 'can_update_service',
                        'can_create_service_instance', 'can_delete_service_instance', 'can_update_service_instance'];
                    }; 
        'Swagata':{
            'roles': [4,6],
            'permissions': ['can_update_service','can_update_service_instance'];
                    }; 
        'Akshay':{
            'roles': [4,6],
            'permissions': [''can_update_service','can_update_service_instance'];
                    }; 
        }
