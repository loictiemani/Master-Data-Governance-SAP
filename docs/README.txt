🔍 Data Governance & Quality Management
SAP MDG (also listed above) – for master data policies, validation, and stewardship

Data Cleansing & Validation Processes – Error detection, deduplication, template governance

Master Data Upload Governance (1SAP, APM) – Standardized template and quality control practices


🛠️ Example 1: Structuring Equipment Hierarchy for 1SAP/APM
Task: Designed equipment hierarchy for the Mill Area (Crushing & Conveying systems) following ISO 14224 and BHP standards.
Actions:

Created consistent functional locations and equipment IDs (e.g., JANSEN-MILL-CRUSH-CR01).

Used templates to load data via LSMW into 1SAP and GE APM.
Outcome: Reduced duplicate equipment entries and enabled better alignment of maintenance plans with asset structure.

🛠️ Example 2: Optimizing Maintenance Plans Before Activation
Task: Reviewed 500+ maintenance plans for critical underground hoisting assets.
Actions:

Aligned task lists with FMECA outputs and ensured correct linkage to functional locations.

Removed redundant plans and standardized cycle definitions.
Outcome: Cut plan activation errors by 80% and improved planner confidence in system-generated work orders.

🛠️ Example 3: Data Governance via Master Data Quality Dashboards
Task: Implemented Power BI dashboard to monitor SAP PM master data quality KPIs (missing object types, duplicates, outdated plans).
Actions:

Pulled data using SQL from SAP ECC tables (e.g., EQUI, IFLOT, MPOS).

Created data quality scoring system shared weekly with Reliability and Maintenance teams.
Outcome: Enabled proactive cleansing and improved compliance with governance standards.

🛠️ Example 4: Upload Governance Pipeline
Task: Managed and reviewed over 10 data load templates (BOMs, task lists, equipment).
Actions:

Created a version-controlled pipeline in SharePoint with QA checkpoints before loading to 1SAP.

Aligned with global SAP MDG team for approval workflows.
Outcome: Reduced bad uploads, saved 100+ hours of rework, and ensured readiness for asset commissioning.
