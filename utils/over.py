def over(__aliens):
    for alien in __aliens:
        if alien.over():
            return True
    return False
