import streamlit as st
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prototype.settings')
django.setup()

from myapp.models import Record

st.title("Django and Streamlit Test")

records = Record.objects.all()
st.write("Database Records:")
for record in records:
    st.write(f"Title: {record.title}, Description: {record.description}")