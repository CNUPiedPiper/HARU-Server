geo_data="./src/GeoLiteCity.dat"
if [ -f "$geo_data" ]
then
    echo "$geo_data already exist."
else
    cd src
    curl -O http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
    gzip -d GeoLiteCity.dat.gz
    cd ..
fi