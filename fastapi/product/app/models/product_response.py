import pprint
from datetime import date
from pydantic import BaseModel

class ProductResponse(BaseModel):

    id: str
    creation: date

    def __repr__(self):
        return self.to_str()
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return not self == other
        
