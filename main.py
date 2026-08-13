import json
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import requests # අලුතින් එකතු කරපු Library එක

# --- මෙන්න මේ ටික ඔයාගේ Green API විස්තර වලින් පුරවන්න ---
ID_INSTANCE = os.environ.get("ID_INSTANCE")
API_TOKEN = os.environ.get("API_TOKEN")
GROUP_ID = os.environ.get("GROUP_ID")

def send_to_whatsapp(image_path, kid_name):
    # Green API එකේ ෆොටෝ යවන URL එක
    url = f"https://api.green-api.com/waInstance{ID_INSTANCE}/sendFileByUpload/{API_TOKEN}"
    
    # මැසේජ් එකේ යටින් වැටෙන Caption එක (මෙතන ඔයාට ඕන විදිහට වෙනස් කරගන්න පුළුවන්)
    caption_text = f"🎉 අද දින උපන්දිනය සමරන අපේ බැච් එකේ {kid_name} ට සුභම සුභ උපන්දිනයක් වේවා! 🎂✨"
    
    payload = {
        'chatId': GROUP_ID,
        'caption': caption_text
    }
    
    try:
        # ෆොටෝ එක Open කරලා API එකට Upload කරනවා
        with open(image_path, 'rb') as file:
            files = {'file': (image_path, file, 'image/jpeg')}
            response = requests.post(url, data=payload, files=files)
            
        if response.status_code == 200:
            print("✅ සාර්ථකයි! WhatsApp ගෲප් එකට පෝස්ට් එක යැව්වා.")
        else:
            print(f"❌ WhatsApp යවන්න බැරි වුණා. Error: {response.text}")
    except Exception as e:
        print(f"❌ WhatsApp යවද්දී අවුලක් ගියා: {e}")

def create_birthday_post():
    today = datetime.today().strftime('%m-%d')

    try:
        with open('data.json', 'r') as file:
            students = json.load(file)
    except Exception as e:
        print(f"දත්ත කියවීමේදී දෝෂයක්: {e}")
        return

    birthday_kids = [student for student in students if student['birthday'] == today]

    if not birthday_kids:
        print("අද කාගෙවත් උපන්දිනේ නෑ!")
    else:
        for kid in birthday_kids:
            try:
                # 1. Template එක සහ ෆොටෝ එක ලෝඩ් කරගැනීම
                template = Image.open("Templates/base.png").convert("RGBA")
                photo_path = f"student_photos/{kid['photo_name']}"
                photo = Image.open(photo_path).convert("RGBA")

                draw = ImageDraw.Draw(template)

                # 2. "JULIANA SILVA" නම Seamless විදිහට වසා දැමීම
                bg_color = template.getpixel((500, 2400)) 
                draw.rectangle([(800, 2300), (2600, 2550)], fill=bg_color)

                # 3. ෆොටෝ එක Center Crop කිරීම
                size = (1415, 1415) 
                photo = ImageOps.fit(photo, size, Image.Resampling.LANCZOS)
                
                mask = Image.new('L', size, 0)
                mask_draw = ImageDraw.Draw(mask)
                mask_draw.ellipse((0, 0) + size, fill=255)
                
                # 4. රන්වන් බෝඩර් එකට ගාණටම සෙට් වෙන්න ෆොටෝ එක ඇලවීම
                template.paste(photo, (985, 865), mask)

                # 5. අලුත් නම ටයිප් කිරීම
                text_to_add = f"{kid['name'].upper()}"
                
                # 5. අලුත් නම ටයිප් කිරීම
                text_to_add = f"{kid['name'].upper()}"
                
                font = ImageFont.truetype("myfont.ttf", 180) 

                text_bbox = draw.textbbox((0, 0), text_to_add, font=font)

                # 6. අවසාන පෝස්ට් එක සේව් කරනවා
                final_image = template.convert("RGB")
                output_path = f"{kid['name']}_birthday_post.jpg"
                final_image.save(output_path, quality=95)
                print(f"පට්ට! පෝස්ට් එක සේව් වුණා: {output_path}")

                # 7. සේව් වුණාට පස්සේ WhatsApp එකට යවන Function එක Call කරනවා
                print("WhatsApp එකට යවමින් පවතී...")
                send_to_whatsapp(output_path, kid['name'])

            except Exception as e:
                print(f"අවුලක් ගියා මචන්: {e}")

if __name__ == "__main__":
    create_birthday_post()