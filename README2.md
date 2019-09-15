# DOWNLOAD pre-trained and dataset v2

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1YVBGMru0dlwB8zu1OoErOazZoc8ISSJn' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1YVBGMru0dlwB8zu1OoErOazZoc8ISSJn" -O dataset.zip && rm -rf /tmp/cookies.txt


wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1aDdC4hGWXzWoECfMP9wjXnkA8Gd-ztgP' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1aDdC4hGWXzWoECfMP9wjXnkA8Gd-ztgP" -O pretrained.zip && rm -rf /tmp/cookies.txt

unzip pretrained.zip

mv model Multi-Human-Parsing/Nested_Adversarial_Networks

rm pretrained.zip

unzip dataset.zip

mv LV-MHP-v2/val/images/* LV-MHP-v2/train/images/
mv LV-MHP-v2/val/parsing_annos/* LV-MHP-v2/train/parsing_annos/
mv LV-MHP-v2/val/pose_annos/* LV-MHP-v2/train/parsing_annos/

mv LV-MHP-v2 Multi-Human-Parsing/Nested_Adversarial_Networks

cd Multi-Human-Parsing/Nested_Adversarial_Networks

 python generate_list.py
 