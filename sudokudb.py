import streamlit as st

st.title("Streamlit + Neon DB 테스트")

try:
  conn = st.connection("postgresql", type="sql")

  df = conn.query("SELECT * FROM sudoku_scores;", ttl="10m")

  st.success("Neon DB 연결")
  st.dataframe(df)

except Exception as e:
  st.error(f"연결 중 오류: {e}")