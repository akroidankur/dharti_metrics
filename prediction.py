import os
import pandas as pd

def is_file_valid(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return False
    try:
        df = pd.read_csv(file_path)
        return not df.empty
    except (pd.errors.EmptyDataError, Exception):
        return False

def predict_plastic_waste(df, state, year):
    state = state.title()
    state_data = df[df['state_ut_wise'].str.lower() == state.lower()]
    if state_data.empty:
        return None, f"No data found for state: {state}"

    years = ['__2016_17', '_2017_18', '_2018_19', '_2019_20', '_2020_21']
    waste_values = []
    for year_col in years:
        value = state_data.iloc[0][year_col]
        if pd.isna(value) or value == 'NA':
            continue
        waste_values.append(float(value))

    if not waste_values:
        return None, f"No valid data available for {state} to make a prediction."

    avg_waste = sum(waste_values) / len(waste_values)
    annual_growth_rate = 0.02  # 2% annual increase
    latest_year = 2021
    years_diff = year - latest_year
    predicted_waste = avg_waste * (1 + annual_growth_rate) ** years_diff

    impacts = []
    if predicted_waste < 50000:
        impacts.append("Environmental: Low land and water pollution risk.")
        impacts.append("Economic: Manageable waste management costs.")
    elif 50000 <= predicted_waste <= 200000:
        impacts.append("Environmental: Moderate pollution risk, affecting local ecosystems.")
        impacts.append("Economic: Increased costs for waste management and recycling.")
    else:
        impacts.append("Environmental: High pollution risk, severe impact on land and water bodies.")
        impacts.append("Economic: Significant costs for waste management, cleanup, and policy enforcement.")

    return predicted_waste, impacts

def predict_wastewater_bod(df, state, year):
    state = state.title()
    state_data = df[df['state'].str.lower() == state.lower()]
    if state_data.empty:
        return None, f"No data found for state: {state}"

    bod_load = float(state_data.iloc[0]['bod_load__tpd_'])
    wastewater_discharge = float(state_data.iloc[0]['wastewater_discharge__mld_'])

    annual_increase_rate = 0.01
    latest_year = 2021
    years_diff = year - latest_year
    predicted_bod = bod_load * (1 + annual_increase_rate) ** years_diff

    impacts = []
    if predicted_bod < 2:
        impacts.append("Ecological: Low impact on river ecosystem health.")
        impacts.append("Social: Minimal impact on community well-being.")
    elif 2 <= predicted_bod <= 5:
        impacts.append("Ecological: Moderate impact, reduced oxygen levels affecting aquatic life.")
        impacts.append("Social: Potential health risks for communities relying on the river.")
    else:
        impacts.append("Ecological: Severe impact, significant harm to aquatic ecosystems.")
        impacts.append("Social: Major health and livelihood risks for river-dependent communities.")

    return predicted_bod, impacts

def run_plastic_waste_prediction(data_path):
    try:
        df = pd.read_csv(data_path)
        if df.empty:
            print(f"❌ No data found in {data_path}. Please fetch Plastic Waste data again (Option 1).\n")
            return False
    except pd.errors.EmptyDataError:
        print(f"❌ Data file at {data_path} contains no valid data. Please fetch Plastic Waste data again (Option 1).\n")
        return False
    except Exception as e:
        print(f"❌ Error reading data from {data_path}: {str(e)}. Please fetch Plastic Waste data again (Option 1).\n")
        return False
    
    while True:
        print("\nAvailable states/UTs:", ", ".join(df['state_ut_wise'].unique()))
        state = input("Enter state/UT name (e.g., Andhra Pradesh): ").strip()
        year = input("Enter year to predict plastic waste (e.g., 2025): ").strip()
        try:
            year = int(year)
            if year <= 2021:
                print("❌ Please enter a future year (after 2021).\n")
                continue
            predicted_waste, result = predict_plastic_waste(df, state, year)
            if predicted_waste is not None:
                print(f"\nPredicted plastic waste for {state.title()} in {year}: {predicted_waste:,.2f} tonnes")
                print("Impacts:")
                for impact in result:
                    print(f"  - {impact}")
            else:
                print(f"❌ {result}\n")
            print("\n💡 Would you like to predict for another state/UT? (y/n):")
            continue_choice = input("> ").strip().lower()
            if continue_choice != 'y':
                break
        except ValueError:
            print("❌ Please enter a valid year (e.g., 2025).\n")
    return True

def run_wastewater_prediction(data_path):
    try:
        df = pd.read_csv(data_path)
        if df.empty:
            print(f"❌ No data found in {data_path}. Please fetch Wastewater data again (Option 1).\n")
            return False
    except pd.errors.EmptyDataError:
        print(f"❌ Data file at {data_path} contains no valid data. Please fetch Wastewater data again (Option 1).\n")
        return False
    except Exception as e:
        print(f"❌ Error reading data from {data_path}: {str(e)}. Please fetch Wastewater data again (Option 1).\n")
        return False
    
    while True:
        print("\nAvailable states:", ", ".join(df['state'].unique()))
        state = input("Enter state name (e.g., Uttar Pradesh): ").strip()
        year = input("Enter year to predict BOD load (e.g., 2025): ").strip()
        try:
            year = int(year)
            if year <= 2021:
                print("❌ Please enter a future year (after 2021).\n")
                continue
            predicted_bod, result = predict_wastewater_bod(df, state, year)
            if predicted_bod is not None:
                print(f"\nPredicted BOD load for {state.title()} in {year}: {predicted_bod:.2f} tonnes/day")
                print("Impacts:")
                for impact in result:
                    print(f"  - {impact}")
            else:
                print(f"❌ {result}\n")
            print("\n💡 Would you like to predict for another state? (y/n):")
            continue_choice = input("> ").strip().lower()
            if continue_choice != 'y':
                break
        except ValueError:
            print("❌ Please enter a valid year (e.g., 2025).\n")
    return True