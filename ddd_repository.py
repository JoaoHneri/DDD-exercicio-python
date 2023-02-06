from ddd import DDD

class DddRepository():
    def __init__(self) -> None:
        self.ddd_repository: list[DDD] = []
        
    def getDDD(self, ddd: int) -> str:
        for d in self.ddd_repository:
            if(ddd == d.ddd):
              return d.cidade
        
    def append(self, ddd_repository: DDD) -> None:
        self.ddd_repository.append(ddd_repository)
        
    def checar_se_existe_o_ddd(self, ddd: int) -> bool:
        for d in self.ddd_repository:
            if ddd == d.ddd:
                return True
            
        return False