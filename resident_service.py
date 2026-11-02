##check any issue
import re
from datetime import datetime, date


def submit_missed_bin_report(name, postcode, bin_type, collection_date):

    # Check resident name
    if not name or not name.strip():
        return {
            "accepted": False,
            "message": "Name is required"
        }

    # Check UK postcode
    postcode_pattern = r"^[A-Z]{1,2}\d[A-Z\d]?\s*\d[A-Z]{2}$"

    if not re.match(postcode_pattern, postcode.strip(), re.IGNORECASE):
        return {
            "accepted": False,
            "message": "Invalid postcode"
        }

    # Check supported bin type
    allowed_bins = ["General Waste", "Recycling", "Garden Waste"]

    if bin_type not in allowed_bins:
        return {
            "accepted": False,
            "message": "Invalid bin type"
        }

    # Check collection date
    try:
        missed_date = datetime.strptime(
            collection_date, "%Y-%m-%d"
        ).date()
    except ValueError:
        return {
            "accepted": False,
            "message": "Invalid date format"
        }

    if missed_date > date.today():
        return {
            "accepted": False,
            "message": "Collection date cannot be in the future"
        }

    # Report accepted
    return {
        "accepted": True,
        "message": "Missed bin collection report submitted successfully"
    }
