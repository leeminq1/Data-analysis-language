import streamlit as st

import folium
from folium.plugins import MarkerCluster
import geopandas as gpd

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json
from streamlit_folium import folium_static
import time



### map csv ###
if 'df_map' not in st.session_state:
    df_map = './data/map.csv'
    df_map = pd.read_csv(df_map, encoding='utf-8-sig')
    st.session_state.df_map = df_map

### geo json ###

if 'geo_data_json' not in st.session_state:
    # JSON 파일 읽기
    json_file_path = './data/geo_seoul.json'
    with open(json_file_path, encoding='utf-8-sig') as file:
        data = json.load(file)
    st.session_state.geo_data_json = data




def main_draw_map(df_fil,geo_data):
    # 기본 지도 생성
    m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, width='100%', height='100%')

    # 색상 지정
    color_dict = {
        '골목상권': 'blue',
        '발달상권': 'green',
        '전통시장': 'red',
        '관광특구': 'purple',
    }

    # 상권 리스트
    sales_top_5 = ['종각역', '대학로(혜화역)', '종로구청', '서대문역', '북촌(안국역)']
    korean_food_top_5 = ['성곡미술관', '종로5가역', '동묘앞역(동묘)', '광장시장(광장전통시장)', '종로4가']
    hof_drink_food_top_5 = ['광화문역', '삼청동', '동대문역 1번', '세검정초등학교', '이북5도청사']
    western_food_top_5 = ['종각역', '세종마을음식문화거리(금천교시장)', '서촌(경복궁역)', '이화사거리', '통인시장']
    chaina_food_top_5 = ['북촌(안국역)', '종로·청계 관광특구', '종로3가역', '동대문역']

    # MarkerCluster 추가
    marker_clusters = {}
    for key in color_dict.keys():
        marker_clusters[key] = MarkerCluster(name=key).add_to(m)

    # 각 데이터를 마커로 추가
    def add_markers(data):
        for i, row in data.iterrows():
            color = color_dict.get(row['상권_구분_코드_명'], 'gray')
            cluster = marker_clusters.get(row['상권_구분_코드_명'], None)

            # 마커 아이콘 및 색상 설정
            icon_html = ''
            popup_html = f"""
            <div style="font-family: Arial; font-size: 14px;">
                <span style="font-size: 18px; color: darkblue;"><b>{row['상권_코드_명']}</b></span><br>
                {row['상권_구분_코드_명']}<br>
                행정동 코드: {row['행정동']}<br>
                직장인수 평균 : {row['직장인수_평균']:,.0f} 명 <br>
                상주인구 평균 : {row['상주인구_평균']:,.0f} 명 <br>
                최다업종 : {row['최다업종']} <br>
                개업률 평균 : {row['개업률_평균']:,.0f} % <br>
                폐업률 평균 : {row['폐업률_평균']:,.0f} % <br>
                월매출 평균 : {row['월매출_평균']:,.0f} 원
            </div>
            """

            # top5_list에 있는 상권_코드_명은 별 모양
            if row['상권_코드_명'] in sales_top_5:
                icon_html = f"""
                <div style="color: yellow; font-size: 32px;">
                    <i class="fa-solid fa-trophy fa-spin"></i>
                </div>
                """

            elif row['상권_코드_명'] in korean_food_top_5:
                icon_html = f"""
                <div style="color: white; font-size: 32px;">
                         <i class="fa-solid fa-bowl-rice fa-spin"></i>
                </div>
                """

            elif row['상권_코드_명'] in hof_drink_food_top_5:
                icon_html = f"""
                <div style="color: blue; font-size: 32px;">
                         <i class="fa-solid fa-beer-mug-empty fa-spin"></i>
                </div>
                """

            elif row['상권_코드_명'] in western_food_top_5:
                icon_html = f"""
                <div style="color: green; font-size: 32px;">
                         <i class="fa-solid fa-pizza-slice fa-spin"></i>
                </div>
                """

            elif row['상권_코드_명'] in chaina_food_top_5:
                icon_html = f"""
                <div style="color: red; font-size: 32px;">
                         <i class="fa-solid fa-bowl-food fa-spin"></i>
                </div>
                """

            else:
                icon_html = f"""
                <div style="color: {color}; font-size: 16px;">
                    <i class="fa fa-info-circle"></i>
                </div>
                """

            if cluster:
                icon = folium.DivIcon(html=icon_html)
                popup = folium.Popup(popup_html, max_width=300)
                folium.Marker(
                    location=[row['위도'], row['경도']],
                    icon=icon,
                    popup=popup
                ).add_to(cluster)

    # 마커 추가
    add_markers(df_fil)

    # 각 데이터의 영역 면적을 원으로 표시
    def add_circles(data):
        for i, row in data.iterrows():
            if row['자치구명'] == '종로구':
                color = color_dict.get(row['상권_구분_코드_명'], 'gray')
                folium.Circle(
                    location=[row['위도'], row['경도']],
                    radius=row['영역_면적'] / 3000,  # 제곱 미터 단위
                    color=color,
                    fill=True,
                    fill_color=color,
                    fill_opacity=0.1
                ).add_to(m)

    # 원 추가
    add_circles(df_fil)

    # 자치구 경계 데이터 읽어오기 (geojson 파일 경로 지정)
    # geojson_path = f'../data/geo_seoul.json'
    # geo_data = gpd.read_file(geojson_path)

    # 자치구 경계 추가
    folium.GeoJson(
        geo_data,
        name='자치구 경계',
        style_function=lambda feature: {
            'fillColor': 'lightblue' if feature['properties']['name'] == '종로구' else 'orange',
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.3 if feature['properties']['name'] == '종로구' else 0.1,
        }
    ).add_to(m)

    # 지도 크기 조절
    # m.get_root().html.add_child(folium.Element('<style> #map { height: 90%; width: 90%; } </style>'))
    m.get_root().html.add_child(folium.Element('<style></style>'))


    return m



