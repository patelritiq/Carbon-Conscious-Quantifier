# FILE: CarbonConsciousQuantifier.py
# AUTHOR: Ritik Pratap Singh Patel
# COMPLETION DATE: 20 May 2024
# DESCRIPTION:  Analyse your Carbon Footprints: An Application that calculates an individual's carbon footprint based on their daily activities, provides visual dashboard, and provides suggestions to reduce it.
# GUIDANCE: Prof. Pooja Meena

import matplotlib.pyplot as plt

def calc_trans_fp(trans_kms):
    emission_values = {
        "car": 0.280,  # kg CO2 per km
        "bus": 0.098,
        "train": 0.049,
        "rickshaw": 0.025,
        "bike": 0.113,
        "flight": 0.112,
        "cyclewalk": 0,
    }
    total_fp = 0
    for vehicle_type, kms in trans_kms.items():
        total_fp += kms * emission_values.get(vehicle_type, 0) * 4  # weekly
    return total_fp

def calc_elec_fp(kwh):
    emission_values = 0.395  # kg CO2 per kWh
    return kwh * emission_values

def calc_diet_fp(diet_type):
    emission_values = {
        "1": 6.5,  # Full Meat Diet
        "2": 4.9,  # Omnivore Diet
        "3": 3.7,  # Veggie Diet
        "4": 3.1,  # Vegan Diet
    }
    return emission_values.get(diet_type, 0) * 30  # Monthly footprint

def calc_water_usage_fp(litres):
    emission_values = 0.014  # kg CO2 per litre
    return litres * emission_values * 30

def calc_waste_fp(waste_kg):
    emission_values = 0.590  # kg CO2 per kg of waste
    return waste_kg * emission_values * 4  # weekly

def calc_smoking_fp(cigarettes_per_day):
    emission_values = 0.028  # kg CO2 per cigarette
    return cigarettes_per_day * emission_values * 30  # Monthly footprint

def get_suggestions(trans_fp, elec_fp, diet_fp, water_fp, waste_fp, smoking_fp=None):
    suggestions = []
    if trans_fp > 335:
        suggestions.append(
            "Opt for public transportation, share rides through carpooling, use a cycle or walk through short distances - these actions contribute to lowering transportation-related carbon emissions."
        )
    if elec_fp > 100:
        suggestions.append(
            "Switch to energy-efficient appliances, ensuring that you power off lights and electronic devices when they’re not needed. Additionally, explore renewable energy options, such as installing solar panels, to reduce your electricity usage."
        )
    if diet_fp > 155:
        suggestions.append(
            "Take steps to reduce meat consumption, particularly red meat or beef, and considering a shift toward a vegetarian or vegan diet can have positive effects on both personal health and the environment."
        )
    if water_fp > 1700:
        suggestions.append(
            "Consider using a bucket instead of taking showers, promptly address any leaks, and install water-saving fixtures to minimize water usage, as excessive water consumption contributes significantly to carbon emissions."
        )
    if waste_fp > 80:
        suggestions.append(
            "Embrace recycling, practice composting, and actively minimize waste generation to decrease carbon emissions associated with waste materials."
        )
    if smoking_fp is not None and smoking_fp > 35:
        suggestions.append(
            "Consider reducing or quitting smoking, as it affects your carbon footprint and has adverse effects on health."
        )
    if not suggestions:
        suggestions.append(
            "Congratulations! You are doing great for the environment by keeping your carbon footprint in check, KEEP IT UP!"
        )

    return suggestions

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("The value cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                raise ValueError(f"Value must be between {min_val} and {max_val}.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def main():
    print(
        "-----Welcome to the Carbon Conscious Quantifier: Analyse your Carbon Footprints-----"
    )

    # Get user inputs for transportation
    print("Enter the average kms you travel per week for each mode of transportation:")
    trans_kms = {}
    trans_kms["car"] = get_float_input("Car: ")
    trans_kms["bus"] = get_float_input("Bus: ")
    trans_kms["train"] = get_float_input("Train: ")
    trans_kms["rickshaw"] = get_float_input("Rickshaw: ")
    trans_kms["bike"] = get_float_input("Bike: ")
    trans_kms["flight"] = get_float_input("Flight: ")
    trans_kms["cyclewalk"] = get_float_input("Bicycle or Walk: ")

    kwh = get_float_input("Enter your average Monthly Electricity usage in kWh: ")

    diet_type = get_int_input(
        "Enter your Diet type:\n 1. Full Meat Diet (Only Meat & eggs, no veggies or dairy products)\n 2. Omnivore Diet (Contains, Meat, dairy products & veggies)\n 3. Vegetarian Diet (Contains veggies & dairy products)\n 4. Vegan Diet (No Dairy products, only veggies)\n[Select 1-4]: ", 1, 4
    )

    litres = get_float_input("Enter your average daily water usage in litres: ")

    waste = get_float_input("Enter your average weekly waste generation in kg: ")

    smoking_fp = None
    smokes = input("Do you smoke? (yes/no): ").strip().lower()
    if smokes == "yes":
        cigarettes_per_day = get_float_input("Enter the average number of cigarettes you smoke per day: ")
        smoking_fp = calc_smoking_fp(cigarettes_per_day)

    # Calculate footprints
    trans_fp = calc_trans_fp(trans_kms)
    elec_fp = calc_elec_fp(kwh)
    diet_fp = calc_diet_fp(str(diet_type))
    water_fp = calc_water_usage_fp(litres)
    waste_fp = calc_waste_fp(waste)

    # Sum total footprint
    total_fp = trans_fp + elec_fp + diet_fp + water_fp + waste_fp
    if smoking_fp is not None:
        total_fp += smoking_fp

    # Print results
    print(f"\nYour Monthly Carbon Footprint is approximately {total_fp:.2f} kg CO2.")
    print(f"Transportation: {trans_fp:.2f} kg CO2")
    print(f"Electricity: {elec_fp:.2f} kg CO2")
    print(f"Diet: {diet_fp:.2f} kg CO2")
    print(f"Water Usage: {water_fp:.2f} kg CO2")
    print(f"Waste: {waste_fp:.2f} kg CO2")
    if smoking_fp is not None:
        print(f"Smoking: {smoking_fp:.2f} kg CO2")

    # Provide suggestions
    suggestions = get_suggestions(
        trans_fp, elec_fp, diet_fp, water_fp, waste_fp, smoking_fp
    )

    print("\nWhat we think??")
    for suggestion in suggestions:
        print(f"- {suggestion}")

    # Visualization
    labels = ["Transportation", "Electricity", "Diet", "Water Usage", "Waste"]
    values = [trans_fp, elec_fp, diet_fp, water_fp, waste_fp]

    if smoking_fp is not None:
        labels.append("Smoking")
        values.append(smoking_fp)

    # Cumulative contributions for line plot
    cumulative_values = [sum(values[: i + 1]) for i in range(len(values))]

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 18))

    # Bar chart
    ax1.bar(
        labels, values, color=["blue", "green", "orange", "purple", "brown", "grey"]
    )
    ax1.set_ylabel("CO2 Emissions (kg)")
    ax1.set_title("Monthly Carbon Footprint Breakdown")

    # Pie chart
    ax2.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=["blue", "green", "orange", "purple", "brown", "grey"],
    )
    ax2.set_title("Carbon Footprint Distribution")

    # Line chart
    ax3.plot(labels, cumulative_values, marker="o", linestyle="-", color="black")
    ax3.set_ylabel("Cumulative CO2 Emissions (kg)")
    ax3.set_title("Cumulative Contribution to Carbon Footprint")
    ax3.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
