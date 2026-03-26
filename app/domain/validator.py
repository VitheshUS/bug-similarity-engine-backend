class ApiValidator:
    @staticmethod
    def validate_query(query):
        if not query or not isinstance(query, str) or query.strip() == "":
            raise ValueError("Query must be a non-empty string.")