def main():

    # 페이지 제목 설정
    st.title('🌎서울시 상권 지도 시각화')



    df_map = st.session_state.df_map
    geo_data_json = st.session_state.geo_data_json
    m = main_draw_map(df_map, geo_data_json)


    with st.spinner('지도를 로딩중입니다....😅😅😅'):
        if m is not None:
            folium_static(m)
            st.markdown("""
                <div style="font-weight: bold; line-height: 2; font-size :7px">
                    <p style="margin-bottom: 5px;"><strong>지도 구분</strong></p>
                    <ul>
                        <li>마커 : 파란색(골목상권), 초록색(발달상권), 빨간색(전통시장), 보라색(관광특구)</li>
                        <li>순위 : <br/> 노란색 트로피(전체), 하얀색 밥(한식), 파란색 맥주잔(호프), 초록색 피자(양식),  
                                빨간색 그릇(중식)</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                <div style="font-weight: bold; line-height: 2;">
                    <p style="margin-bottom: 5px;"><strong>매출 순위</strong></p>
                    <ul>
                        <li> 1)전체 TOP 5 종각역, 대학로(혜화역), 종로구청, 서대문역, 북촌(안국역)</li>
                        <li> 2)한식 TOP 5 : 성곡미술관, 종로5가역, 동묘앞역(동묘), 광장시장(광장전통시장), 종로4가</li>
                        <li> 3)양식 TOP 5 : 종각역, 세종마을음식거리(금천교시장),서촌(경복궁역), 이화사거리, 통인시장</li>
                        <li> 4)중식 TOP 5 : 북촌(안국역), 종로·청계 관광특구, 종로3가역, 동대문역</li>
                        <li> 5)호프/간이주점 TOP 5 : 광화문역, 삼청동, 동대문역 1번, 세검정초등학교, 이북5도청사</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)







if __name__ == "__main__":
    main()