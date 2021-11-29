
#%%
import requests
import pandas as pd
import json
import streamlit as st
import plotly.express as px
from PIL import Image
import streamlit_analytics
with streamlit_analytics.track():
    with open('sample.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
        
    our_league={'Name':['Michał', 'Marcin','Tomek', 'Darek'],'Points':['14','13','11','7']}
    our_league_df=pd.DataFrame(our_league) 
    #print(json.dumps(json_object, indent=4))
    ###############################3
    biggest_streak=json_object['response']['biggest']['streak']
    #print(biggest_streak)
    biggest_wins=json_object['response']['biggest']['wins']
    biggest_loses=json_object['response']['biggest']['loses']
    biggest_goals_for=json_object['response']['biggest']['goals']['for']
    biggest_goals_against=json_object['response']['biggest']['goals']['against']
    clean_sheet=json_object['response']['clean_sheet']
    failed_to_score=json_object['response']['failed_to_score']
    penalty_scored=json_object['response']['penalty']['scored']
    penalty_missed=json_object['response']['penalty']['missed']
    #cards_yellow=json_object['response']['cards']['yellow']
    biggest_streak_pd=pd.DataFrame([biggest_streak],index=['biggest_streak'])
    biggest_wins_pd=pd.DataFrame([biggest_wins],index=['biggest_wins'])
    biggest_loses_pd=pd.DataFrame([biggest_loses],index=['biggest_loses'])
    biggest_goals_for_pd=pd.DataFrame([biggest_goals_for],index=['biggest_goals_for'])
    biggest_goals_against_pd=pd.DataFrame([biggest_goals_against],index=['biggest_goals_against'])
    cleansheet_pd=pd.DataFrame([clean_sheet], index=['clean_sheet'])
    
    failed_to_score_pd=pd.DataFrame([failed_to_score], index=['failed_to_score'])
    
    penalty_pd=pd.DataFrame([penalty_scored, penalty_missed],index=['penalty_scored','penalty_missed'])
    #####################################
    forma=json_object['response']['form']
    fixtures=json_object['response']['fixtures']
    pd1=pd.DataFrame.from_dict(fixtures)
    goals=json_object['response']['goals']
    #goals FOR
    goals2=json_object['response']['goals']['for']['average']
    golas3=json_object['response']['goals']['for']['total']
    averagegoals={}
    averagegoals['avereage_goals_for']={}
    averagegoals['avereage_goals_for']=goals2
    totalgoals={}
    totalgoals['total_goals_for']={}
    totalgoals['total_goals_for']=golas3
    #goals Against
    goalsagainst2=json_object['response']['goals']['against']['average']
    golasagainst3=json_object['response']['goals']['against']['total']
    averagegoalsagainst={}
    averagegoalsagainst['avereage_goals_against']={}
    averagegoalsagainst['avereage_goals_against']=goalsagainst2
    totalgoalsagainst={}
    totalgoalsagainst['total_goals_against']={}
    totalgoalsagainst['total_goals_against']=golasagainst3
    #Merging Dictionaries
    averagegoals.update(totalgoals)
    averagegoalsagainst.update(totalgoalsagainst)
    averagegoals.update(averagegoalsagainst)
    pd2=pd.DataFrame.from_dict(averagegoals)
    #print(pd1)
    #print(pd2) 
    #minutes Goals For, Against
    goalsforminutes=json_object['response']['goals']['for']['minute']
    pd3=pd.DataFrame.from_dict(goalsforminutes)
    df_goalsforminutes = pd3.rename(index={'total': 'total_for', 'percentage':'percentage_for'})
    golasagainstminutes=json_object['response']['goals']['against']['minute']
    #df_goalsforminutes.drop('index1',axis='columns')
    pd4=pd.DataFrame.from_dict(golasagainstminutes)
    df_goalsagainstminutes = pd4.rename(index={'total': 'total_against', 'percentage':'percentage_against'})
    result = df_goalsforminutes.append(df_goalsagainstminutes)
    #LEAGUE TABLE
    #
    with open('league_stand.json', 'r') as openfile:
    
        # Reading from json file
        json_object = json.load(openfile)
        
    #print(json.dumps(json_object, indent=4))
    proba=json_object['response'][0]['league']['standings']
    rank_list=[]
    team_id_list=[]
    team_name_list=[]
    points_list=[]
    goalsDiff_list=[]
    form_list=[]
    status_list=[]
    description_list=[]
    allgameplayed_list=[]
    allgamewin_list=[]
    allgamedraw_list=[]
    allgamelose_list=[]
    allgamegoalfor_list=[]
    allgamegoalagainst_list=[]
    home_played_list=[]
    homewin_list=[]
    homegamedraw_list=[]
    homelose_list=[]
    homegamegoalfor_list=[]
    homegamegoalagainst_list=[]
    away_played_list=[]
    awaywin_list=[]
    awaygamedraw_list=[]
    awaylose_list=[]
    awaygamegoalfor_list=[]
    awaygamegoalagainst_list=[]
    for teams in proba:
        #print(teams)
        for team in teams:
            rank=team['rank']
            team_id=team['team']['id']
            team_name=team['team']['name']
            points=team['points']
            goalsDiff=team['goalsDiff']
            form=team['form']
            status=team['status']
            description=team['description']
            allgameplayed=team['all']['played']
            allgamewin=team['all']['win']
            allgamedraw=team['all']['draw']
            allgamelose=team['all']['lose']
            allgamegoalfor=team['all']['goals']['for']
            allgamegoalagainst=team['all']['goals']['against']
            home_played=team['home']['played']
            homewin=team['home']['win']
            homegamedraw=team['home']['draw']
            homelose=team['home']['lose']
            homegamegoalfor=team['home']['goals']['for']
            homegamegoalagainst=team['home']['goals']['against']
            away_played=team['away']['played']
            awaywin=team['away']['win']
            awaygamedraw=team['away']['draw']
            awaylose=team['away']['lose']
            awaygamegoalfor=team['away']['goals']['for']
            awaygamegoalagainst=team['away']['goals']['against']
            rank_list.append(rank)
            team_id_list.append(team_id)
            team_name_list.append(team_name)
            points_list.append(points)
            goalsDiff_list.append(goalsDiff)
            form_list.append(form)
            status_list.append(status)
            description_list.append(description)
            allgameplayed_list.append(allgameplayed)
            allgamewin_list.append(allgamewin)
            allgamedraw_list.append(allgamedraw)
            allgamelose_list.append(allgamelose)
            allgamegoalfor_list.append(allgamegoalfor)
            allgamegoalagainst_list.append(allgamegoalagainst)
            home_played_list.append(home_played)
            homewin_list.append(homewin)
            homegamedraw_list.append(homegamedraw)
            homelose_list.append(homelose)
            homegamegoalfor_list.append(homegamegoalfor)
            homegamegoalagainst_list.append(homegamegoalagainst)
            away_played_list.append(away_played)
            awaywin_list.append(awaywin)
            awaygamedraw_list.append(awaygamedraw)
            awaylose_list.append(awaylose)
            awaygamegoalfor_list.append(awaygamegoalfor)
            awaygamegoalagainst_list.append(awaygamegoalagainst)
    list_of_tuples_all = list(zip(rank_list,
    team_id_list,
    team_name_list,
    form_list,
    status_list,
    description_list,
    allgameplayed_list,
    allgamewin_list,
    allgamedraw_list,
    allgamelose_list,
    goalsDiff_list,
    allgamegoalfor_list,
    allgamegoalagainst_list,points_list))
    dfleagueall = pd.DataFrame(list_of_tuples_all, columns = ['rank', 'team_id','team_name','team form','status','description','played','win','draw','lose','goals_diff','goals_for','goals_against','points']) 
    dfleagueall=dfleagueall.set_index('rank')
    #%% streamlit run sportAPI.py
    
    st.set_page_config(page_title='ŁKS STATISTICS')
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)
    padding = 0
    st.markdown(f""" <style>
        .reportview-container .main .block-container{{
            padding-top: {padding}rem;
            padding-right: {padding}rem;
            padding-left: {padding}rem;
            padding-bottom: {padding}rem;
        }} </style> """, unsafe_allow_html=True)
    st.header('League Table')
    st.dataframe(dfleagueall)
    st.header('ŁKS  Form: '+forma)
    st.header('Fixtures')
    #pd1['index1'] = pd1.index
    #cols = pd1.columns.tolist()
    #cols = cols[-1:] + cols[:-1]
    #pd1=pd1[cols]
    #df_reset=pd1.reset_index(drop=True)
    
    st.dataframe(pd1)
    
    fig = px.bar(pd1, x=['wins','draws','loses'], y=["home", "away", "total"], title="Played Games")
    st.plotly_chart(fig)
    st.header('Goals')
    def left_align(df):
        left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
        left_aligned_df = left_aligned_df.set_table_styles(
            [dict(selector='th', props=[('text-align', 'left')])]
        )
        return left_aligned_df
    left_align(pd2)
    
    
    st.table(pd2)
    #df_goalsforminutes[df_goalsforminutes.columns] = df_goalsforminutes.apply(lambda x: x.str.strip('%'))
    df_goalsforminutes.replace('%', '', regex=True, inplace=True)
    df_goalsforminutes=df_goalsforminutes.astype(float)
    
    
    df_goalsforminutes = df_goalsforminutes.round(decimals = 2)
    
    st.header('Goals For, Minutes')
    st.table(df_goalsforminutes.style.format({'0-15': '{:.1f}', '16-30': '{:.1f}', '31-45': '{:.1f}','46-60':'{:.1f}','61-75':'{:.1f}','76-90':'{:.1f}', '91-105':'{:.1f}','106-120':'{:.1f}'}))
    #st.dataframe(df_goalsforminutes)
    df_goalsagainstminutes.replace('%', '', regex=True, inplace=True)
    df_goalsagainstminutes=df_goalsagainstminutes.astype(float)
    st.header('Goals Against, Minutes')
    st.table(df_goalsagainstminutes.style.format({'0-15': '{:.1f}', '16-30': '{:.1f}', '31-45': '{:.1f}','46-60':'{:.1f}','61-75':'{:.1f}','76-90':'{:.1f}', '91-105':'{:.1f}','106-120':'{:.1f}'}))
    #st.dataframe(df_goalsforminutes)
    
    
    ##df['col'] = df['col'].str.rstrip('%').astype('float') / 100.0
    #NOWE
    
    st.header('Biggest Streak')
    st.dataframe(biggest_streak_pd)
    st.header('Biggest Wins')
    st.dataframe(biggest_wins_pd)
    st.header('Biggest Loses')
    st.dataframe(biggest_loses_pd)
    st.header('Biggest Goals For')
    st.dataframe(biggest_goals_for_pd)
    st.header('Biggest Goals Against')
    st.dataframe(biggest_goals_against_pd)
    st.header('Clean Sheet')
    st.dataframe(cleansheet_pd)
    st.header('Failed To Score')
    st.dataframe(failed_to_score_pd)
    st.header('Penalties')
    st.dataframe(penalty_pd)
    st.title('PLAYERS')
    LKS_stats_to_excel = pd.read_excel (r"ŁKS_stats.xlsx")
    st.dataframe(LKS_stats_to_excel)
    #####OPPONENT########
    with open('opponent.json', 'r') as openfile:
    
        # Reading from json file
        json_object_opponent = json.load(openfile)
    print(json.dumps(json_object_opponent, indent=4))
    Oppo_name=json_object_opponent['response']['team']['name']
    Oppo_forma=json_object_opponent['response']['form']
    Oppo_fixtures=json_object_opponent['response']['fixtures']
    st.header('Next Opponent: '+Oppo_name)
    st.subheader('Forma: '+Oppo_forma)
    st.subheader('Fixtures')
    Oppo_fixtures_pd=pd.DataFrame.from_dict(Oppo_fixtures)
    st.table(Oppo_fixtures_pd)
    st.header('Our league')
    st.table(our_league_df)
