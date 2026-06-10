import inspect
import core.pydle_system as pydle
import core.game_scripts.actions as game_actions

[(name, value)]=inspect.getmembers(game_actions, inspect.isfunction)

pydle.run(name)

