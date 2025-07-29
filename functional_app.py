import streamlit as st

def calculate_profit(area_m2, construction, transport, sales, land, closed_price, open_price, tax_rate):
    total_cost_per_m2 = construction + transport + sales + land
    tax_multiplier = 1 + (tax_rate / 100)

    results = {}

    for is_roof_closed in [True, False]:
        selling_price = closed_price if is_roof_closed else open_price
        profit_per_m2 = selling_price - total_cost_per_m2 * tax_multiplier
        total_profit = profit_per_m2 * area_m2

        key = "Usti yopiq" if is_roof_closed else "Usti ochiq"
        results[key] = {
            "1 m² Sotuv narxi": f"${selling_price}",
            "1 m² Xarajat (soliqsiz)": f"${total_cost_per_m2}",
            f"1 m² Xarajat ({tax_rate}% soliq bilan)": f"${round(total_cost_per_m2 * tax_multiplier, 2)}",
            "1 m² Foyda": f"${round(profit_per_m2, 2)}",
            "Umumiy foyda": f"${round(total_profit, 2)}"
        }

    return results

# Streamlit UI
st.title("Uy Qurilish Foyda Hisoblagichi")

st.subheader("Maydon va xarajatlarni kiriting:")

area = st.number_input("Uyning maydoni (m²)", min_value=1.0, value=100.0)

construction = st.number_input("1 m² uchun qurilish xarajati ($)", min_value=0.0, value=1000.0)
transport = st.number_input("1 m² uchun transport xarajati ($)", min_value=0.0, value=100.0)
sales = st.number_input("1 m² uchun savdo xarajati ($)", min_value=0.0, value=50.0)
land = st.number_input("1 m² uchun yer xarajati ($)", min_value=0.0, value=200.0)

st.subheader("Sotuv narxlari va soliq foizini kiriting:")
roof_closed_price = st.number_input("1 m² uchun usti yopiq narxi ($)", min_value=0.0, value=1800.0)
roof_open_price = st.number_input("1 m² uchun usti ochiq narxi ($)", min_value=0.0, value=1700.0)
tax_rate = st.number_input("Soliq foizi (%)", min_value=0.0, value=27.0)

if st.button("Hisoblash"):
    result = calculate_profit(
        area,
        construction,
        transport,
        sales,
        land,
        roof_closed_price,
        roof_open_price,
        tax_rate
    )

    st.subheader("Hisob-kitob natijalari:")
    for roof_type, data in result.items():
        st.markdown(f"### {roof_type}")
        for key, value in data.items():
            st.write(f"**{key}**: {value}")
        st.markdown("---")
