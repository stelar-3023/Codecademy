def ground_shipping(weight):
    if weight <= 2:
        price_per_pound = 1.50
    elif weight > 2 and weight <= 6:
        price_per_pound = 3.00
    elif weight > 6 and weight <= 10:
        price_per_pound = 4.00
    else:
        price_per_pound = 10.00
    return 20 + (price_per_pound * weight)

premium_shipping = 125.00

def drone_shipping(weight):
    if weight <= 2:
        price_per_pound = 4.50
    elif weight > 2 and weight <= 6:
        price_per_pound = 9.00
    elif weight > 6 and weight <= 10:
        price_per_pound = 12.00
    else:
        price_per_pound = 14.25
    return price_per_pound * weight


def cheapest_shipping(weight):
    premium = premium_shipping
    ground = ground_shipping(weight)
    drone = drone_shipping(weight)
    if ground < drone and ground < premium:
        return("Ground shipping is the cheapest and will cost " + str(ground))
    elif premium < ground and premium < drone:
        return("Premium shipping is the cheapest and will cost " + str(premium))
    else:
        return("Drone shipping is the cheapest and will cost " + str(drone))
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))