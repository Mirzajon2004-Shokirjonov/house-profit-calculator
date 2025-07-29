import streamlit as st

# Foyda hisoblovchi funksiya
def calculate_profit(area_m2, is_roof_closed=True):
    construction = 1000
    transport = 100
    sales = 50
    land = 200

    total_cost_per_m2 = construction + transport + sales + land
    selling_price = 1800 if is_roof_closed else 1700

    profit_per_m2 = selling_price - total_cost_per_m2 * 1.27
    total_profit = profit_per_m2 * area_m2

    return {
        "1 m² Revenue (Sotuv narxi)": f"${selling_price}",
        "1 m² Cost without Tax": f"${total_cost_per_m2}",
        "1 m² Cost with Tax (27%)": f"${round(total_cost_per_m2 * 1.27, 2)}",
        "1 m² Profit": f"${round(profit_per_m2, 2)}",
        "Total Profit": f"${round(total_profit, 2)}"
    }

# Streamlit ilova interfeysi
st.set_page_config(page_title="Uy Qurilishi: Foyda Kalkulyatori", page_icon="🏠")
st.title("Uy Qurilishi: Sof Foyda Kalkulyatori")

# Foydalanuvchi input
area = st.number_input("Maydonni kiriting (m²):", min_value=0.0, step=1.0)
is_roof_closed = st.radio("Uyning tomi qanday?", ["Usti yopiq", "Usti ochiq"]) == "Usti yopiq"

# Hisoblash va natija
if area > 0:
    result = calculate_profit(area, is_roof_closed)

    st.subheader("Hisob natijalari:")
    for key, value in result.items():
        st.write(f"**{key}**: {value}")
else:
    st.info("Maydonni kamida 1 m² kiriting.")
