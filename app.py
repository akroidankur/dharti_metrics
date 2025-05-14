import os
import asyncio
import shutil
import matplotlib.pyplot as plt
from api import fetch_plastic_waste_data, fetch_wastewater_data
from prediction import is_file_valid, run_plastic_waste_prediction, run_wastewater_prediction
from plotting import plot_plastic_waste_data, plot_wastewater_data, set_current_topic

# Create the main data directory and subdirectories
os.makedirs("data/api_data", exist_ok=True)
os.makedirs("data/SavedData", exist_ok=True)

# Track the last plotted topic to determine when to close plots
last_plotted_topic = None

def close_previous_plots(current_topic):
    global last_plotted_topic
    if last_plotted_topic is not None and (last_plotted_topic != current_topic or last_plotted_topic == current_topic):
        plt.close('all')
    last_plotted_topic = current_topic

def display_welcome():
    border = "🌍" * 25
    print(f"\n{border}")
    print("🌟 Welcome to Spring Dale International School 🌟".center(50))
    print("Beharbari, Guwahati, Assam – 781028".center(50))
    print(f"{border}\n")
    print("📊 Project: DhartiMetrics 📊".center(50))
    print("A climate data analysis tool for the International Coding Olympiad.".center(50))
    print("Focus: Plastic Waste and Wastewater Discharge.".center(50))
    print('\n')
    print("📡 Data Source: https://api.data.gov.in (Indian Government Open Data)".center(50))
    print("\n🌿 Team: HAV_X 🌿".center(50))
    print("👥 Members:".center(50))
    print("  - Hridip Kashyap (Class 12)".center(50))
    print("  - Arush Nath (Class 12)".center(50))
    print("  - Vyom Agarwal (Class 12)".center(50))
    print("  - Mentor: Mr. Ankur Hazarika".center(50))
    print(f"\n{border}\n")

def display_main_menu():
    print("\n🔍 Select a topic to explore:")
    print("  1. Plastic Waste Generation (State/UT)")
    print("  2. Wastewater Discharge into Ganga (BOD Load)")
    print("  0. Exit")
    print("\n💡 Enter the number (e.g., 1, 2, 0):")

def display_plastic_waste_submenu():
    print("\n🔍 Plastic Waste Analysis Options:")
    print("  1. Fetch Plastic Waste Data")
    print("  2. Predict Future Plastic Waste")
    print("  3. Plot Graphs")
    print("  0. Back to Main Menu")
    print("\n💡 Enter the number (e.g., 1, 2, 3, 0):")

def display_wastewater_submenu():
    print("\n🔍 Wastewater Analysis Options:")
    print("  1. Fetch Wastewater Data")
    print("  2. Predict Future BOD Load")
    print("  3. Plot Graphs")
    print("  0. Back to Main Menu")
    print("\n💡 Enter the number (e.g., 1, 2, 3, 0):")

def display_data_source_options(data_type):
    print(f"\n🔍 Choose data source for {data_type}:")
    print("  1. API Fresh Data")
    print("  2. Old Saved Data")
    print("  0. Cancel")
    print("\n💡 Enter the number (e.g., 1, 2, 0):")

def display_overwrite_option(data_type):
    print(f"\n💡 Would you like to update the Saved {data_type} Data with this newly fetched data? (y/n):")
    choice = input("> ").strip().lower()
    return choice == 'y'

def get_numeric_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"❌ Invalid choice. Please select one of: {', '.join(valid_choices)}.\n")

