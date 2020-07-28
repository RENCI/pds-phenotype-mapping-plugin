import pdsphenotypemapping.dispatcher


def mappingClinicalFromData(body):
    if "settingsRequested" not in body:
        body["settingsRequested"] = config['settingsDefaults']
    patient_ids = body["patientIds"]
    timestamp = body["timestamp"]

    ret_response = []
    for i, patient_id in enumerate(patient_ids):
        val = pdsphenotypemapping.dispatcher.lookupClinicalsFromData(patient_id, i, timestamp, body)
        if isinstance(val, tuple):
            # mapping failed since a (error_message, status_code) tuple is returned
            return val
        else:
            ret_response.append({
                "patientId": patient_id,
                "values": val
            })
    return ret_response


config = {
    "title": "smarthealthit.org variable mapper",
    'piid': "pdspi-mapper-example",
    "pluginType": "m",
    "settingsDefaults": {
        "pluginSelectors": [],
        "patientVariables": [
            {
                "id": i,
                "title": t,
                "legalValues": lv
            } for i,t,lv in [
                ("LOINC:2160-0", "Serum creatinine", {"type": "number"}),
                ("LOINC:82810-3", "Pregnancy", {"type": "boolean"}),
                ("HP:0001892", "Bleeding", {"type": "boolean"}),
                ("HP:0000077", "Kidney dysfunction", {"type": "boolean"}),
                ("LOINC:45701-0", "Fever", {"type": "boolean"}),
                ("LOINC:LP212175-6", "Date of fever onset", {"type": "string"}),
                ("LOINC:64145-6", "Cough", {"type": "boolean"}),
                ("LOINC:85932-2", "Date of cough onset", {"type": "string"}),
                ("LOINC:54564-0", "Shortness of breath", {"type": "boolean"}),
                ("LOINC:LP172921-1", "Cardiovascular disease", {"type": "boolean"}),
                ("LOINC:54542-6", "Pulmonary disease", {"type": "boolean"}),
                ("LOINC:LP128504-0", "Autoimmune disease", {"type": "boolean"}),
                ("LOINC:LP21258-6", "Oxygen saturation", {"type": "number"}),
                ("LOINC:30525-0", "Age", {"type": "integer"}),
                ("LOINC:54134-2", "Race", {"type": "string"}),
                ("LOINC:54120-1", "Ethnicity", {"type": "string"}),
                ("LOINC:21840-4", "Sex", {"type": "string"}),
                ("LOINC:8302-2", "Height", {"type": "number"}),
                ("LOINC:29463-7", "Weight", {"type": "number"}),
                ("LOINC:56799-0", "Address", {"type": "string"}),
                ("LOINC:39156-5", "BMI", {"type": "number"})
            ]
        ]
    },
    "pluginTypeTitle": "Mapping"
}


def get_config():
    return config
