def ground_shipping(weight):
  if weight <= 2:
    return 20 + 1.50*weight
  elif weight >2 and weight <= 6:
    return 20 + 3.00*weight
  elif weight >6 and weight <= 10:
    return 20 + 4.00*weight
  else:
    return 20 + 4.75*weight
print(ground_shipping(8.4))

premium_ground = 125.00

def drone_shipping(weight):
  if weight <= 2:
    return 4.50*weight
  elif weight >2 and weight <= 6:
    return 9.00*weight
  elif weight >6 and weight <= 10:
    return 12.00*weight
  else:
    return 14.25*weight
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  ground_cheaper = ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground
  drone_cheaper = drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground
  if ground_cheaper:
    return "You should go with ground shipping, it will cost "+ str(ground_shipping(weight)) + "."
  elif drone_cheaper:
    return "You should go with drone shipping, it will cost "+ str(drone_shipping(weight)) + "."
  elif (premium_ground < ground_shipping(weight)) and (premium_ground < drone_shipping(weight)):
    return "You should go with premium ground shipping, it will only cost 125.00"

print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))
