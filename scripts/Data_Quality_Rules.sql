-- SQL example: Find missing critical fields
SELECT * FROM Equipment_Master WHERE Description IS NULL OR Criticality IS NULL;
