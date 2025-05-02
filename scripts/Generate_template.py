import random
import pandas as pd
import numpy as np

# Seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define equipment types, manufacturers, and models
equipment_classes = ["HOIST", "UG_CONVEYOR", "MILL", "PUMP", "FAN", "MOTOR"]
manufacturers = {
    "HOIST": ["ABB", "Siemens"],
    "UG_CONVEYOR": ["Sandvik", "Joy Global"],
    "MILL": ["Metso", "FLSmidth"],
    "PUMP": ["Sulzer", "Flowserve"],
    "FAN": ["Howden", "Twin City"],
    "MOTOR": ["GE", "Baldor"]
}
models = {
    "HOIST": ["HX-100", "HX-300"],
    "UG_CONVEYOR": ["CV-200", "CV-500"],
    "MILL": ["M-800", "M-1000"],
    "PUMP": ["P-40", "P-80"],
    "FAN": ["F-50", "F-75"],
    "MOTOR": ["MTR-150", "MTR-200"]
}
criticalities = ["High", "Medium", "Low"]

# Generate Equipment Master Data (50 rows)
equipment_data = []
for i in range(50):
    eq_class = random.choice(equipment_classes)
    manu = random.choice(manufacturers[eq_class])
    model = random.choice(models[eq_class])
    eq_id = f"EQ{i+1:03}"
    desc = f"{eq_class.replace('_', ' ').title()} Unit {i+1}"
    func_loc = f"PLANT01-{eq_class}-{i+1:03}"
    crit = random.choice(criticalities)
    equipment_data.append([eq_id, desc, func_loc, eq_class, manu, model, crit])

equipment_df = pd.DataFrame(equipment_data, columns=[
    "Equipment ID", "Description", "Functional Location", "Class",
    "Manufacturer", "Model", "Criticality"
])

# Display first few rows for validation
equipment_df.head()


# Generate additional datasets based on equipment_df
bom_rows = []
floc_rows = []
task_list_rows = []
fmeca_rows = []

for i, row in equipment_df.iterrows():
    # Bill of Materials - 2-4 components per equipment
    num_components = random.randint(2, 4)
    for c in range(num_components):
        bom_rows.append([
            row["Equipment ID"],
            f"COMP-{i+1:03}-{c+1}",
            f"{row['Class']} Component {c+1}",
            random.choice(["Spare", "Wear", "Critical"]),
            random.randint(1, 5)
        ])

    # Functional Location Hierarchy
    area = row["Functional Location"].split("-")[1]
    floc_rows.append([
        row["Functional Location"],
        f"{area} Area {random.randint(1, 3)}",
        f"Subarea {random.randint(1, 5)}",
        row["Class"]
    ])

    # Task List (Maintenance Plan)
    task_list_rows.append([
        row["Equipment ID"],
        f"INSPECT_{row['Class']}",
        "Inspection",
        f"Inspect {row['Class'].lower()} annually",
        "365 days"
    ])
    task_list_rows.append([
        row["Equipment ID"],
        f"LUBE_{row['Class']}",
        "Lubrication",
        f"Lubricate {row['Class'].lower()} bearings",
        "90 days"
    ])

    # FMECA data
    fmeca_rows.append([
        row["Equipment ID"],
        f"FAIL-{i+1:03}",
        f"{row['Class']} Failure Mode",
        random.choice(["Medium", "High", "Critical"]),
        random.choice(["Planned Replacement", "Condition Monitoring"]),
        row["Criticality"]
    ])

# Create dataframes
bom_df = pd.DataFrame(bom_rows, columns=[
    "Equipment ID", "Component ID", "Component Description", "Type", "Quantity"
])
func_loc_df = pd.DataFrame(floc_rows, columns=[
    "Functional Location", "Area", "Subarea", "Class"
])
task_list_df = pd.DataFrame(task_list_rows, columns=[
    "Equipment ID", "Task ID", "Task Type", "Description", "Frequency"
])
fmeca_df = pd.DataFrame(fmeca_rows, columns=[
    "Equipment ID", "Failure Mode ID", "Failure Mode", "Severity", "Recommended Action", "Criticality"
])

# Save to Excel in the data_templates directory
excel_path = "MASTER-DATA-GOVERNANCE-SAP/data_templates/"
equipment_df.to_excel(os.path.join(excel_path, "Equipment_Master.xlsx"), index=False)
bom_df.to_excel(os.path.join(excel_path, "BOM_List.xlsx"), index=False)
func_loc_df.to_excel(os.path.join(excel_path, "Functional_Locations.xlsx"), index=False)
task_list_df.to_excel(os.path.join(excel_path, "Task_List.xlsx"), index=False)
fmeca_df.to_excel(os.path.join(excel_path, "FMECA_Data.xlsx"), index=False)

# Confirm files created
os.listdir(excel_path)
