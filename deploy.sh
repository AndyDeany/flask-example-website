if [ $# == 0 ]
then
    echo "You must provide an environment"
    exit 1
fi


site=daviddean
environment=${1,,}

if [ $environment != "production" ]
then
    site=$environment-$site
fi

heroku git:remote -a $site
git push heroku master
