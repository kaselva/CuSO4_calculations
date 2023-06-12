import sys
# Define Constants
COPPER_SULFATE_MOLAR_MASS = 159.62
WATER_MOLAR_MASS = 18.02
PENTAHYDRATE_MOLAR_MASS = 90.1 
COPPER_SULFATE_PENTAHYDRATE = COPPER_SULFATE_MOLAR_MASS + PENTAHYDRATE_MOLAR_MASS

def calculate_copper_sulfate(concentration, water_liters):
    molarity = concentration * 10/COPPER_SULFATE_MOLAR_MASS
    copper_sulfate_g_L = molarity * COPPER_SULFATE_MOLAR_MASS
    copper_sulfate_pentahydrate_g_L = molarity * COPPER_SULFATE_PENTAHYDRATE
    copper_sulfate_pentahydrate_kg_per_water_vol = copper_sulfate_pentahydrate_g_L * water_liters/1000
    return copper_sulfate_pentahydrate_kg_per_water_vol

def main():
    concentration, water_volume = float(sys.argv[1]), float(sys.argv[2])
    molarity = calculate_copper_sulfate(concentration, water_volume)
    #print(molarity + "molarity CUSO4.5H2O kg/" + str(water_volume) + " L")
    print(f'{molarity:.3f} CUSO4.5H2O kg/{water_volume} L')
    
if __name__ == "__main__":
    main()