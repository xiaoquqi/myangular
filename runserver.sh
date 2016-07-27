#!/bin/bash

#
# Script to start ruler or miner for developers
#

CURRENT_PATH=$(cd $(dirname $0); pwd)

VENV_PATH=$CURRENT_PATH/.venv
#virtualenv $VENV_PATH
source $VENV_PATH/bin/activate
#pip install -r $CURRENT_PATH/requirements.txt

#RULER_CONF="$CURRENT_PATH/etc/ruler/ruler.py"
#MINER_CONF="$CURRENT_PATH/etc/miner/miner.yaml"
#
#export RULER_CONF=$RULER_CONF
#export MINER_CONF=$MINER_CONF

cd $CURRENT_PATH
if [[ $1 = "ruler" ]]; then
  echo "Starting ruler..."
  echo "python run.py"
  python run.py
elif [[ $1 = "upgrade" ]]; then
  echo "Running db upgrade..."
  cd $CURRENT_PATH/ruler/database
  python manage.py db upgrade
elif [[ $1 = "db_init" ]]; then
  echo "Running db initialization..."
  cd $CURRENT_PATH/ruler/database
  python manage.py db init
elif [[ $1 = "migrate" ]]; then
  echo "Running db migration..."
  cd $CURRENT_PATH/ruler/database
  python manage.py db migrate
else
  echo "Usage: runserver.sh [ruler|upgrade|db_init|migrate]"
  exit 1
fi
