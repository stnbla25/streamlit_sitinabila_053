import streamlit as st
from scipy import stats

def anova_test(data):
    # Lakukan uji ANOVA
    f_value, p_value = stats.f_oneway(*data)
    return f_value, p_value

def main():
    st.title("Uji ANOVA dengan Streamlit")

    # Tambahkan input untuk setiap kelompok data
    group_data = []
    num_groups = st.number_input("Jumlah kelompok data", min_value=2, max_value=10, value=2, step=1)
    for i in range(num_groups):
        group_name = st.text_input(f"Kelompok {i+1}")
        data = st.text_area(f"Data Kelompok {i+1}", "1, 2, 3, 4, 5")
        data = [float(x.strip()) for x in data.split(",") if x.strip()]
        group_data.append(data)

    # Tombol untuk melakukan uji ANOVA
    if st.button("Lakukan Uji ANOVA"):
        f_value, p_value = anova_test(group_data)
        st.write(f"Nilai F: {f_value}")
        st.write(f"Nilai p: {p_value}")

if __name__ == "__main__":
    main()