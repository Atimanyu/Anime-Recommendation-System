import streamlit as st
from RecommenderEngine import get_recommendations_from_query

st.markdown('# :japanese_castle: Anime Recommendation System')
input_data = st.text_input("Enter anime name to get recommendations")
st.write('')
st.write('')
# st.dataframe(get_recommendations_from_query(input_data,50),hide_index=True)

# Assume this is your DataFrame with the top N recommendations
# Each row has 'Name' and 'ImageURL' columns
if(input_data!=''):
    top_recs = get_recommendations_from_query(input_data,50)  # or however you call it
    cards_per_row = 3

    # Iterate in groups

    for i in range(0, len(top_recs), cards_per_row):
        cols = st.columns(cards_per_row)
        for j, (_, row) in enumerate(top_recs.iloc[i:i+cards_per_row].iterrows()):
            with cols[j]:
                st.markdown(
                    f"""
                    <div style='display: flex; justify-content: center; gap: 15px'>
                        <img src="{row['Image URL']}" style="
                            width: 100%;
                            height: 300px;
                            object-fit: cover;
                            border-radius: 10px;
                        ">
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"""
                    <div style='
                        text-align: center;
                        font-weight: bold;
                        white-space: nowrap;
                        overflow: hidden;
                        text-overflow: ellipsis;
                        max-width: 100%;
                        margin-top: 5px;
                    '>{row['Name']}</div>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown("---")
else:
    st.markdown("### Please enter an anime name to get recommendations‼️")