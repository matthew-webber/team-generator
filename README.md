# team-generator
Create randomized teams given a list of names for games, parties, events, etc.

***Works great on [Pythonista](http://omz-software.com/pythonista/)!***

## Getting Started

### Setup

Simply clone the repo and edit the Players.txt to include the name of all potential participants.

If a participant is sitting a game out, place an 'x' before their name and they will not be added to a team.

```text
John
Jane
xJacob <== inactive player
Jean
```

### Using team-generator
Once all players are accounted for:

```shell
python FieldDay.py
```

### Team sizes

Pick teams of 2 or splitting teams right down the middle entering '2' or 's' respectively.

A random team name pulled from TeamNames.txt will be assigned to each team for added fun.

```text
Team size?
s
Team The Frontline -- ['Brandon', 'Karamie', 'Molly', 'Jeramy', 'Chelsea', 'Kayla']
Team Terminators -- ['Alan', 'Tori', 'Kelsey', 'Matt', 'Ethan', 'Cassie']
To go again just hit enter, anything else to quit
```