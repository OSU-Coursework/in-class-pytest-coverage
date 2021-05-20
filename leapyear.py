def leap_year(_year):
    
    if _year < 0:
        raise ValueError

    # test value for leap year condition
    valid_condition_01 = (_year % 4 == 0) and (_year % 100 != 0)
    valid_condition_02 = (_year % 400 == 0)

    if valid_condition_01 or valid_condition_02:
        return True
    else:
        return False