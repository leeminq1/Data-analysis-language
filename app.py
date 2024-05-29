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


def pages():
    main_page = 'app.py'
    seoul_main = "pages/seoul_main.py"
    jongro_food_corr = "pages/jongro_food_corr.py"
    jonro_food_graph = "pages/jonro_food_graph.py"

    show_pages(pages=
        [
            Page(main_page, "상권분석 개요", icon="🔶"),
            Page(seoul_main, "서울시 자치구내 상권구분", icon="🔷"),
            Page(jongro_food_corr, "종로구 요식업 - 변수/상관관계", icon="🟨"),
            Page(jonro_food_graph, "종로구 요식업 - 그래프 시각화", icon="🟥"),
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



def main_text():
    st.header("데이터분석언어 6조 - 상권분석")
    st.markdown("**데이터 갱신일:** 2024-05-26")
    st.subheader('상권분석 가설')

    st.markdown("""
    **상권분석을 위한 데이터 분석**

    - 가설 1 : 유동인구와 매출 간의 상관관계
    - 가설 2 : 직장인 수, 거주자 수와 매출과의 상관관계
    - 가설 3 : 주변 업소 수(개/폐점, 주변 업체 수)와 매출 간의 상관관계
    - 가설 4 : 코로나19와 매출 간의 상관관계
    """)


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
