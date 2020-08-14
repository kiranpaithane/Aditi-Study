def cigar_party(cigars, is_weekend):
    if cigars == 30 and is_weekend == False:
        return False
    elif cigars == 50 and is_weekend == False:
        return False
    elif cigars == 70 and is_weekend == True:
        print("True")
        return True

cigar_party(70, True)