from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LastNGames, MeasureTypeDetailedDefense, Month, PaceAdjust, PerModeDetailed, Period, PlusMinus, Rank, Season, SeasonTypeAllStar, GameSegmentNullable, LeagueIDNullable, LocationNullable, OutcomeNullable, SeasonSegmentNullable, ShotClockRangeNullable, ConferenceNullable, DivisionNullable


class TeamDashboardByGameSplits(Endpoint):
    endpoint = 'teamdashboardbygamesplits'
    expected_data = {'ByActualMarginTeamDashboard': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'CFID', 'CFPARAMS'], 'ByHalfTeamDashboard': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'CFID', 'CFPARAMS'], 'ByPeriodTeamDashboard': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'CFID', 'CFPARAMS'], 'ByScoreMarginTeamDashboard': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'CFID', 'CFPARAMS'], 'OverallTeamDashboard': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'CFID', 'CFPARAMS']}

    def __init__(self,
                 team_id,
                 last_n_games=LastNGames.default,
                 measure_type_detailed_defense=MeasureTypeDetailedDefense.default,
                 month=Month.default,
                 opponent_team_id=0,
                 pace_adjust=PaceAdjust.default,
                 per_mode_detailed=PerModeDetailed.default,
                 period=Period.default,
                 plus_minus=PlusMinus.default,
                 rank=Rank.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 date_from_nullable='',
                 date_to_nullable='',
                 game_segment_nullable=GameSegmentNullable.default,
                 league_id_nullable=LeagueIDNullable.default,
                 location_nullable=LocationNullable.default,
                 outcome_nullable=OutcomeNullable.default,
                 po_round_nullable='',
                 season_segment_nullable=SeasonSegmentNullable.default,
                 shot_clock_range_nullable=ShotClockRangeNullable.default,
                 vs_conference_nullable=ConferenceNullable.default,
                 vs_division_nullable=DivisionNullable.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'TeamID': team_id,
                'LastNGames': last_n_games,
                'MeasureType': measure_type_detailed_defense,
                'Month': month,
                'OpponentTeamID': opponent_team_id,
                'PaceAdjust': pace_adjust,
                'PerMode': per_mode_detailed,
                'Period': period,
                'PlusMinus': plus_minus,
                'Rank': rank,
                'Season': season,
                'SeasonType': season_type_all_star,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'GameSegment': game_segment_nullable,
                'LeagueID': league_id_nullable,
                'Location': location_nullable,
                'Outcome': outcome_nullable,
                'PORound': po_round_nullable,
                'SeasonSegment': season_segment_nullable,
                'ShotClockRange': shot_clock_range_nullable,
                'VsConference': vs_conference_nullable,
                'VsDivision': vs_division_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.by_actual_margin_team_dashboard = Endpoint.DataSet(data=data_sets['ByActualMarginTeamDashboard'])
        self.by_half_team_dashboard = Endpoint.DataSet(data=data_sets['ByHalfTeamDashboard'])
        self.by_period_team_dashboard = Endpoint.DataSet(data=data_sets['ByPeriodTeamDashboard'])
        self.by_score_margin_team_dashboard = Endpoint.DataSet(data=data_sets['ByScoreMarginTeamDashboard'])
        self.overall_team_dashboard = Endpoint.DataSet(data=data_sets['OverallTeamDashboard'])
