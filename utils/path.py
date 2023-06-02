import os,sys

current_path = os.path.abspath(__file__)

directory_path = os.path.dirname(os.path.dirname(current_path))

report_path = os.path.join(directory_path, 'report')

test_data_path = os.path.join(directory_path, 'test_game_second','test_data')

test_game_path = os.path.join(directory_path, 'test_game')

test_game_second_path = os.path.join(directory_path, 'test_game_second')
