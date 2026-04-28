import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template.
    """
    # 1. Validate Input Types
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected string, got {type(template).__name__}.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Invalid input type for attendees. Expected a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Attendees and Generate Files
    placeholders = ['name', 'event_title', 'event_date', 'event_location']
    
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        for key in placeholders:
            # Retrieve value or default to "N/A" if missing or None
            value = attendee.get(key)
            if value is None or value == "":
                value = "N/A"
            
            # Replace placeholder in the string
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
            
        # 4. Write Output File
        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
            print(f"Successfully created: {filename}")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    attendees_data = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees_data)