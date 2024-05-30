import streamlit as st
import pandas as pd


def load_img2(option2):

    if option2 == '매출지표':
        st.image('./data/sales_corr.png')

    elif option2 =='유동인구':
        st.image('./data/flow_corr.png')

    elif option2 =='직장인구/상주인구':
        st.image('./data/live__job_corr.png')

    elif option2 =='점포':
        st.image('./data/store_corr.png')

def main_select_box2():
    # 첫 번째 selectbox
    option2 = st.selectbox(
        '상관관계 분석 시각화:',
        ['매출지표', '유동인구', '직장인구/상주인구', '점포']
    )

    load_img2(option2)

def text_select_feature():
    data = {
        "구분": ["매출", "유동인구", "상주/직장인구", "점포"],
        "변수": ["수/목/금 매출,시간대 17~21시 매출",'없음','총 직장인구수,남/여성 직장인구수,연령대 30~40 직장인구수', '점포밀도, 프랜차이즈 점포수'],
    }
    # 데이터프레임 생성
    df = pd.DataFrame(data)

    # 스타일링 설정
    styled_df = df.style.set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#f0f0f0'), ('font-size', '14px')]},
        {'selector': 'td', 'props': [('font-size', '12px')]},
        {'selector': 'th.col_heading.level0.col1', 'props': [('min-width', '150px')]}  # 구분 열의 너비 설정
    ])

    # 데이터프레임 출력 (인덱스 표시하지 않음)
    st.write(styled_df.hide(axis='index').to_html(), unsafe_allow_html=True)


def main():

    # 페이지 제목 설정
    st.title('🕍 종로구 요식업 영향 변수 분석')
    st.subheader('1️⃣ 변수 선정')
    st.markdown("""
        <div style="font-weight: bold; line-height: 2; font-size :7px">
            <p style="margin-bottom: 5px;"><strong></strong></p>
            <ul>
                <li>피어슨 상관관계 : 두 변수 간 선형 관계의 강도와 방향을 측정하는 통계적 방법</li>
                <li>검정 통계량 회귀분석 : 모델이 데이터에 얼마나 적합한지를 평가하는 통계적 기법으로, 예측 변수의 영향력을 분석</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("")
    st.markdown("")

    st.subheader('2️⃣ 상관관계 ')
    st.write("매출과 연관성이 있는 변수")
    text_select_feature()


    main_select_box2()



    st.subheader('3️⃣ 선형 회귀 학습 후 계수')
    st.image('./data/liner_coeffi.png')

    # multi_select_btn()




if __name__ == "__main__":
    main()