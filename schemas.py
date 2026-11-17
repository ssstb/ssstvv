from pydantic import BaseModel

# Схема для входящих данных при создании пользователя
class UserCreate(BaseModel):
    name: str
    email: str

# Схема для ответа клиенту (чтобы скрыть лишнее и отдать id)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = {"from_attributes": True}  # Позволяет SQLAlchemy моделям легко конвертироваться в Pydantic