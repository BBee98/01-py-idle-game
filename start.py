import functools
import inspect
import core.pydle_system as pydle_system
import core.game_scripts.actions as game_actions
import core.screen as system_game_screen

[(_, game_action_func)]=inspect.getmembers(game_actions, inspect.isfunction)

game_screen = system_game_screen.init()

pydle_system.run([game_action_func, functools.partial(system_game_screen.render, game_screen)])

