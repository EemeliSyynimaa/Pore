__author__ = 'eeneku'

import home
import intro
import settings

states = {'home': home.Home, 'intro': intro.Intro, 'settings': settings.Settings}
enter_state = 'home'