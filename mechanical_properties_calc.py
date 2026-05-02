MATERIALS = {
    "steel": {"E": 210, "yield": 250},
    "aluminum": {"E": 70, "yield": 270},
    "copper": {"E": 117, "yield": 70},
    "rubber": {"E": 0.05, "yield": 20 },
    "cast_iron": {"E": 170, "yield": 130},
    "titanium": {"E": 114, "yield": 830},
    "brass": {"E": 100, "yield": 200},
    "stainless_steel": {"E": 193, "yield": 215},
    "nylon": {"E": 2.0, "yield": 45},
    "polycarbonate": {"E": 2.4, "yield": 60}
}
while True:
    print("-------MECHANICAL ENGINEERING TOOLBOX--------")
    print ("1. stress")
    print ("2. strain")
    print ("3. factor of safety")
    task = input("choose option : ")

    if task == "1":
         pressure = float(input("Pressure: "))
         area = float(input("Area: "))
         stress = (pressure / area)
         print("stress:", stress)

    elif task == "2":
        initial_length = float(input("initial_length: "))
        final_length = float(input("final_length : "))
        strain = ((final_length - initial_length) / initial_length)
        print("strain:", strain)

    elif task == "3":
        choice = input("Enter material name: " ).lower()
        if choice in MATERIALS:
            print(f"The saved yield strength for {choice} is {MATERIALS[choice]["yield"]} MPa")
            yield_strength = MATERIALS[choice]["yield"] * 1_000_000
            stress = float(input("Enter the stress: "))
            factor_of_safety = (yield_strength/stress)
            print("factor of safety of material is :", factor_of_safety)
            if factor_of_safety < 1.0:
                print(">>> WARNING: MATERIAL WILL PERMANENTLY DEFORM (Yielded) <<<")
            elif factor_of_safety < 1.5:
                print(">>> CAUTION: Low Factor of Safety for typical engineering standards. <<<")
            else:
                print(">>> Status: Design is Safe. <<<")
        else:
            print("Material not found in database.")

    repeat = input("Do you want to continue? (yes/no) ")
    if repeat == "no" or repeat == "No":
        print("******YOUR TASK COMPLETED*******")
        print ("----THANKS FOR USING PROGRAM-----")
        break
