from app.models.api_key import APIKey

from app.core.api_key import (
    generate_api_key,
    hash_api_key
)

from app.api_keys.repository import (
    APIKeyRepository
)


class APIKeyService:

    def __init__(
        self,
        repository: APIKeyRepository
    ):
        self.repository = repository


    async def create_key(
        self,
        user_id,
        name: str
    ):

        raw_key = generate_api_key()

        api_key = APIKey(
            user_id=user_id,
            name=name,
            key_hash=hash_api_key(
                raw_key
            )
        )

        await self.repository.create(
            api_key
        )

        return raw_key
    
    
    async def list_keys(
        self,
        user_id
    ):

        return await self.repository.get_by_user_id(
            user_id
        )
        
    async def revoke_key(
        self,
        api_key_id,
        user_id
    ):
        api_key = await self.repository.get_by_id(
            api_key_id
        )

        if not api_key:
         return None

        if api_key.user_id != user_id:
            return None

        api_key.is_active = False

        await self.repository.update(
            api_key
        )

        return api_key