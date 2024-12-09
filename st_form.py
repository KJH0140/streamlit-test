import streamlit as st

st.title('제목')

# 'with' 표기법을 사용한 전체 예시
st.header('소제목')
st.subheader('설명')

with st.form('my_form'):
    st.subheader('상위항목')

    # 입력 위젯
    coffee_bean_val = st.selectbox('하위항목1분류', ['하위항목1-1', '하위항목1-2', '하위항목1-3'])
    coffee_roast_val = st.selectbox('하위항목2분류', ['하위항목2-1', '하위항목2-2', '하위항목2-3'])
    brewing_val = st.selectbox('하위항목3분류', ['하위항목3-1', '하위항목3-2', '하위항목3-3'])
    serving_type_val = st.selectbox('하위항목4분류', ['하위항목4-1', '하위항목4-2', '하위항목4-3'])
    milk_val = st.select_slider('하위항목5분류', ['최저', '저', '중저', '중', '중고', '고', '최고'])
    owncup_val = st.checkbox('체크박스')

    # 모든 양식은 제출 버튼을 가져야 함
    submitted = st.form_submit_button('제출')

if submitted:
    st.markdown(f'''
        결과 :
        - 하위항목1 : `{coffee_bean_val}`
        - 하위항목2 : `{coffee_roast_val}`
        - 하위항목3 : `{brewing_val}`
        - 하위항목4 : `{serving_type_val}`
        - 하위항목5 : `{milk_val}`
        - 체크박스 : `{owncup_val}`
        ''')
else:
    st.write('결과 없음.')


# # 객체 표기법을 사용한 짧은 예시
# st.header('2. 객체 표기법 예시')

# form = st.form('my_form_2')
# selected_val = form.slider('값 선택')
# form.form_submit_button('제출') #모든 양식은 st.form_submit_button을 포함해야 함.
# #st.button과 st.download_button은 양식에 추가할 수 없습니다.
# st.write('선택된 값: ', selected_val)
