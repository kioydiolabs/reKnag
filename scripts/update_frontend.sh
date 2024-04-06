cd /etc/
if [ -d "reknag" ]; then
    continue
else
    mkdir reknag
fi
cd reknag
git clone https://github.com/kioydiolabs/reKnag temp_update
cd ./temp_update/web-frontend
cp ./index.html /var/www/html/index.html
cp ./index.js /var/www/html/index.js
cp ./style.css /var/www/html/style.css
cd ../../
rm -rf temp_update
echo "Frontend updated successfully to latest version"