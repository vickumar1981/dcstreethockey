# dcstreethockey

##Deploy - keeps dev and heroku in sync
1. ./manage.py makemigrations
1. ./manage.py migrate
1. git push heroku master
1. heroku run python ./manage.py migrate
1. git push origin master

##Ensure DJANGO_SETTINGS_MODULE is set for production deployments
1. heroku config:set DJANGO_SETTINGS_MODULE=dcstreethockey.settings.production

##Create backup of heroku database and restore in local postgres instance
1. heroku pg:backups:capture
1. heroku pg:backups:download
1. pg_restore --verbose --clean --no-acl --no-owner -h localhost -U user -d dcstreethockey latest.dump
1. https://devcenter.heroku.com/articles/heroku-postgres-import-export

##Import/Export CSV file to local postgres db
1. Copy data from CSV - You can specify the columns to read:
   - \copy leagues_player(first_name,last_name,email, photo) FROM '/Users/stirling/Downloads/sunday_players.csv' DELIMITER ',' CSV
1. Copy data from PostgreSQL table to csv file:
   - \copy leagues_player FROM '/Users/stirling/Downloads/sunday_players.csv' DELIMITER ',' CSV
   
##Push local database to heroku
1. Create backup! https://devcenter.heroku.com/articles/heroku-postgres-import-export 
1. DATABASE_URL=$(heroku config:get DATABASE_URL -a dcstreethockey 
1. heroku pg:reset DATABASE_URL
1. heroku pg:push dcstreethockey DATABASE_URL --app dcstreethockey
