# For Lab 3 Part 2
## Set up using uv (ideally)
After downloading, run `uv sync` in the `lab3_part2` directory.
Be sure to `cd` into the `lab03_part2` directory if necessary

Then you can source the venv and run the main.py script with the only arg needed being the path to the `data/languages/paragraphs` directory, e.g. :
`source .venv/bin/activate`

Or whichever shell script corresponds to your system, I use the fish shell so mine looked like this:
`source .venv/bin/activate.fish`

After that run the main.py and point to the `paragraphs` directory:
`main.py data/languages/paragraphs`

Altogether:
```
cd lab03_part2 // if necessary
uv sync && \
source .env/bin/activate && \
python main.py data/languages/paragraphs/
```