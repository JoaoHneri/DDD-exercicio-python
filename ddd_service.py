from ddd import DDD
from ddd_repository import DddRepository

class DddService():
    def __init__(self, ddd_repository: DddRepository) -> None:
        self.ddd_repository = ddd_repository
        
        
    def encontrarCidade(self, ddd: int) -> str:
        if(self.ddd_repository.checar_se_existe_o_ddd(ddd)):
           return self.ddd_repository.getDDD(ddd)
       
        return "None"