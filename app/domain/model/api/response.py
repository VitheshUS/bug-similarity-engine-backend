class ApiResponse:
    def __init__(self,status,result=None,error=None):
        self.status=status
        self.result=result
        self.error=error