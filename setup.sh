#!/bin/bash

GTDDIR=~/gtd
CONFIGDIR=~/.config

mkdir -p "${CONFIGDIR}/gtd"
mkdir -p "${GTDDIR}/tickler/repeating"
mkdir -p "${GTDDIR}/tickler/Projects"
mkdir -p "${GTDDIR}/tickler/Completed"
mkdir -p ~/bin

cat > "${CONFIGDIR}/gtd/config" << EOF
GTDDIR=${GTDDIR}
EOF

cp nexactions project tick ~/bin
cp insert_entry.py update_repeating.sh "${GTDDIR}/tickler/"

for month in january february march april may june july august september \
	october november december; do
	touch "${GTDDIR}/tickler/$month"
done

touch "${GTDDIR}/next_actions.otl"
touch "${GTDDIR}/done.otl"

cat > "${GTDDIR}/tickler/repeating/bills" << EOF
# Rules for inserting entries into the tickler files
# happen here
# For instance:
# Pay rent on first of month
D 1 Pay rent

# Look over all GTD projects on Tuesdays:
W Tuesday 3pm 4pm Look over GTD Projects (p list)

# File taxes on April 5
A April 5 Pay taxes
EOF

cat >> ~/.bashrc << EOF
alias p=project
[ -e $HOME/gtd_bash_completion ] && . $HOME/gtd_bash_completion
EOF

cp gtd_bash_completion $HOME/gtd_bash_completion

echo "GTD is setup.  You may need to add ~/bin to your PATH"
echo "Manage GTD projects with ~/bin/project (alias 'p')"
echo "Use 'tick' to view today's tickler files"
echo "See http://github.com/hallyn/gtdtools for more information"
