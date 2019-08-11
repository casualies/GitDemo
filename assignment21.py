def sandwich(*toppings):
    print(toppings)
    
sandwich('a','b','c','d')
sandwich('afdqafq')

def car(size,brand,**more_information):
    information = {}
    information['size'] = size
    information['brand'] = brand
    for key,value in more_information.items():
        information[key] = value
    return information
    
a_car = car('outback','bwm',color='blue',money=10000000)
print(a_car)
