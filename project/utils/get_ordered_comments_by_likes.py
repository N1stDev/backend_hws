from models.comment import Comment
from typing import List

def get_ordered_comments_by_likes(comments: List[Comment]) -> List[Comment]:
    return sorted(comments, key=lambda x: x.like_count, reverse=True)
