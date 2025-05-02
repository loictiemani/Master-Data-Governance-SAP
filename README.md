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

## 📂 Folder Guide
- `data_templates/` → Master data Excel templates
- `scripts/` → Data validation SQL
- `docs/` → Documentation of governance process
  
## Asset Hierarchy

Plant
├── Area
│   ├── Subarea
│   │   ├── System
│   │   │   ├── Equipment
│   │   │   │   └── Component
<pre> Jansen Mine (Plant) 
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
## 📬 Contact
Created by Loic, Regional Asset Management Process & Data Lead (ex-Glencore)  

