from django.conf.urls import url
from core.views import MatchUpDetailView
from core.views import TeamStatDetailView
from core.views import PlayerStatDetailView
import core.views as core_view

urlpatterns = [
	url(r'^roster/$', MatchUpDetailView.as_view(), name='rosters'),
	url(r'^team_standings/$', TeamStatDetailView.as_view(), name='team_standings'),
	url(r'^player_stats/$', PlayerStatDetailView.as_view(), name='player_stats'),
	url(r'^schedule/$', core_view.schedule, name='schedule'),

]