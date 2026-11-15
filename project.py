#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ipl_matches_2026.csv')

print('\nEnter 1 to check your team total wins')
print('Enter 2 to check if your team wins Toss and the match')
print('Enter 3 to check which player has won most Player of the match')
print('Enter 4 to check how many matches are played in each stadium')
print('Enter 5 to check how many teams scores more than 200')
print('Enter 6 to check average run scored in a match')

num = input("\nEnter a valid value: ")

if num == '1':
    team = input('Enter your favorite team: ')

    if team in df['winner'].values:
        win = df[df['winner'] == team].shape[0]
        print(f'{team} has won {win} matches.')

        wins = df['winner'].value_counts()
        color1 = ['red' if i == team else '#005aff' for i in wins.index]
                
        sns.barplot(x= wins.values, y= wins.index, palette=color1, hue=wins.index, legend= False)
    
    else:
        print('Invalid team name')
            

elif num == '2':
    team2 = input('Enter team name: ')

    toss_winner = df['toss_winner']
    match_win = df['winner']
            
    common = df[df['toss_winner'] == df['winner']]
    win_count = common['toss_winner'].value_counts()
    total_matches_per_team = ((df['team1'] == team2) |
                              (df['team2'] == team2)).sum()


    if team2 in win_count.index:
        per_team = win_count.get(team2, 0)
        overall_win = (df['winner'] == team2).sum()
        percent = (per_team/total_matches_per_team)*100

        print(f'---{team2} won {overall_win} matches outoff {total_matches_per_team} matches---')
        print(f'---{per_team} matches won from {total_matches_per_team} matches after winning a toss---')
        print(f'---Percentage of the team that they won the match after winning the toss {percent}%---')

        color2 = ['Red' if x == team2 else '#005aff' for x in win_count.index]
        sns.barplot(x=win_count.values,
                    y=win_count.index,
                    hue=win_count.index,
                    legend=False,
                    palette=color2)
                
    else:
        print('Invalid team name')

elif num == '3':
            
    player = input('Enter the player of the match name you want to check: ')

    if player in df['player_of_match'].values:
        player_win = (df['player_of_match'] == player).sum()
        print(f'---{player} has won Player of the Match {player_win} times.---')

        top_player = df['player_of_match'].value_counts().head(10)

        sns.barplot(x= top_player.values,
                    y= top_player.index)

        plt.title("---Top 10 Players with most Player of the match---")
        plt.xlabel('Total Man of the Match')
        plt.ylabel('Player of the Match')

elif num == '4':

    stadium = input('Enter any Stadium name to know how many matches are played in it: ')
    stand_count = df['venue'].value_counts()
            
    if stadium in stand_count.index:
                
        total_match = stand_count[stadium]
        print(f'---Total matches played in {stadium} is {total_match}.---')
        color3 = ['Red' if x == stadium else '#005aff' for x in stand_count.index]

        sns.barplot(x= stand_count.values,
        y= stand_count.index,
        hue= stand_count.index,
        palette= color3,
        legend=False)

elif num == '5':
    total_teams = df['team1'].value_counts()
    runs1 = df['team1_runs']
    result = df[df['team1_runs'] >= 200]

    team_runs = result['team1'].value_counts()

    sns.barplot(x= team_runs.values,
                y= team_runs.index,
                hue= team_runs.index,
                legend= False)
    plt.xlabel('Total wins')
    plt.ylabel('Teams')
    plt.title('---Teams That Have Scored 200 or More Runs the Most Times.---')

elif num == '6':
    runs_team1 = (df['team1_runs']).values
    runs_team2 = (df['team2_runs']).values

    runs1 = df['team1_runs']

    filtered = runs1[runs1 > 50]

    avg = filtered.mean()

    print(f'---Average runs scored ina a match : {avg}---')    

else:
    print('Please enter a valid option.')


# %%
