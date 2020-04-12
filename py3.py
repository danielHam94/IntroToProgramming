counter = 1
while counter <= 1000: 
	print(counter)
	counter = counter + 4.5

import random
WhatIWantToBuy = ["Airplane ticket", "iPad", "iPhone X", "tennis racquet", "BMW", "Adidas shoes", "Taylor guitar"]
while WhatIWantToBuy:
    OrderToBuy = random.choice(WhatIWantToBuy)
    print(OrderToBuy)
    WhatIWantToBuy.remove(OrderToBuy)
