# mkdir fl
# cd fl

git clone -b master git@github.com:andrewkoff/flight_planner.git
cd flight_planner
pipenv sync
pipenv run python src/manage.py runserver