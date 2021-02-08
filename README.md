# Genshin Impact DPS Framelist Calculation

This repository houses the code for a character database, as well as
configurable DPS calculator for team composition and real-time DPS analysis.

# Broad overview

The goal of this application is to lay out a set of frames in a large 2D array,
sort of like a timeline in video editing softwares. Each x-index of this
timeline array will be an in-game rendered frame; Each y-index of this timeline
array will be some new motion.

Once the entire laid out set of frames is designed from left to right, a
calculation sweeps from left to right, overlaying the frames together, and
calculating any damage outputs.

In order to ensure proper interactions between characters and objects, every
object on the timeline has a context value which is exported to other objects
surrounding it. Context attributes tell the calculator how the specific object
interacts with other objects. For instance, Chongyun's E field will have a
context `infusion` on it, which states to the calculator that the E field
infuses normal combos with a certain damage type.

Each character in the list of characters has individual motion object
definitions. When that character exports a certain motion to the frame, that
motion appears on the framelist as an object with a counter and a maximum value,
as well as values for all the hitmarks.

Say, for instance, at frame t=0 Zhongli exports his turret (which lasts for 1800
frames, and ticks every 120 frames.) This turret will pad frames t=0 through
t=119 with the turret object. Each of these objects will have a
`context: turret` attribute. However, when the calculator passes over these
turret objects, since the current counter value of the instance is not equal to
a scalar multiple of the turret's activation value (in this case, 120), no
damage tick will be provided. It is only when the turret's activation value is
equivalent to a scalar of the counter that a damage tick occurs.

When a damage tick occurs, it occurs based on hitmarks. That is to say, when a
motion deals damage, it deals damage based on the current state of the timeline
when the damage tick is emit. Say a normal combo rotation occurs over 140
frames. Instead of doing damage all at once at the end of that 140 frame period,
damage is output in specific hitmarks and frame-counted to occur at these times.
Because of this, if an infusion effect on the field dissipates or a buff
dissipates, this calculator will better represent that change.

# Input parsing

In order to better control the calculation, the frame setup module is instructed
what combos to utilize beforehand. An input string controls this. For example,
let's assume that our team consists of three characters: Zhongli, Xingqiu, and
Qiqi. If the following string is passed in:

`n5js3es2e(e)qs1`

The machine will first split this into portions as follows:

`n5j s3 e s2 e(e)q s1`

Then, the machine will read this string as the following combo:

```md
Starting on Zhongli:

1. Perform a normal 5-hit jump combo.
2. Swap to Qiqi (slot 3).
3. Use elemental skill (E).
4. Swap to Xingqiu (slot 2).
5. Use elemental skill.
6. If elemental skill is off cooldown, use elemental skill.
7. Then, use elemental burst.
8. Swap back to Zhongli.

Repeat.
```

This pseudo-language will encode combos for simplicity of programming and
reprogramming interactions with team compositions.

## Table of input parsed symbols

The following is a complete table of input symbols.

| Symbol  | Description                                                |
| ------- | ---------------------------------------------------------- |
| `n<x>j` | Perform a normal <x> hit combo, with jump cancel.          |
| `n<x>d` | Perform a normal <x> hit combo, with dash cancel.          |
| `n<x>c` | Perform a normal <x> hit combo, with charge attack cancel. |
| `c`     | Perform a charge attack.                                   |
| `e`     | Perform an elemental skill.                                |
| `q`     | Perform an elemental burst.                                |
| `s<x>`  | Swap to the character in slot <x>.                         |

There are also conditional operators.

| Operator | Description                                                               |
| -------- | ------------------------------------------------------------------------- |
| `()`     | If the cooldown of the action within this is 0, then perform this action. |

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
