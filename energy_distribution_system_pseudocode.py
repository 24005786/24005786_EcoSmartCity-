# Initialise energy_sources as an empty list
energy_sources = []

# Define a function to add a new energy source
def add_energy_source (type, production_capacity):
    # Create a new energy source as a dictionary
    new_source = {
        "type": type,
        "production_capacity": production_capacity,
        "status": "active"
    }
    # Append the new source to the energy_sources list
    energy_sources.append(new_source)

# Define a function to remove an energy source
def remove_energy_source (type):
    # For each energy source in the list
    for source in energy_sources:
        # If the type matches, remove it from the list
        if source ["type"] == type:
            energy_sources.remove (source)
            return # Exit the function

# Define a function to deactivate an energy source
def deactivate_energy_source (type):
    # For each energy source in the list
    for source in energy_sources:
        # If the type matches, set its status to "inactive"
        if source ["type"] == type:
            source ["status"] = "inactive"
            return # Exit the function

# Define a function to calculate total energy from active sources
def calculate_total_energy():
    total_energy = 0 #Initialise total energy to 0
    # For each energy source in the list
    for source in energy_sources:
        # If the source is active, add its production capacity to total_energy
        if source ["status"] == "active":
            totoal_energy += source ["production_capacity"]
    return total_energy # Return the total energy

# Define a function to display energy statistics
def display_statistics():
    # For each energy source in the list
    for source in energy_sources:
        # Print the type, production capacity, and status of the source
        print (f"Type: {source["type"]}, Production: {source["production_capacity"]}, Status: {source["status"]}")
    # Print the total energy production
    print (f"Total Energy Production: {calculate_total_energy()} units")

# Define a function to distribute energy based on demand
def distribute_energy (demand):
    # Calculate the total energy available 
    total_energy = calculate_total_energy()
    # If total_energy is greater than or equal to demand
    if total_energy >= demand:
        print ("Demand met successfull.y")
    else:
        # Print the energy shortfall
        print (f"Shortfall of {demand - total_energy} units.")