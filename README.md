# BrawlElo
BrawlElo is a Brawl Stars ESports data analysis/statistics tool to analyze the strength of different teams. It is essentially a wrapper around [Ordo](https://github.com/michiguel/Ordo).

The data found in this repository (in the folder bs-2024-raw-main) is taken from [here](https://github.com/idouab/bsc-2024-raw).

I kind of expect there to be bugs, so please make an issue on GitHub if you happen to find one.

This was originally created as an extension of my [EMEA rankings](https://www.reddit.com/r/BrawlStarsEsports/comments/1edort7/emea_elo_rankings/) and [NA rankings](https://www.reddit.com/r/BrawlStarsEsports/comments/1edrhqw/na_elo_rankings/) reddit posts.

BrawlElo is available under the MIT License.

# Usage
Download [Ordo 1.0](https://github.com/michiguel/Ordo/releases/tag/1.0) (for windows: download `ordo-1.0-win.zip`, extract from the zip file, then drag `ordo-win64.exe` into the folder which this `README.md` is in)
Go to the `src` directory, then run `python main.py (region acronym)`

# You may wonder ...

## Why are the rankings different from the ones in the reddit posts?
I manually went onto liquipedia and got match results which I thought were relevant. I obviously did not collect all match results, while this code utilizes the full results. This may lead to ranking differences.

## Why are the elo ratings much higher than the ones in the reddit posts?
In the elo system, what's important is not the actual ratings, but the difference between the ratings. For example, if you only have 3 teams in your system which have elo ratings of 500, 700, and 900, it would be theoretically sound to also say they have elo ratings of 2400, 2600, and 2800.

Ordo automatically shifts elo ratings such that the average elo of all of the teams is 2300. Because this code uses the full match data from Monthly Qualifiers and Monthly Finals, there are more teams which are relatively bad, and so the top teams' elo is shifted upwards to keep the average elo 2300.
