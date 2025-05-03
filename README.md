# Maintenance Readiness & Master Data Governance Project

This end-to-end project simulates the master data preparation and governance process for a greenfield mining operation, aligning with the responsibilities described in BHP's Fixed Reliability role for the Jansen Potash project.

## 🚀 Objectives
- Simulate equipment master data creation and validation
- Align FMECA outputs with maintenance strategies
- Govern upload templates for 1SAP/APM
- Cleanse and validate data using SQL and Power BI

## 🧩 Components
- **Master Data Templates**: Equipment, BOM, Functional Locations, Maintenance Plans
- **FMECA Integration**: Sample study linked to maintenance planning
- **Data Quality Checks**: SQL rules and Power BI dashboard
- **Governance Workflow**: Template approval simulation

## 📊 Tools Used
SAP PM | SAP MDG | Power BI | SQL Server | AVEVA PI (simulated) | Azure (optional)

## 🖼️ Screenshots
*(Include images of Power BI dashboards, asset hierarchy charts, etc.)*
![MasterData](https://github.com/loictiemani/Master-Data-Governance-SAP/blob/main/docs/MasterData.png)

## 📂 Folder Guide
- `data_templates/` → Master data Excel templates
- `scripts/` → Data validation SQL
- `docs/` → Documentation of governance process

## 🏗️ Asset Structure
### Asset Hierarchy

<pre>
Plant
├── Area
│   ├── Subarea
│   │   ├── System
│   │   │   ├── Equipment
│   │   │   │   └── Component
</pre> 
  
<pre>
  Plant 
  ├── Mill Area 
  │ ├── Crushing Subarea 
  │ │ ├── Crusher System 
  │ │ │ ├── Crusher A (Equipment) 
  │ │ │ │ ├── Motor A (Component) 
  │ │ │ │ ├── Gearbox A 
  │ │ │ │ └── Bearing A1 
  │ ├── Conveying Subarea 
  │ │ ├── Conveyor System 
  │ │ │ ├── Conveyor 1 (Equipment) 
  │ │ │ │ ├── Motor B 
  │ │ │ │ ├── Pulley B1 
  │ │ │ │ └── Belt B1 
  ├── UG Mine Area │ 
  ├── Hoisting Subarea 
  │ │ ├── Hoist System 
  │ │ │ ├── Hoist A (Equipment) 
  │ │ │ │ ├── Motor H1 
  │ │ │ │ ├── Brake System H2 
  │ │ │ │ └── Drum H3 
</pre>

---

## 📈 Performance Measurement
### KPIs

| KPI                            | Description                                      |
|--------------------------------|--------------------------------------------------|
| MTTF (Mean Time to Failure)    | Average uptime between failures                 |
| MTTR (Mean Time to Repair)     | Average time taken to restore equipment         |
| MTBF (Mean Time Between Failures) | Measures reliability over time              |
| OEE (Overall Equipment Effectiveness) | Availability × Performance × Quality   |
| Availability (%)               | % of time equipment is available for use        |
| Utilization Rate               | Equipment run hours vs. available hours         |

### 🔍 Maintenance Efficiency KPIs

| KPI                                  | Description                                         |
|--------------------------------------|-----------------------------------------------------|
| Planned vs. Unplanned Maintenance (%)| % of work that was planned in advance               |
| Backlog Age                          | Average age of open work orders                     |
| PM Compliance Rate (%)               | % of preventive maintenance tasks on schedule       |
| Maintenance Cost per Equipment       | Cost to maintain each asset annually                |
| Failure Rate per Equipment Class     | Number of failures per asset type over time         |

### 📊 Master Data Quality KPIs

| KPI                      | Description                                          |
|--------------------------|------------------------------------------------------|
| Data Completeness (%)    | % of records with all required fields filled         |
| Duplicate Records Count  | Number of duplicate equipment IDs or locations       |
| Hierarchy Accuracy       | % of assets correctly mapped in hierarchy            |
| BOM Coverage (%)         | % of assets with complete bill of materials          |
| Task List Coverage (%)   | % of equipment with assigned maintenance tasks       |

### 📦 Readiness & Progress KPIs

| KPI                                   | Description                                           |
|---------------------------------------|-------------------------------------------------------|
| Master Data Upload Progress           | % of total assets uploaded into 1SAP/APM              |
| Validation Error Rate (%)             | % of records with validation errors during upload     |
| FMECAs Completed (%)                  | % of assets with completed FMECA analysis             |
| Template Submission Compliance        | % of teams/sites submitting data templates on time    |
| Maintenance Strategy Optimization Progress | % of strategies approved before go-live         |

---


## 📬 Contact

Created by **Loic**, Regional Asset Management Process & Data Lead (ex-Glencore)
