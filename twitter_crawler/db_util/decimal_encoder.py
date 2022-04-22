import decimal
import json


class DecimalEncoder(json.JSONEncoder):
    """
    helper class to solve `Object of type Decimal is not JSON serializable`

    author: xiaotian li
    """
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self).default(o)
