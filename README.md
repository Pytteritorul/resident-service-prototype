# resident-service-prototype
Python-based council missed bin collection reporting service using Behave and BDD.

Service: Report a missed bin collection.

Main stakeholder: Local council residents and waste management officers.

Problem: Residents need a simple way to report missed collections so the council can investigate and arrange collection.

Example user story

As a council resident, I want to report a missed bin collection so that the council can investigate and resolve the problem.

Acceptance criteria
- The resident must provide their name.
- The resident must provide a valid postcode.
- The bin type must be selected from an allowed list.
- The missed collection date must be valid and not in the future.
- Invalid information must produce a clear error message.
- A valid report must receive a confirmation.
