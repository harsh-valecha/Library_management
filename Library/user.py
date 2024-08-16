class User:
    '''
    since if i set the user_id as public it can be modified by using User.user_id = somevalue so
    making it private

    Note here the difference between the class attribute and instance attribute i.e. user_id and name
    '''
    __user_id = 0
    def __init__(self,name:str):
        self.name = name
        User.__user_id+=1

    def get_user_id(self):
        return self.__user_id



