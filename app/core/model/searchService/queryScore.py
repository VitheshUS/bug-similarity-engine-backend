class QueryScore:
    def __init__(self,query,score):
        self.query=query
        self.score=score

    def to_dict(self):
        return {
            "query": self.query,
            "score": self.score
        }