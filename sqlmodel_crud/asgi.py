
from mangum import Mangum
from sqlmodel_crud.main import app #type: ignore

handler = Mangum(app)


