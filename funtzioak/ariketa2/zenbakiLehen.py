def lehenaDauka(n):

    for zenbakia in range(n, n * 2):
        lehena = True

        for i in range(2, zenbakia):
            if zenbakia % i == 0:
                lehena = False

        if lehena:
            return True

    return False
