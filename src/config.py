import os


db_file_name = 'aflore_sqlite.db'
results_file_name = "results.xlsx"

folder_assets = os.path.join(os.path.dirname(os.path.realpath('__file__')),
                             'assets', 'data')

folder_assets_in = os.path.join(folder_assets, 'input')

folder_assets_out = os.path.join(folder_assets, 'output')

db_file_path = os.path.join(folder_assets_in, db_file_name)
output_file_path = os.path.join(folder_assets_out, results_file_name)
