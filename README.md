# Genshin Impact DPS Framelist Calculation

This repository houses the code for a character database, as well as
configurable DPS calculator for team composition and real-time DPS analysis.

# Characters

Characters are all subclass definitions of a parent class `CharacterAbstract`.
Since every character has this same base stats screen, their data all follows
this form.

Given a max level and a current level parameter passed in, character data is
filled in based on database readout. For simplicity's sake, character levels are
smoothed to the extrema - If a character is 18/20, they will have stats of a
character level 20/20. If a character is 20/40, they will stay at 20/40, or 20+.

# License TL;DR

This project is distributed under the MIT license. This is a paraphrasing of a
[short summary](https://tldrlegal.com/license/mit-license).

This license is a short, permissive software license. Basically, you can do
whatever you want with this software, as long as you include the original
copyright and license notice in any copy of this software/source.

## What you CAN do:

-   You may commercially use this project in any way, and profit off it or the
    code included in any way;
-   You may modify or make changes to this project in any way;
-   You may distribute this project, the compiled code, or its source in any
    way;
-   You may incorporate this work into something that has a more restrictive
    license in any way;
-   And you may use the work for private use.

## What you CANNOT do:

-   You may not hold me (the author) liable for anything that happens to this
    code as well as anything that this code accomplishes. The work is provided
    as-is.

## What you MUST do:

-   You must include the copyright notice in all copies or substantial uses of
    the work;
-   You must include the license notice in all copies or substantial uses of the
    work.

If you're feeling generous, give credit to me somewhere in your projects.
