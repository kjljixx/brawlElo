# BrawlElo
BrawlElo is a Brawl Stars ESports data analysis/statistics tool to analyze the strength of different teams. It is essentially a wrapper around [Ordo](https://github.com/michiguel/Ordo).

The data used is taken from [here](https://github.com/idouab/bsc-2025-raw).

I kind of expect there to be bugs, so please make an issue on GitHub if you happen to find one.

This was originally created as an extension of my [EMEA rankings](https://www.reddit.com/r/BrawlStarsEsports/comments/1edort7/emea_elo_rankings/) and [NA rankings](https://www.reddit.com/r/BrawlStarsEsports/comments/1edrhqw/na_elo_rankings/) reddit posts.

BrawlElo is available under the MIT License.

# Usage
Download [Ordo 1.0](https://github.com/michiguel/Ordo/releases/tag/1.0) (for windows: download `ordo-1.0-win.zip`, extract from the zip file, then drag `ordo-win64.exe` into the folder which this `README.md` is in)
Go to the `src` directory, then run `python main.py (region acronym)`

# About the Elo System
In the elo system, what's important is not the actual ratings, but the difference between the ratings. For example, if you only have 3 teams in your system which have elo ratings of 500, 700, and 900, it would be theoretically sound to also say they have elo ratings of 2400, 2600, and 2800.

**A 200 elo difference means about a ~76% chance for the higher elo team to win a game against the lower elo team.** Using some basic probability calculations, this means that the same 200 elo difference also corresponds to a ~85% chance for the higher elo team to win a set and a ~98% chance to win a best-of-5-sets series. Below is a table of various different elo difference values and corresponding probabilities for game wins, set wins, and Bo5 set wins.
|Elo Diff|Game Win|Set Win|Bo5 Win|
|--------|--------|-------|-------|
|20|53%|54%|58%|
|40|56%|58%|65%|
|60|58%|62%|72%|
|80|61%|66%|78%|
|100|64%|70%|84%|
|120|66%|74%|88%|
|140|69%|77%|92%|
|160|71%|80%|94%|
|180|74%|83%|96%|
|200|76%|85%|98%|

Ordo automatically shifts elo ratings such that the average elo of all of the teams is 2300. Because this code uses the full match data from Monthly Qualifiers and Monthly Finals, there are more teams which are relatively bad, and so the top teams' elo is shifted upwards to keep the average elo 2300.

Note that because of this, **elo between regions is not directly comparable**.
