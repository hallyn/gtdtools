# GTD scripts

## Introduction

I've been using GTD for over a decade.  I've been developing and using
these scripts for almost as long.

If you run setup.sh from this directory, it will by default setup;

1. ~/gtd as a base directory for the GTD files
1. ~/gtd/tickler as the tickler directory
1. ~/gtd/Projects as the project directory, and ~/gtd/Completed as the completed project directory
1. ~/gtd/next_actions.otl as the (vimoutliner) next actions file
1. ~/gtd/done.otl as the (vimoutliner) done file
1. ~/bin/update_repeating as the script to update the tickler files each month
1. ~/bin/tick as the script to run each day to view your daily tickler files
1. ~/bin/project (alias p) as the script to manage projects

As I find time, I'll add more detailed information below.

## Tickler

A tickler file is machination to help you remember periodic tasks.
For instance,

1. On a certain date each month you should pay rent
2. On a certain day each week you should water the lawn
3. On Tuesday and Thursday you should mail progress reports to your boss
4. The 15th of February you should pay annual insurance

The tickler scripts in gtdtools are designed to help you remember those.
You'll have a 'tickler' directory, usually ~/gtd/tickler.  Under that,
will be

1. A file for each possible date of the month (01-31)
2. A file for each month
3. A 'repeating' directory which is the source of information for the daily and monthly files

On the first of each month, you will

1. Go through this month's monthly file, and copy the information to the relevant dates.
2. Run the script `~/gtd/tickler/update_repeating` script to apply the information under ~/gtd/tickler/repeating to the daily files

For instance, on the 20th of February you may have noticed that during the next month you'll need to refill some account.  You quickly write a note under ~/gtd/tickler/march to that effect.  Then on March 1,  you move that information from `march` to `10` to remember on the 10th to do that.

Meanwhile `~/gtd/tickler/repeating/general.r` has entries:

```
D 10 pay loan
A March 15 Mom's birthday
```

When you run `~/gtd/tickler/update_repeating`, these will be copied to the `10` and `15` daily files.

Now, every morning you run the script `tick` to open the current day's daily file alongside `~/gtd/next_actions.otl`, to copy actions into next actions (or, move them to a different date, move them elsewhere, or just delete them).

## GTD

GTD is in my opinion an excellent workflow for managing projects and information.
It is designed to at the same time never lose any information or lose track of
any task, and to never be stressed about whether you are working on the wrong thing
or forgetting something.

This repo provides tools which help me use GTD.  It is not a how-to guide for using
GTD.  If you want to learn more, I highly recommend reading the book.  (Check your
local library)

## Project

GTD is often used "physically" - using paper and folders.  When used this way, you
might have one folder for each project you are working on.  All information for that
projects goes into that folder.  Then you  have a separate 'next actions' paper or
folder where you only write the very next action to be done for projects.  (The idea
is, if you see "I have to replace the car window motor" you may hesitate;  if you
see that the next step is to walk to the car and get the VIN number before
ordering the motor, then you don't need to think through steps, and you might do it)

The 'project' script here is designed to help (me) use this.  The goal is for nothing
to stand in the way of my keeping organized, so shortcuts are in order:

```
$ p l
Project                                 |  Last updated
gtdtools                                |  Dec 28 10:51:10 2017
$ p new car_window
$ p e car_window
# An editor pops up with three files under ~/gtd/Projects/car_window/
# ("p s car_window" would be a shortcut for "p n car_window; p e car_window")
$ p co<tab> ca<tab>    # moves car_window to the Completed folder
```
