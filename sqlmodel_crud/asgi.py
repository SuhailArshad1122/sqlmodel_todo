from mangum import Mangum
from sqlmodel_crud.main import app  # adjust the import according to your project structure

handler = Mangum(app)
