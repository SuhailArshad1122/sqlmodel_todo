
from mangum import Mangum
from src.api import app #type: ignore

handler = Mangum(app)


