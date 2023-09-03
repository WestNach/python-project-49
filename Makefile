install:
		poetry install

brain-game:
		poetry run brain-games

brain-even:
	    poetry run brain-even

build:
		poetry build
		

publish:
		poetry publish --dry-run
		

package-instlall:
		python3 -m pip install --user dist/*.whl

package-reinstall:
	    python3 -m pip install --user --force-reinstall dist/*.whl	

lint:
	    poetry run flake8 brain_games
