def can_delete_book(has_active_loans: bool) -> bool:
    return not has_active_loans
