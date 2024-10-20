from models.user import User
from typing import List

def select_top_users_by_rate(users: List[User], top_size: int) -> List[User]:
    return sorted(users, key=lambda x: x.rate, reverse=True)[:top_size]
