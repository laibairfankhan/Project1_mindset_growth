# import streamlit as at
# import pandas as pd
# from io import BytesIO

# st.set_page_config(page_title="File Converter", layout="wide")
# st.title("File Converter & Cleaner")
# st.write("Upload csv or excel files,clean data,and converter formats.")

# files = st.file_uploader("Upload CSV or Excel Files." , type["csv","xlsx"])

# if files :
#     for file  in files :
#     ext = file.name.split(".")[=1]
#     df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)
    
#     st.subheader(f"{file.name} - preview")
# st.dataframe(df.head())


# import streamlit as st
# import pandas as pd
# from io import BytesIO

# st.set_page_config(page_title="File Converter", layout="wide")
# st.title("File Converter & Cleaner")
# st.write("Upload CSV or Excel files, clean data, and convert formats.")

# files = st.file_uploader("Upload CSV or Excel Files.", type=["csv", "xlsx"], accept_multiple_files=True)

# if files:
#     for file in files:
#         ext = file.name.split(".")[-1]
#         df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

#         st.subheader(f"{file.name} - Preview")
#         st.dataframe(df.head())

#         if st.checkbox(f"Remove Duplicates - {file.name}"):
#             df = df.drop_duplicates()
#             st.success("Duplicates Removed")
#             st.dataframe(df.head())

#             if st.checkbox(f"Fill Missing Values - {file.name}"):
#                 df.fillna(df.select_dtypes(include=["number"]).mean(),inplace=True)
#                 st.success("Missing Values filed with mean")
#                 st.dataframe(df.head())



#                 selected_columns = st.multiselect(f"Select Columns - {file.name}" . df.columns, default=df.columns)
#                 df= df[selected_columns]
#                 st.dataframe(df.head())


# if st.checkbox(f"Show chart - {file.name}") and not df.select_dtypes(include="number").empty:
#  st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

# format_choice = st.radio(f"Convert {file.name} to:" , ["csv", "Excel"], key=file.name)

# if st.button(f"Download {file.name} as {format_choice}"):
#    output =BytesIO
#    if format_choice == "csv":
#       df.to_csv(output, index=False)
#       mine = "text/csv"
#       new_name = file.name.replace(ext, "csv")
      
#    else :
#       df.to_excel(output, index=False, engine='openpyxl')
#       mine = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#       new_name = file.name.replace(ext, "xlsx")


# output.seek(0)
# st.download_button("Download file ", file_name=new_name, data=output, mime=mine)
# st.success("Processing Complete!")













# import streamlit as st
# import pandas as pd
# from io import BytesIO

# st.set_page_config(page_title="File Converter", layout="wide")
# st.title("File Converter & Cleaner")
# st.write("Upload CSV or Excel files, clean data, and convert formats.")

# files = st.file_uploader("Upload CSV or Excel Files.", type=["csv", "xlsx"], accept_multiple_files=True)

# if files:
#     for file in files:
#         ext = file.name.split(".")[-1]
#         df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

#         st.subheader(f"{file.name} - Preview")
#         st.dataframe(df.head())

#         # Remove duplicates
#         if st.checkbox(f"Remove Duplicates - {file.name}"):
#             df = df.drop_duplicates()
#             st.success("Duplicates Removed")
#             st.dataframe(df.head())

#         # Fill missing values
#         if st.checkbox(f"Fill Missing Values - {file.name}"):
#             df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
#             st.success("Missing Values filled with mean")
#             st.dataframe(df.head())

#         # Select specific columns
#         selected_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns)
#         df = df[selected_columns]
#         st.dataframe(df.head())

#         # Show chart
#         if st.checkbox(f"Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
#             st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

#         # File format conversion
#         format_choice = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

#         # Download file
#         if st.button(f"Download {file.name} as {format_choice}"):
#             output = BytesIO()
#             if format_choice == "CSV":
#                 df.to_csv(output, index=False)
#                 mime_type = "text/csv"
#                 new_name = file.name.replace(ext, "csv")
#             else:
#                 df.to_excel(output, index=False, engine='openpyxl')
#                 mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                 new_name = file.name.replace(ext, "xlsx")

#             output.seek(0)
#             st.download_button("Download file", file_name=new_name, data=output.getvalue(), mime=mime_type)
#             st.success("Processing Complete!")







import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="File Converter", layout="wide")
st.title("File Converter & Cleaner")
st.write("Upload CSV or Excel files, clean data, and convert formats.")

files = st.file_uploader("Upload CSV or Excel Files.", type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1]

        try:
            df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file, engine="openpyxl")
        except Exception as e:
            st.error(f"Error loading {file.name}: {str(e)}")
            continue

        st.subheader(f"{file.name} - Preview")
        st.dataframe(df.head())

        # Remove duplicates
        if st.checkbox(f"Remove Duplicates - {file.name}"):
            df = df.drop_duplicates()
            st.success("Duplicates Removed")
            st.dataframe(df.head())

        # Fill missing values
        if st.checkbox(f"Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
            st.success("Missing Values filled with mean")
            st.dataframe(df.head())

        # Select specific columns
        selected_columns = st.multiselect(f"Select Columns - {file.name}", df.columns, default=df.columns)
        df = df[selected_columns]
        st.dataframe(df.head())

        # Show chart
        if st.checkbox(f"Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # File format conversion
        format_choice = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        # Download file
        def convert_df(df, format_choice):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mime_type = "text/csv"
                new_name = file.name.replace(ext, "csv")
            else:
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False)
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_name = file.name.replace(ext, "xlsx")

            output.seek(0)
            return output.getvalue(), mime_type, new_name

        if st.button(f"Download {file.name} as {format_choice}"):
            file_data, mime_type, new_name = convert_df(df, format_choice)
            st.download_button("Download file", file_name=new_name, data=file_data, mime=mime_type)
            st.success("Processing Complete!")
