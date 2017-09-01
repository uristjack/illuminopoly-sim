# illuminopoly-sim
_Fiction generation through simulation of secret societies._

illuminopoly-sim is a system intended to write 50,000 words of fiction for the [2017 NaNoGenMo](https://github.com/NaNoGenMo/2017/issues/6) contest.
It will simulate a set of AIs playing _[Illuminopoly](http://www.gamecabinet.com/rules/Illuminopoly.html)_, and narrate their gameplay as a story.
To better narrate it, the story will be framed as a narration of competing factions and secret societies that are trying to control a city.
Just for simplicity, I'm going for London, and hard-coding the names for streets etc.

However, if I can be bothered, I may turn this into a graduated system.
Different factions (with randomly generated names, but the same winning criteria as in the original _Illuminopoly_) will try to control cities.
Say, 10 cities per country.
Then, the 10 winning factions in each country will perform a similar game, but country-wide rather than city-wide.
Then, 5 factions which control a country each can fight for control over a continent.
After that, the top 7 factions, which each control a full continent, can attempt to achieve world domination!
8 factions per city (1 for each kind of player in Illuminopoly), 10 winning factions per country, 5 winning factions per continent, 7 winning factions in the world.
That would be a full 2800 games that the computer would need to simulate and narrate.
And at a 50,000 word requirement, that's 18 words per game.
Which would be dreadfully boring.

Perhaps there could be a whole set of fiction - 7 in total, one for each continent...

Of course, this would require some reworking in terms of naming - probably using JSON files or something.
It would also require some basic number alterations - factions are going to be playing with lots more money the higher up in the chain they go.
 
