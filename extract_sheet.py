import streamlit as st
import pandas as pd
import io

# Function to extract sheet names from Excel file
def extract_sheet_names(file):
    try:
        # Load the Excel file
        xls = pd.ExcelFile(file)

        # Get the sheet names
        sheet_names = xls.sheet_names

        return sheet_names
    except Exception as e:
        st.error(f"Error: {e}")
        return []

# Main web app code

# Set Streamlit app title and description
st.title("Sheet Names Extractor")
st.write("Upload an Excel file to extract sheet names.")

# Create file upload widget
file = st.file_uploader("Upload file", type=["xlsx"])

# Check if a file is uploaded
if file is not None:
    # Read the Excel file
    sheet_names = extract_sheet_names(file)

    # Create a DataFrame with the extracted sheet names
    df_sheet_names = pd.DataFrame({"Sheet Names": sheet_names})

    # Download button for sheet names DataFrame
    if st.button("Download Sheet Names"):
        # Save DataFrame to Excel file
        excel_file = io.BytesIO()
        with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
            df_sheet_names.to_excel(writer, sheet_name="Sheet Names", index=False)
        excel_file.seek(0)

        # Provide file download link
        st.download_button("Click here to download", excel_file, file_name="sheet_names.xlsx")

    # Show the extracted sheet names
    st.write("Sheet Names:")
    st.dataframe(df_sheet_names)