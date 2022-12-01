"""Tax"""
def tax_cc(car_cc):
    """tax_cc"""
    if car_cc >= 1:
        if 1 <= car_cc <= 600:
            return car_cc*0.50
        elif 601 <= car_cc <= 1800:
            car_600 = 600*0.50
            car_1800 = (car_cc-600)*1.50
            return car_600 + car_1800
        else:
            car_600 = 600*0.50
            car_1800 = (1800-600)*1.50
            car_morethan1800 = (car_cc-1800)*4.00
            return car_600 + car_1800 + car_morethan1800
    else:
        return car_cc
        
def tax_year(car_year, bath_cc):
    """tax_year"""
    if car_year == 6:
        price_sale = (10/100) *bath_cc
        return bath_cc - price_sale
    elif car_year == 7:
        price_sale = (20/100) *bath_cc
        return bath_cc - price_sale
    elif car_year == 8:
        price_sale = (30/100) *bath_cc
        return bath_cc - price_sale
    elif car_year == 9:
        price_sale = (40/100) *bath_cc
        return bath_cc - price_sale
    elif car_year >= 10:
        price_sale = (50/100) *bath_cc
        return bath_cc - price_sale
    else:
        return bath_cc

def main():
    """Tax"""
    car_year = int(input())
    cc_car = int(input())
    bath_cc = tax_cc(cc_car)
    tax_car = tax_year(car_year, bath_cc)
    print("%.2f"%tax_car)
main()
