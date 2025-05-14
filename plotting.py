import matplotlib.pyplot as plt
import pandas as pd
import os

current_topic = None

def set_current_topic(topic):
    global current_topic
    current_topic = topic

def plot_plastic_waste_data(data_path):
    os.makedirs("plots", exist_ok=True)
    
    df = pd.read_csv(data_path)
    
    # Ask user to select a state for time-series plots
    print("\nAvailable states/UTs:", ", ".join(df['state_ut_wise'].unique()))
    state = input("Enter state/UT name for time-series plots (e.g., Andhra Pradesh): ").strip().title()
    state_data = df[df['state_ut_wise'].str.lower() == state.lower()]
    
    if state_data.empty:
        print(f"❌ No data found for state: {state}\n")
        return
    
    # Prepare data for time-series plots (years vs. plastic waste)
    years = ['2016-17', '2017-18', '2018-19', '2019-20', '2020-21']
    year_cols = ['__2016_17', '_2017_18', '_2018_19', '_2019_20', '_2020_21']
    waste_values = []
    valid_years = []
    for year, col in zip(years, year_cols):
        value = state_data.iloc[0][col]
        if pd.isna(value) or value == 'NA':
            continue
        waste_values.append(float(value))
        valid_years.append(year)
    
    if not waste_values:
        print(f"❌ No valid data available for {state} to plot.\n")
        return
    
    # Time-series plots for the selected state
    plots = [
        ("Line Plot", lambda: plt.plot(valid_years, waste_values, color="blue", label="Plastic Waste (tonnes)"),
         f"plastic_waste_{state.lower().replace(' ', '_')}_line.png"),
        ("Scatter Plot", lambda: plt.scatter(valid_years, waste_values, color="blue", edgecolor="black", label="Plastic Waste (tonnes)"),
         f"plastic_waste_{state.lower().replace(' ', '_')}_scatter.png"),
        ("Bar Plot", lambda: plt.bar(valid_years, waste_values, color="blue", edgecolor="black", label="Plastic Waste (tonnes)"),
         f"plastic_waste_{state.lower().replace(' ', '_')}_bar.png"),
        ("Area Plot", lambda: plt.fill_between(valid_years, waste_values, color="blue", alpha=0.5, label="Plastic Waste (tonnes)"),
         f"plastic_waste_{state.lower().replace(' ', '_')}_area.png")
    ]
    
    saved_files = []
    for plot_title, plot_func, filename in plots:
        plt.figure(figsize=(8, 6))
        plot_func()
        plt.title(f"Plastic Waste in {state}: {plot_title}", fontsize=16)
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Plastic Waste (tonnes)", fontsize=12)
        plt.legend(loc=2)
        plt.grid(True)
        plt.tight_layout()
        
        save_path = os.path.join('plots', filename)
        plt.savefig(save_path)
        saved_files.append(save_path)
    
    # Comparison plot across states for a selected year
    print("\nAvailable years: 2016-17, 2017-18, 2018-19, 2019-20, 2020-21")
    year_input = input("Enter year for comparison across states (e.g., 2020-21): ").strip()
    year_map = {
        '2016-17': '__2016_17', '2017-18': '_2017_18', '2018-19': '_2018_19',
        '2019-20': '_2019_20', '2020-21': '_2020_21'
    }
    if year_input not in year_map:
        print("❌ Invalid year. Skipping comparison plot.\n")
    else:
        year_col = year_map[year_input]
        comparison_df = df[['state_ut_wise', year_col]].copy()
        comparison_df = comparison_df[comparison_df[year_col] != 'NA']
        comparison_df[year_col] = pd.to_numeric(comparison_df[year_col], errors='coerce')
        comparison_df = comparison_df.dropna(subset=[year_col])
        
        if not comparison_df.empty:
            plt.figure(figsize=(12, 6))
            plt.bar(comparison_df['state_ut_wise'], comparison_df[year_col], color="purple", edgecolor="black")
            plt.title(f"Plastic Waste Across States in {year_input}", fontsize=16)
            plt.xlabel("States/UTs", fontsize=12)
            plt.ylabel("Plastic Waste (tonnes)", fontsize=12)
            plt.xticks(rotation=45, ha='right')
            plt.grid(True, axis='y')
            plt.tight_layout()
            
            comparison_filename = f"plastic_waste_comparison_{year_input.replace('-', '_')}.png"
            save_path = os.path.join('plots', comparison_filename)
            plt.savefig(save_path)
            saved_files.append(save_path)
    
    print("\n📊 Displaying all Plastic Waste plots...")
    plt.show(block=False)
    
    print("\n✅ Plastic Waste plots saved to the 'plots/' directory:")
    for file in saved_files:
        print(f"  - {file}")

def plot_wastewater_data(data_path):
    os.makedirs("plots", exist_ok=True)
    
    df = pd.read_csv(data_path)
    
    # Remove the 'Total' row for plotting
    df = df[df['state'] != 'Total']
    
    if df.empty:
        print("❌ No valid data available for plotting.\n")
        return
    
    # Plot 1: Wastewater Discharge by State (Bar Plot)
    plt.figure(figsize=(10, 6))
    plt.bar(df['state'], df['wastewater_discharge__mld_'], color="teal", edgecolor="black")
    plt.title("Wastewater Discharge into Ganga by State (2020-21)", fontsize=16)
    plt.xlabel("States", fontsize=12)
    plt.ylabel("Wastewater Discharge (MLD)", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y')
    plt.tight_layout()
    
    wastewater_discharge_path = os.path.join('plots', 'wastewater_discharge_bar.png')
    plt.savefig(wastewater_discharge_path)
    saved_files = [wastewater_discharge_path]
    
    # Plot 2: BOD Load by State (Bar Plot)
    plt.figure(figsize=(10, 6))
    plt.bar(df['state'], df['bod_load__tpd_'], color="orange", edgecolor="black")
    plt.title("BOD Load into Ganga by State (2020-21)", fontsize=16)
    plt.xlabel("States", fontsize=12)
    plt.ylabel("BOD Load (tonnes/day)", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y')
    plt.tight_layout()
    
    bod_load_path = os.path.join('plots', 'bod_load_bar.png')
    plt.savefig(bod_load_path)
    saved_files.append(bod_load_path)
    
    # Plot 3: Combined Bar Plot for Wastewater Discharge and BOD Load
    plt.figure(figsize=(12, 6))
    bar_width = 0.35
    x = range(len(df['state']))
    plt.bar(x, df['wastewater_discharge__mld_'], bar_width, label="Wastewater Discharge (MLD)", color="teal")
    plt.bar([i + bar_width for i in x], df['bod_load__tpd_'], bar_width, label="BOD Load (tonnes/day)", color="orange")
    plt.title("Wastewater Discharge and BOD Load by State (2020-21)", fontsize=16)
    plt.xlabel("States", fontsize=12)
    plt.ylabel("Values", fontsize=12)
    plt.xticks([i + bar_width / 2 for i in x], df['state'], rotation=45, ha='right')
    plt.legend()
    plt.grid(True, axis='y')
    plt.tight_layout()
    
    combined_path = os.path.join('plots', 'wastewater_bod_combined.png')
    plt.savefig(combined_path)
    saved_files.append(combined_path)
    
    print("\n📊 Displaying all Wastewater plots...")
    plt.show(block=False)
    
    print("\n✅ Wastewater plots saved to the 'plots/' directory:")
    for file in saved_files:
        print(f"  - {file}")