def main():
    display_welcome()
    
    try:
        while True:
            display_main_menu()
            choice = get_numeric_choice("> ", ["0", "1", "2"])
            
            if choice == "0":
                print("\n🌱 Exiting DhartiMetrics. Goodbye! 🌱")
                break
            elif choice == "1":
                while True:
                    display_plastic_waste_submenu()
                    sub_choice = get_numeric_choice("> ", ["0", "1", "2", "3"])
                    if sub_choice == "0":
                        break
                    elif sub_choice == "1":
                        # Fetch Plastic Waste Data
                        try:
                            df = asyncio.run(fetch_plastic_waste_data())
                            api_path = 'data/api_data/plastic_waste_data.csv'
                            df.to_csv(api_path, index=False)
                            print(f"✅ Data fetched from data.gov.in API and saved to {api_path}\n")
                            if is_file_valid(api_path):
                                if display_overwrite_option("Plastic Waste"):
                                    saved_path = 'data/SavedData/plastic_waste_data.csv'
                                    shutil.copy2(api_path, saved_path)
                                    print(f"✅ Saved Plastic Waste Data updated with new data at {saved_path}\n")
                            else:
                                print(f"❌ Fetched Plastic Waste data at {api_path} is empty or invalid. Cannot use this data.\n")
                        except Exception as e:
                            print(f"❌ Failed to fetch Plastic Waste data: {str(e)}\n")
                    elif sub_choice == "2":
                        # Predict Future Plastic Waste
                        display_data_source_options("Plastic Waste")
                        source_choice = get_numeric_choice("> ", ["0", "1", "2"])
                        if source_choice == "0":
                            continue
                        if source_choice == "1":
                            data_path = 'data/api_data/plastic_waste_data.csv'
                        else:
                            data_path = 'data/SavedData/plastic_waste_data.csv'
                        
                        if not os.path.exists(data_path):
                            print(f"❌ Data file not found at {data_path}. Please fetch Plastic Waste data first (Option 1).\n")
                            continue
                        if os.path.getsize(data_path) == 0:
                            print(f"❌ Data file at {data_path} is empty. Please fetch Plastic Waste data again (Option 1).\n")
                            continue
                        
                        run_plastic_waste_prediction(data_path)
                    elif sub_choice == "3":
                        # Plot Plastic Waste Graphs
                        display_data_source_options("Plastic Waste")
                        source_choice = get_numeric_choice("> ", ["0", "1", "2"])
                        if source_choice == "0":
                            continue
                        if source_choice == "1":
                            data_path = 'data/api_data/plastic_waste_data.csv'
                        else:
                            data_path = 'data/SavedData/plastic_waste_data.csv'
                        
                        if not os.path.exists(data_path):
                            print(f"❌ Data file not found at {data_path}. Please fetch Plastic Waste data first (Option 1).\n")
                            continue
                        if os.path.getsize(data_path) == 0:
                            print(f"❌ Data file at {data_path} is empty. Please fetch Plastic Waste data again (Option 1).\n")
                            continue
                        if not is_file_valid(data_path):
                            print(f"❌ Data file at {data_path} contains no valid data. Please fetch Plastic Waste data again (Option 1).\n")
                            continue
                        
                        close_previous_plots("Plastic Waste")
                        set_current_topic("Plastic Waste")
                        
                        plot_plastic_waste_data(data_path)
            elif choice == "2":
                while True:
                    display_wastewater_submenu()
                    sub_choice = get_numeric_choice("> ", ["0", "1", "2", "3"])
                    if sub_choice == "0":
                        break
                    elif sub_choice == "1":
                        # Fetch Wastewater Data
                        try:
                            df = asyncio.run(fetch_wastewater_data())
                            api_path = 'data/api_data/wastewater_data.csv'
                            df.to_csv(api_path, index=False)
                            print(f"✅ Data fetched from data.gov.in API and saved to {api_path}\n")
                            if is_file_valid(api_path):
                                if display_overwrite_option("Wastewater"):
                                    saved_path = 'data/SavedData/wastewater_data.csv'
                                    shutil.copy2(api_path, saved_path)
                                    print(f"✅ Saved Wastewater Data updated with new data at {saved_path}\n")
                            else:
                                print(f"❌ Fetched Wastewater data at {api_path} is empty or invalid. Cannot use this data.\n")
                        except Exception as e:
                            print(f"❌ Failed to fetch Wastewater data: {str(e)}\n")
                    elif sub_choice == "2":
                        # Predict Future BOD Load
                        display_data_source_options("Wastewater")
                        source_choice = get_numeric_choice("> ", ["0", "1", "2"])
                        if source_choice == "0":
                            continue
                        if source_choice == "1":
                            data_path = 'data/api_data/wastewater_data.csv'
                        else:
                            data_path = 'data/SavedData/wastewater_data.csv'
                        
                        if not os.path.exists(data_path):
                            print(f"❌ Data file not found at {data_path}. Please fetch Wastewater data first (Option 1).\n")
                            continue
                        if os.path.getsize(data_path) == 0:
                            print(f"❌ Data file at {data_path} is empty. Please fetch Wastewater data again (Option 1).\n")
                            continue
                        
                        run_wastewater_prediction(data_path)
                    elif sub_choice == "3":
                        # Plot Wastewater Graphs
                        display_data_source_options("Wastewater")
                        source_choice = get_numeric_choice("> ", ["0", "1", "2"])
                        if source_choice == "0":
                            continue
                        if source_choice == "1":
                            data_path = 'data/api_data/wastewater_data.csv'
                        else:
                            data_path = 'data/SavedData/wastewater_data.csv'
                        
                        if not os.path.exists(data_path):
                            print(f"❌ Data file not found at {data_path}. Please fetch Wastewater data first (Option 1).\n")
                            continue
                        if os.path.getsize(data_path) == 0:
                            print(f"❌ Data file at {data_path} is empty. Please fetch Wastewater data again (Option 1).\n")
                            continue
                        if not is_file_valid(data_path):
                            print(f"❌ Data file at {data_path} contains no valid data. Please fetch Wastewater data again (Option 1).\n")
                            continue
                        
                        close_previous_plots("Wastewater")
                        set_current_topic("Wastewater")
                        
                        plot_wastewater_data(data_path)
    finally:
        # Ensure all plot windows are closed when the program exits
        plt.close('all')

if __name__ == '__main__':
    main()