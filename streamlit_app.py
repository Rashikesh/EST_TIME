import streamlit as st
import pandas as pd

st.set_page_config(page_title="Order Delivery Data", layout="wide")
st.title("📦 Order Delivery Details")

# Read CSV from same directory
try:
    df = pd.read_csv("processed_orders.csv")

    # Select required columns
    columns_to_display = [
        "order_id", "customer_id", "order_status",
        "order_purchase_timestamp", "order_approved_at",
        "order_delivered_carrier_date", "order_delivered_customer_date",
        "order_estimated_delivery_date", "actual_delivery_days",
        "estimated_delivery_days", "delay",
        "seller_customer_distance_km", "seller_avg_rating"
    ]

    # Check if all required columns exist
    missing_cols = [col for col in columns_to_display if col not in df.columns]
    if missing_cols:
        st.error(f"Missing columns in CSV: {missing_cols}")
    else:
        st.subheader("📋 Selected Order Details")
        st.dataframe(df[columns_to_display])
        st.success("Data loaded successfully!")

except FileNotFoundError:
    st.error("The file 'processed_orders.csv' was not found in the current directory.")
except Exception as e:
    st.error(f"An error occurred: {e}")


# Search bar input
search_query = st.text_input("🔍 Search within results (Order ID / Status):").lower()
if search_query:
    filtered_df = df[
        df['customer_id'].astype(str).str.contains(search_query) |
        df['order_status'].str.lower().str.contains(search_query)
    ]
    if not filtered_df.empty:
        st.subheader("🔍 Search Results")
        st.dataframe(filtered_df[columns_to_display])
    else:
        st.warning("No results found for your search query.")
