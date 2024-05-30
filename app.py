import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from st_pages import Page, show_pages, add_page_title,add_indentation,show_pages_from_config
from pathlib import Path


# Define the Open Graph tags
og_title = "데이터분석언어 기말프로젝트 6조-상권분석"
og_description = "서울시 공공데이터를 활용한 상권 분석"
og_image = "URL_to_your_image.jpg"

# Create HTML with Open Graph meta tags
html_code = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta property="og:title" content="{og_title}" />
    <meta property="og:description" content="{og_description}" />
    <meta property="og:image" content="{og_image}" />
</head>
<body>
</body>
</html>
"""

# Use st.components.v1.html to render the HTML
st.components.v1.html(html_code, height=0)

# st.set_page_config(page_title='데이터분석언어 6조', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

def pages():
    main_page = 'app.py'
    seoul_main = "pages/seoul_main.py"
    jongro_food_corr = "pages/jongro_food_corr.py"
    jonro_food_graph = "pages/jonro_food_graph.py"

    show_pages(pages=
        [
            Page(main_page, "데이터분석언어 기말과제 6조 - 상권분석", icon="🟥"),
            Page(seoul_main, "서울시 자치구내 상권구분", icon="🟧"),
            Page(jongro_food_corr, "종로구 요식업 - 변수/상관관계", icon="🟨"),
            Page(jonro_food_graph, "종로구 요식업 - 그래프 시각화", icon="🟩"),
        ]
    )

    add_page_title()  # Optional method to add title and icon to current page





#### session state ####
if "font" not in st.session_state:
    st.session_state.font = ''



def unique(list):
    x = np.array(list)
    return np.unique(x)

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '/customFonts']
    font_files = fm.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)


# 버튼 상태를 유지하기 위해 session state 사용
if 'expanded1' not in st.session_state:
    st.session_state.expanded1 = False

if 'expanded2' not in st.session_state:
    st.session_state.expanded2 = False

if 'expanded3' not in st.session_state:
    st.session_state.expanded3 = False

def toggle_text1():
    st.session_state.expanded1 = not st.session_state.expanded1

def toggle_text2():
    st.session_state.expanded2 = not st.session_state.expanded2

def toggle_text3():
    st.session_state.expanded3 = not st.session_state.expanded3



def main_text():
    st.header("서울시 상권분석 프로젝트")
    # st.subheader('기말과제 6조-상권분석')
    st.markdown("**데이터 갱신일:** 2024-05-26")
    # st.subheader('상권분석 가설')

    st.markdown("""
    **상권분석을 위한 데이터 분석**
    - 서울 자치구의 서비스 업종 비율 및 상권코드별 구분
    - 종로구 요식업에 영향을 주는 변수 분석
    - 당월 매출을 기준으로 상권의 매출 예상 
    """)

    # 버튼을 클릭하면 텍스트를 토글
    st.button("1️⃣ 사용 데이터", on_click=toggle_text2)
    if st.session_state.expanded2:
        st.write("2019년 ~ 2023년 분기별 서울시 상권 데이터 ")
        st.image('./data/data_drawio.png')

    # 버튼을 클릭하면 텍스트를 토글
    st.button("2️⃣ 분석 목적", on_click=toggle_text1)

    if st.session_state.expanded1:
        st.write("""
        <div style="font-weight: bold; font-size: 14px;">
        2019년 ~ 2023년 상권 데이터를 통하여 각 지표 ( 매출, 점포수, 유동인구, 상주인구 등)간 상관관계를 확인하고,<br/>
        상권의 매출에 영향을 주는 지표를 선정한다. 더 나아가 해당 지표를 통해 앞으로 유명한 상권후보지를 선정하고, <br/>
        해당 지역에서 유명한 업종을 추천하고, 매출을 예측한다.
        </div>
        """, unsafe_allow_html=True)


    # 버튼을 클릭하면 텍스트를 토글
    st.button("3️⃣ 분석방법 및 순서", on_click=toggle_text3)

    if st.session_state.expanded3:
        st.markdown("""
        **상권분석을 위한 데이터 분석 순서**
        <div style="font-weight: bold;">

        1)	상권의 지리적 범위를 대규모 단위 (서울시) -> 소규모 단위(특정 자치구, 길, 동)로 축소시켜 분석하고자 하는 특정 자치구의 상권 분류 기준(골목상권, 발달상권, 전통시장, 관광특구)에 따라 데이터 분석을 수행한다.
        2)	특정 자치구의 데이터 분석을 통해 상권에 형성에 영향을 주는 인자를 정량적 / 정성적으로 평가하여 주된 요인을 선정한다
        3)	주요 인자로 선정된 지표를 통해 선정된 자치구내에 유망한 상권이 될 가능성이 있는 상권 배후지를 선정한다.
        4)	선정된 상권 배후지에서 유망한 업종을 추천하고, 주요인자를 통해 매출을 예측한다.
        </div>
        """,unsafe_allow_html=True)

# def data_index_btn():
#     data_list = ['연령별 임금 및 근로시간', '연령별 임금 및 근로시간2']
#     clicked_buttons = [False] * len(data_list)  # 각 버튼의 클릭 여부를 저장하는 리스트
#
#     for i, data in enumerate(data_list):
#         clicked_buttons[i] = st.button(f'{data}')
#
#     # 각 버튼의 클릭 여부를 확인하여 이벤트 처리
#     for i, data in enumerate(data_list):
#         if clicked_buttons[i]:
#             # 페이지 이동을 위한 URL 설정
#             if data == '연령별 임금 및 근로시간':
#                 page_url = 'pages/seoul_main.py'
#                 st.switch_page(page_url) ### page 이동 ###
#
#             elif data == '연령별 임금 및 근로시간2':
#                 page_url = ''




def main():

    ### loading 시 main page로 이동 ###
    pages()

    ### custtom font 등록하기 ###
    fontRegistered()
    # fontNames = [f.name for f in fm.fontManager.ttflist]
    # default_font_index = fontNames.index("Malgun Gothic") if "Malgun Gothic" in fontNames else 0
    # #### session state에 값이 없으면 default_font_index로 설정하고, 값이 잇으면 session state에서 fontNames에서 선택한 font의 index를 찾아서 표시함
    # fontname = st.selectbox("폰트 선택", fontNames, index=fontNames.index(st.session_state.font) if st.session_state.font!='' else default_font_index)
    #
    # ### font 이름이 변경 되었을 때 감지 ###
    # if st.session_state.font != fontname:
    #     if "font" in st.session_state:
    #         st.session_state.font = fontname

    # 초기 폰트를 Malgun Gothic으로 설정
    initial_font = "Malgun Gothic"

    # 폰트 이름 고정
    st.session_state.font = initial_font

    main_text()
    # data_index_btn()






if __name__ == '__main__':
    main()
    # print("##")
