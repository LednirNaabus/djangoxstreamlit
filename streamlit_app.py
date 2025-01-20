import streamlit as st
import django
import pandas as pd
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototype.settings')
django.setup()

from myapp.models import Employee

st.set_page_config(page_title="HR Performance Dashboard")
st.title("Django and Streamlit Test")

employees = Employee.objects.all()

data = [
    {
        "Name": employee.name,
        "Position": employee.position,
        "Department": employee.department,
        "Branch": employee.branch,
        "Employed Date": employee.employed_date,
    }
    for employee in employees
]

employee_df = pd.DataFrame(data)
st.header("Employee Masterlist")
st.dataframe(employee_df)