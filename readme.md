# DhartiMetrics 🌍

**A Climate Data Analysis Tool for the International Coding Olympiad**

**Submission for Climate Data Analysis Challenge (14-19 yrs) - Deadline: May 15, 2025**

## Project Overview

**DhartiMetrics** is a Python-based climate data analysis tool developed by the **HAV_X** team from **Spring Dale International School**, Beharbari, Guwahati, Assam – 781028. The project focuses on analyzing **Plastic Waste Generation** across Indian states/UTs (2016–2021) and **Wastewater Discharge into the Ganga (BOD Load)** for 2020–2021, using data from the Indian Government Open Data API at [data.gov.in](https://api.data.gov.in). It provides features for data fetching, prediction of future trends, and visualization of environmental data to highlight ecological and social impacts.

### Team Members
- **Hridip Kashyap** (Class 12 - Humanities)
- **Arush Nath** (Class 12 - Science)
- **Vyom Agarwal** (Class 12 - Science)
- **Mentor:** Mr. Ankur Hazarika (developerankurhazarika@gmail.com)

### Project Timeline
- **Start Date:** Early May 2025
- **Completion Date:** May 14, 2025
- **Submission Deadline:** May 15, 2025

---

## Project Purpose

**DhartiMetrics** aims to empower users to explore critical environmental data through:
1. **Plastic Waste Generation (State/UT):** Analyze trends from 2016–2021, predict future plastic waste, and visualize patterns to understand impacts on land and water pollution.
2. **Wastewater Discharge into Ganga (BOD Load):** Assess water pollution in the Ganga basin for 2020–2021, predict future BOD load, and visualize pollution levels to highlight ecological and social consequences.

This project was developed for the **Climate Data Analysis Challenge (14-19 yrs)** as part of the International Coding Olympiad, aiming to raise awareness about environmental sustainability through data-driven insights.

---

## Features

- **Data Fetching:** Retrieve real-time data from data.gov.in API with a progress bar and retry logic for reliability.
- **Prediction:**
  - Predict future plastic waste generation for a selected state using historical averages and a growth rate.
  - Predict future BOD load in the Ganga for a selected state with a linear increase model.
- **Visualization:**
  - Generate time-series plots (Line, Scatter, Bar, Area) for Plastic Waste trends by state.
  - Create a comparison bar plot for Plastic Waste across states for a selected year.
  - Produce bar plots for Wastewater Discharge (MLD), BOD Load (tonnes/day), and a combined view by state.
- **User-Friendly CLI:** Menu-driven interface for easy navigation.
- **Error Handling:** Validates data files and handles API failures gracefully.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Required libraries: `pandas`, `matplotlib`, `aiohttp`

### Setup Instructions
1. **Unzip the Project Folder:**
   - Extract the `dharti_metrics.zip` file to a folder on your computer (e.g., `C:\dharti_metrics` on Windows or `Documents/dharti_metrics` on macOS/Linux).
   - Move to the extracted `dharti_metrics` folder.

2. **Note:** A `requirements.txt` file is already included in the folder with the following content:
   ```
   pandas
   matplotlib
   aiohttp
   ```

3. **Install Dependencies:** Follow the instructions for your operating system below.

### Running on Different Operating Systems

#### Windows
1. Ensure Python is installed on your computer. (Download and install Python 3.8 or higher from [python.org](https://www.python.org/downloads/) if not already installed.)
2. Double-click the `setup.bat` file in the `dharti_metrics` folder to install all required libraries globally.
   *Note:* The `setup.bat` file contains:
   ```
   pip install -r requirements.txt
   ```
3. To run the application, open a Command Prompt or Powershell in the folder and type:
   ```
   python app.py
   ```

#### Linux
1. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python3 app.py
   ```

#### macOS
1. Open the Terminal application (search for "Terminal" in Spotlight).
2. Navigate to the `dharti_metrics` folder using the Finder, then drag the folder into the Terminal and press Enter to set the path.
3. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python3 app.py
   ```

---

## Usage

### Running the Application
Launch the app using the appropriate method for your OS (as shown above). The welcome screen will display:
```
🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍
      🌟 Welcome to Spring Dale International School 🌟
             Beharbari, Guwahati, Assam – 781028
🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍

                  📊 Project: DhartiMetrics 📊
A climate data analysis tool for the International Coding Olympiad.
         Focus: Plastic Waste and Wastewater Discharge.

         📡 Data Source: https://api.data.gov.in (Indian Government Open Data)

                       🌿 Team: HAV_X 🌿
                           👥 Members:
                   - Hridip Kashyap (Class 12)
                     - Arush Nath (Class 12)
                    - Vyom Agarwal (Class 12)
                  - Mentor: Mr. Ankur Hazarika

🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍
```

### Main Menu
- **1. Plastic Waste Generation (State/UT):** Analyze plastic waste data.
- **2. Wastewater Discharge into Ganga (BOD Load):** Analyze wastewater data.
- **0. Exit:** Close the application.

### Plastic Waste Submenu
- **1. Fetch Plastic Waste Data:** Fetch data from the API and save to `data/api_data/plastic_waste_data.csv`. Option to overwrite `data/SavedData/plastic_waste_data.csv`.
- **2. Predict Future Plastic Waste:** Predict plastic waste for a selected state and year.
- **3. Plot Graphs:** Generate time-series plots for a state and a comparison plot across states.
- **0. Back to Main Menu**

### Wastewater Submenu
- **1. Fetch Wastewater Data:** Fetch data from the API and save to `data/api_data/wastewater_data.csv`. Option to overwrite `data/SavedData/wastewater_data.csv`.
- **2. Predict Future BOD Load:** Predict BOD load for a selected state and year.
- **3. Plot Graphs:** Generate bar plots for discharge, BOD load, and a combined view.
- **0. Back to Main Menu**

### Example Interaction
#### Predicting Plastic Waste
```
🔍 Plastic Waste Analysis Options:
  1. Fetch Plastic Waste Data
  2. Predict Future Plastic Waste
  3. Plot Graphs
  0. Back to Main Menu
💡 Enter the number (e.g., 1, 2, 3, 0):
> 2
🔍 Choose data source for Plastic Waste:
  1. API Fresh Data
  2. Old Saved Data
  0. Cancel
💡 Enter the number (e.g., 1, 2, 0):
> 2

Available states/UTs: Andhra Pradesh, Arunachal Pradesh, Assam, ...
Enter state/UT name (e.g., Andhra Pradesh): Andhra Pradesh
Enter year to predict plastic waste (e.g., 2025): 2025
Predicted plastic waste for Andhra Pradesh in 2025: 63,233.48 tonnes
Impacts:
  - Environmental: Moderate pollution risk, affecting local ecosystems.
  - Economic: Increased costs for waste management and recycling.
💡 Would you like to predict for another state/UT? (y/n):
> n
```

#### Plotting Wastewater Discharge
```
🔍 Wastewater Analysis Options:
  1. Fetch Wastewater Data
  2. Predict Future BOD Load
  3. Plot Graphs
  0. Back to Main Menu
💡 Enter the number (e.g., 1, 2, 3, 0):
> 3
🔍 Choose data source for Wastewater:
  1. API Fresh Data
  2. Old Saved Data
  0. Cancel
💡 Enter the number (e.g., 1, 2, 0):
> 2

📊 Displaying all Wastewater plots...
[Three windows: Wastewater Discharge, BOD Load, Combined]

✅ Wastewater plots saved to the 'plots/' directory:
  - plots/wastewater_discharge_bar.png
  - plots/bod_load_bar.png
  - plots/wastewater_bod_combined.png
```

---

## Data Details

### Plastic Waste Data (`plastic_waste_data.csv`)
- **Source:** [data.gov.in API](https://api.data.gov.in/resource/ad39c33f-9d07-41a8-9a7d-06081e01617f)
- **Columns:** `_sl__no_`, `state_ut_wise`, `__2016_17`, `_2017_18`, `_2018_19`, `_2019_20`, `_2020_21`
- **Focus:** Plastic waste (tonnes) for prediction and visualization.
- **Sample:**
  ```
  _sl__no_,state_ut_wise,__2016_17,_2017_18,_2018_19,_2019_20,_2020_21
  1,Andhra Pradesh,82863,NA,66314.0,46222.0,39626.45
  2,Arunachal Pradesh,NA,6,3787.37,2721.0,3755.9
  ```

### Wastewater Data (`wastewater_data.csv`)
- **Source:** [data.gov.in API](https://api.data.gov.in/resource/e374f644-b9d4-4e2a-b55f-f3888859abd6)
- **Columns:** `state`, `no__of_gpis`, `wastewater_discharge__mld_`, `bod_load__tpd_`
- **Focus:** Wastewater discharge (MLD) and BOD load (tonnes/day) for prediction and visualization.
- **Sample:**
  ```
  state,no__of_gpis,wastewater_discharge__mld_,bod_load__tpd_
  Uttarakhand,55,52.42,1.44
  Uttar Pradesh,913,139.41,4.58
  ```

---

## Future Improvements
- **Enhanced Predictions:** Implement linear regression or machine learning models for more accurate predictions.
- **Additional Data Sources:** Integrate more APIs to expand the dataset.
- **GUI Interface:** Develop a graphical user interface using Tkinter or Flask.
- **Interactive Visualizations:** Use Plotly for interactive plots.

---

## Acknowledgments
- **Spring Dale International School** for providing support and resources.
- **data.gov.in** for open access to environmental data.
- **International Coding Olympiad** for organizing the Climate Data Analysis Challenge.
- **Mentor Mr. Ankur Hazarika** for guidance and encouragement.

---

**Team HAV_X**  
**Spring Dale International School**  
**May 14, 2025**

---
