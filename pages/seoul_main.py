import streamlit as st
import pandas as pd



#### session state ####


# def multi_select_btn():
#     col1, col2 = st.columns([2,1])
#
#     # 라벨을 숨기기 위해 빈 텍스트 상자를 만듭니다.
#     with col1:
#         select_cols = st.multiselect('항목 선택',
#             options=st.session_state.df_age_salary['고용형태'].unique(),
#             max_selections=3, placeholder='통계자료를 선택해 주세요',label_visibility="collapsed")
#
#     # 버튼을 아래로 정렬하여 배치합니다.
#     with col2:
#         select_btn = st.button('시각화', key="visualization_button")
#
#     if select_btn:
#         ### graph 생성 ##
#         st.subheader('전체근로자')
#         new_df = st.session_state.df_age_salary
#         draw_graph(select_cols,new_df)
#
#         st.subheader('정규근로자')
#         new_df = st.session_state.df_age_full_time
#         draw_graph(select_cols,new_df)
#
#         st.subheader('비정규근로자')
#         new_df = st.session_state.df_age_not_full_time
#         draw_graph(select_cols,new_df)


def text_service_definition():
    data = {
        '구분' : ['요식업','서비스업','소매업'],
        '세부 서비스 업종' : [
            ['중식음식점', '분식전문점', '커피-음료', '제과점', '치킨전문점', '한식음식점',
            '일식음식점', '양식음식점', '패스트푸드점', '호프-간이주점',],
            ['네일숍','피부관리실','세탁소','가전제품수리','부동산중개업','여관','노래방','일반교습학원', '예술학원',
            '자동차미용','미용실','외국어학원', '스포츠 강습','일반의원', '치과의원','한의원','고시원'],
            ['슈퍼마켓','육류판매','편의점','가방','컴퓨터및주변장치판매','핸드폰','미곡판매','수산물판매','화초'
                ,'청과상','반찬가게','시계및귀금속','일반의류', '신발', '안경', '의약품', '의료기기', '서적'
                ,'문구', '화장품', '운동/경기용품', '자전거 및 기타운송장비', '섬유제품', '완구', '애완동물'
                , '가구','가전제품', '철물점', '인테리어'
                , '조명용품', '전자상거래업','당구장', '골프연습장', 'PC방', '스포츠클럽', '자동차수리',]
        ]
    }
    # DataFrame 생성
    df = pd.DataFrame(data, columns=['구분','세부 서비스 업종'])

    # Streamlit에서 DataFrame 표시
    st.write("서비스 업종 및 세부 서비스 업종")
    st.dataframe(df)

def load_img(option1):

    if option1 == '서비스 업종비율 변화':
        st.image('./data/service_year_percent.png')

    elif option1 =='요식업 업종비율 변화':
        st.image('./data/service_3_year_percent.png')

    elif option1 =='서울시 자치구별 서비스업종비율':
        st.image('./data/service_districe_all.png')

    elif option1 =='서울 자치구별 상권구분비율':
        st.image('./data/seoul_district.png')

    elif option1 =='서울시 점포현황':
        st.image('./data/seoul_store.png')


def main_select_bodx():
    # 첫 번째 selectbox
    option1 = st.selectbox(
        '서울시 자치구 분석내용 그래프 :',
        ['서비스 업종비율 변화', '요식업 업종비율 변화', '서울시 자치구별 서비스업종비율',
         '서울 자치구별 상권구분비율' , '서울시 점포현황'
         ]
    )

    load_img(option1)

def text_feature_definition():
    data = {
        "항목": ["상권", "상권", "상권", "상권", "서비스 업종", "인구", "인구", "인구"],
        "구분": ["골목상권", "발달상권", "전통시장", "관광특구", "서비스업종", "유동인구", "직장인구", "상주인구"],
        "설명 및 예시": [
            "골목상권 일정 점포 수 (30개) 이상의 상권이면서 골목점포 밀집도가 높은 상권으로 주거 지역이 밀집된 곳에 형성<br><br>예시: 성수동 카페거리, 경리단길 남측, 영등포시장3번 등",
            "2천 제곱미터 이내 50개 이상의 상점이 분포하는 상점가로 8개 업종의 점포가 밀집한 상가 업소 밀집지역<br><br>예시: 노량진역(노량진), 용산전자상가(용산역), 가산디지털단지",
            "오랜 기간에 걸쳐 일정한 지역에서 자연발생으로 형성된 시장<br><br>예시: 독산동 우시장, 청량리 청과물시장, 경동시장 등",
            "관광활동이 주로 이루어지는 지역적 공간 내 입지한 상권<br><br>예시: 잠실관광특구, 명동 남대문 북창동 다동 교동 관광특구, 강남 마이스 관광특구",
            "총 63개의 항목으로 분류됨<br><br>예시: 미용실, 한식음식점, 중식음식점, 커피-음료, 일반의류 등",
            "특정지점을 기준으로 일정시간동안 이동한 총보행량으로 정의됨. 서울시 에서는 주기적으로 유동인구에 대한 분석을 실시하고 있으며, 유동인구 조사를 통해 정책자료 및 공공기관의 유동인구 관련 기준 정립, 학술연구 등에 사용",
            "서울시 상권 영역 내 직장이 위치한 인구 정보",
            "한 지역에 주소를 두고 계속 머물러 사는 내/외국인 인구로 일시적 현재자는 제외하고 일시적 부재자를 포함한 인구로 대게 주민등록상 인구를 의미"
        ]
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
    st.title('🕍 서울시 자치구 데이터')
    st.subheader('1️⃣변수별 정의')

    text_feature_definition()

    st.markdown("")
    st.markdown("")

    st.subheader('2️⃣ 서비스 업종 구분')


    st.markdown("""
    - 총 63개의 서비스 형태를 분석의 용이성을 위하여 총 3가지로 분류함 ( 요식업 / 서비스업 / 소매업 )
    """)
    text_service_definition()

    st.subheader('3️⃣ 서울 자치구별 데이터 시각화')
    main_select_bodx()

    # multi_select_btn()




if __name__ == "__main__":
    main()