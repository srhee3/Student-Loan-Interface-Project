def fetch_irs_tax_forms(form_type):
    """     
    Fetch information about specific tax forms from the IRS API.
    """
    api_url = "https://api.irs.gov/forms"
    params = {
        "form_number": form_type,  # Example: "1098" or "1099-C"
        "tax_year": "2023"  # Specify the tax year of the 
    }
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        forms_data = response.json()
                           
        # Display the fetched information about specific tax forms 
        for form in forms_data:
            print(f"Form Number: {form['form_number']}")  
            print(f"Form Title: {form['form_title']}")
            print(f"Description: {form['description']}")
            print(f"Download URL: {form['form_url']}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
fetch_irs_tax_forms("1098")
    fetch  