from models.user import User
from models.comment import Comment
from typing import List

def filter_comments_by_author(comments: List[Comment], author: User) -> List[str]:
    return [c for c in comments if c.author_id == author.id]
