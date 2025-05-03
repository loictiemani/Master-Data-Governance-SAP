import random
import pandas as pd
import numpy as np

def generate_asset_data(num_equipment=50, seed=42):
    # Seed for reproducibility
    random.seed(seed)
    np.random.seed(seed)

    # Equipment definitions
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

    # Equipment Master Data
    equipment_data = []
    for i in range(num_equipment):
        eq_class = random.choice(equipment_classes)
        manu = random.choice(manufacturers[eq_class])
        model = random.choice(models[eq_class])
        eq_id = f"EQ{i+1:03}"
        desc = f"{eq_class.replace('_', ' ').title()} Unit {i+1}"
        func_loc = f"PLANT01-{eq_class}-{i+1:03}"
        crit = random.choice(criticalities)

        # Simulated reliability metrics (in hours/days)
        mttf = round(np.random.uniform(500, 2000), 2)  # Mean time to failure
        mttr = round(np.random.uniform(5, 20), 2)       # Mean time to repair
        mtbf = mttf + mttr                               # MTBF = MTTF + MTTR
        oee = round(np.random.uniform(60, 95), 2)        # Overall Equipment Effectiveness in %

        # Simulate annual maintenance cost based on criticality and class
        base_cost = {
            "High": 50000,
            "Medium": 30000,
            "Low": 15000
        }
        variance = np.random.uniform(0.9, 1.2)
        maint_cost = round(base_cost[crit] * variance, 2)

        equipment_data.append([
            eq_id, desc, func_loc, eq_class, manu, model, crit, mttf, mttr, mtbf, oee, maint_cost
        ])

    equipment_df = pd.DataFrame(equipment_data, columns=[
        "Equipment ID", "Description", "Functional Location", "Class",
        "Manufacturer", "Model", "Criticality",
        "MTTF (hrs)", "MTTR (hrs)", "MTBF (hrs)", "OEE (%)",
        "Maintenance Cost ($/year)"
    ])

    # Related datasets
    bom_rows = []
    floc_rows = []
    task_list_rows = []
    fmeca_rows = []

    for i, row in equipment_df.iterrows():
        # BOM
        for c in range(random.randint(2, 4)):
            bom_rows.append([
                row["Equipment ID"],
                f"COMP-{i+1:03}-{c+1}",
                f"{row['Class']} Component {c+1}",
                random.choice(["Spare", "Wear", "Critical"]),
                random.randint(1, 5)
            ])

        # Functional Location
        area = row["Functional Location"].split("-")[1]
        floc_rows.append([
            row["Functional Location"],
            f"{area} Area {random.randint(1, 3)}",
            f"Subarea {random.randint(1, 5)}",
            row["Class"]
        ])

        # Task List
        task_list_rows.append([
            row["Equipment ID"],
            f"INSPECT_{row['Class']}",
            "Inspection",
            f"Inspect {row['Class'].lower()} annually",
            "365 days",
            random.choice(["Planned", "Unplanned"]),
            random.choice(["Completed", "Pending"])
        ])
        task_list_rows.append([
            row["Equipment ID"],
            f"LUBE_{row['Class']}",
            "Lubrication",
            f"Lubricate {row['Class'].lower()} bearings",
            "90 days",
            random.choice(["Planned", "Unplanned"]),
            random.choice(["Completed", "Pending"])
        ])

        # FMECA
        fmeca_rows.append([
            row["Equipment ID"],
            f"FAIL-{i+1:03}",
            f"{row['Class']} Failure Mode",
            random.choice(["Medium", "High", "Critical"]),
            random.choice(["Planned Replacement", "Condition Monitoring"]),
            row["Criticality"]
        ])

    # Convert to DataFrames
    bom_df = pd.DataFrame(bom_rows, columns=[
        "Equipment ID", "Component ID", "Component Description", "Type", "Quantity"
    ])
    floc_df = pd.DataFrame(floc_rows, columns=[
        "Functional Location", "Area", "Subarea", "Class"
    ])
    task_list_df = pd.DataFrame(task_list_rows, columns=[
        "Equipment ID", "Task ID", "Task Type", "Description", "Frequency",
        "Maintenance Type", "Status"
    ])
    fmeca_df = pd.DataFrame(fmeca_rows, columns=[
        "Equipment ID", "Failure Mode ID", "Failure Mode", "Severity", "Recommended Action", "Criticality"
    ])
    # Failure History & Runtime Logs
    failure_history_rows = []
    runtime_log_rows = []

    for _, row in equipment_df.iterrows():
        equipment_id = row["Equipment ID"]

        # Simulate 5 failures per equipment
        for f in range(5):
            failure_date = pd.Timestamp("2024-01-01") + pd.to_timedelta(random.randint(0, 120), unit="D")
            downtime = round(np.random.uniform(1, 10), 2)
            failure_history_rows.append([
                equipment_id,
                failure_date,
                random.choice(["Mechanical", "Electrical", "Control"]),
                downtime,
                random.choice(["Overload", "Wear", "Misalignment", "Unknown"])
            ])

        # Simulate 12 monthly runtime logs
        for m in range(12):
            date = pd.Timestamp("2024-01-01") + pd.DateOffset(months=m)
            runtime_hours = round(np.random.uniform(600, 720), 2)  # ~700 hrs/month
            downtime_hours = round(np.random.uniform(0, 20), 2)
            availability = round((runtime_hours / (runtime_hours + downtime_hours)) * 100, 2)
            runtime_log_rows.append([
                equipment_id,
                date,
                runtime_hours,
                downtime_hours,
                availability
            ])

    failure_history_df = pd.DataFrame(failure_history_rows, columns=[
        "Equipment ID", "Failure Date", "Failure Type", "Downtime (hrs)", "Cause"
    ])
    runtime_log_df = pd.DataFrame(runtime_log_rows, columns=[
        "Equipment ID", "Date", "Runtime (hrs)", "Downtime (hrs)", "Availability (%)"
    ])

    return equipment_df, bom_df, floc_df, task_list_df, fmeca_df, failure_history_df, runtime_log_df

