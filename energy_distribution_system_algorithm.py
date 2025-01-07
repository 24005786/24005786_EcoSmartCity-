# Energy Distribution System

# Initalise Data Structures
energy_sources = [] # List to store energy sources
energy_demand = 0 # Current energy demand
energy_statistics = {} # Dictionary to store energy statistics 

# Function to add new energy source
def add_energy_source(type, capacity):
    new_source = {"type,": type, "capacity": capacity, "status": "active"}
    energy_sources.append(new_source)
    print(f"Added a new energy source: {type} with capacity {capacity}kW.")

# Function to remove or deactivate an energy source
def remove_energy_source(type):
    for source in energy_sources:
        if source ["type"] == type and source ["status"] == "active":
            source ["status"] = "inactive"
            print (f"Deactivated energy source: {type}.")
            return
    print (f"Energy source '{type}' not found or already inactive")

# Function to caclulate energy distribution
def calculate_distribution():
    total_energy = sum(source["capacity"] for source in energy_sources if source ["status"] == "active")
    if total_energy >= energy_demand:
        print (f"Energy demand met. Surplus energy: {total_energy - energy_demand}kW.")
    else:
        print (f"Energy shortfall. Additonal energy needed: {energy_demand - total_energy}kW. ")
    energy_statistics ["total_energy"] = total_energy
    energy_statistics ["energy_demand"] = energy_demand

# Function to display energy statistics 
def display_statistics():
    print ("Energy Statistics:")
    for key, value in energy_statistics.items():
        print (f"{key}: {value}")

# Function to update energy demand
def update_energy_demand (new_demand):
    global energy_demand
    energy_demand = new_demand
    print (f"Updates energy demand tp: {energy_demand}kW.")

# Main program
def main():
    while True:
        print ("\nSelect an option:")
        print ("1. Add Energy Source")
        print ("2. Remove Energy Source")
        print ("3. Calculate Distribution")
        print ("4. Display Statistics")
        print ("5. Update Energy Demand")
        print ("6. Exit")
        choice = input ("Enter your choice:")
        
        if choice == "1":
            type = input ("Enter energy souce type (e.g., Solae, Wind, Hydro):")
            capacity = int (input("Enter capacity in kW: "))
            add_energy_source (type, capacity)
        elif choice == "2":
            type = input ("Enter energy source type to remove: ")
            remove_energy_source (type)
        elif choice == "3":
            calculate_distribution()
        elif choice == "4":
            display_statistics()
        elif choice == "5":
            new_demand = int(input("Enter new energy demand in kW:"))
            update_energy_demand(new_demand)
        elif choice == "6":
            print ("Exiting Energy Distribution System.")
            break
        else:
            print ("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()