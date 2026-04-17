from typing import TypedDict

class EmailState(TypedDict):
    request: str
    draft: str
    approved: bool
    final_email: str
