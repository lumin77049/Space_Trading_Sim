# Space Trading Sim

Basically I want to re-create the economy system out of No Man's Sky or Elite
(1984) and allow for inter-system trading. I also want to implement different
types of trading ships and use wireframe models to represent them (similar to
Elite).

# Development considerations

ok, so for now I'm storing all my game data as a series of python objects. This
seems... ill-advised. SO, im going to *consider* writing all the game/player
data into a json file or something similar; possibly a custom file format if
that isn't *too* hard.
