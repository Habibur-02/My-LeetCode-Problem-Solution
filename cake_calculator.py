def cake_calculator(flour, sugar):
    
    
    FLOUR_PER_CAKE = 100
    SUGAR_PER_CAKE = 50
    
    
    possible_cakes_via_flour = flour // FLOUR_PER_CAKE
    possible_cakes_via_sugar = sugar // SUGAR_PER_CAKE
    
  
    cakes_we_can_bake = min(possible_cakes_via_flour, possible_cakes_via_sugar)
    
    leftover_flour = flour - (cakes_we_can_bake * FLOUR_PER_CAKE)
    leftover_sugar = sugar - (cakes_we_can_bake * SUGAR_PER_CAKE)
    
    return [cakes_we_can_bake, leftover_flour, leftover_sugar]

