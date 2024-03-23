cd /etc/
mkdir reknag
cd reknag
git clone https://github.com/kioydiolabs/reKnag temp_update
cd temp_update
cd server_side
cp api.py /etc/api_short/api.py
# systemctl restart reknag_api
cd ../../
rm -rf temp_update