import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit 設定
st.set_page_config(page_title="Student Scores Dashboard", layout="wide")
st.title("📊 Student Scores Dashboard")

# 固定檔案路徑（請修改為你的實際路徑）
file_path = 'user_data_re.csv'  # ⚠️ 確認放在專案目錄或用相對路徑

try:
    df = pd.read_csv(file_path)
    
    # 顯示前幾筆資料
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    # 顯示統計摘要
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # 畫分數分布圖
    st.subheader("Score Distributions")
    subjects = ['chinese_score', 'math_score', 'english_score']
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    colors = sns.color_palette("Set2")
    
    for i, subject in enumerate(subjects):
        if subject in df.columns:
            sns.histplot(df[subject], bins=10, kde=True, color=colors[i], ax=axes[i])
            axes[i].set_title(f'{subject.replace("_", " ").title()} Distribution')
            axes[i].set_xlabel('Score')
            axes[i].set_ylabel('Count')
        else:
            axes[i].text(0.5, 0.5, f"No data for {subject}", ha='center', va='center')
            axes[i].set_axis_off()
    
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f"❌ File not found: {file_path}")
except Exception as e:
    st.error(f"❌ An error occurred: {e}")
