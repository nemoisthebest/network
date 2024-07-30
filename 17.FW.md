# חומת אש 🔥🧱🔥🧱🔥🧱


חומת האש (Firewall - FW) היא התקן אבטחת רשת המנטר את תעבורת הרשת הנכנסת והיוצאת ומחליט אם לאפשר או לחסום תעבורה ספציפית בהתבסס על מערכת מוגדרת של כללי אבטחה.

חומת אש יכולה להיות חומרה, תוכנה, תוכנה כשירות (SaaS), ענן ציבורי או ענן פרטי (וירטואלי). 

לחומת האש שני מצבים עיקריים: stateful ו-stateless.

![image](https://github.com/user-attachments/assets/93e87ef5-f502-4e06-819b-83f74b464edb)

## הראשון Stateful Firewall (FW)
במצב זה חומת האש ממוקמת בין הרשת הפנימית של הארגון לרשת החיצונית (לדוגמה, האינטרנט). היא מסוגל לנתח תעבורת רשת ברמה של חיבורים (connections) ולעקוב אחרי מצב החיבור בזמן אמת. ניתן להשתמש בחומת אש זו בקצה הרשת או בפנים.

ה-FW ה-stateful מתייחס לתעבורה בהתבסס על מצב החיבור בו היא מגיעה, כלומר על פי מידע על החיבור כולל כתובות IP, פורטים, ומצב החיבור (כמו מצב הסנכרון שלו, סוג הפרוטוקול של החיבור, וכדומה).
 
לחומת האש יכולת מעקב אחר מצב החיבור, דבר המבטיח שה-FW יכול להחליט על במהירות וביעילות אם לאפשר או לחסום פעולות בהתאם לכללים המוגדרים. כמו כן, חומת האש יכולה לעקוב אחר אופן התנהגות הנתונים, ולקטלג דפוסי התנהגות.

![image](https://github.com/user-attachments/assets/019789d3-a8ee-481c-b3fb-1dddfc795015)

## השני Stateless Firewall (FW)
 
גם כאן, המיקום הוא בין רשת פנימית לרשת חיצונית.
 
ה-FW ה-stateless לא נותן דגש על מצב החיבור אלא על הפרטים הסטטיים של כל פאקטת תעבורה, כמו כתובת IP מקור ויעד, פורטים, ואולי סוג הפרוטוקול.

פילטר ה-stateless יכול לאפשר או לחסום תעבורת בהתאם לכללים שהוגדרו, אך אינו יכול לקחת בחשבון את ההיסטוריה של החיבור או מצבו הנוכחי. חומות אש אלו מדינה עושות שימוש במקור, יעד ופרמטרים אחרים של פאקטת נתונים כדי להבין אם הנתונים מהווים איום.

![image](https://github.com/user-attachments/assets/444cc940-d7ca-4257-a021-54464f87bcc1)

### הבדלים
ההבדל העיקרי בין stateful Firewall ו-stateless Firewall הוא ביכולת ה-stateful לנהל ולסנן תעבורת רשת באופן ממוקד על פי מצב החיבורים הפעילים, בעוד שה-stateless מתמקד בנתונים סטטיים בלבד בכדי לקבוע האם להתיר או לחסום תעבורת.

ארגונים קטנים יעדיפו את ה-stateless מאחר והם יעדיפו את ה-FW לצורך סבירות. זאת בגלל שבטח תהיה פחות תעבורה נכנסת לעומת בארגון גדול וייתכנו גם פחות איומים. 

עבור ארגונים גדולים יותר,stateful הוא הבחירה הטובה ביותר. מכיוון והוא מציע סינון מנות דינמי, הם יכולים להסתגל למגוון איומים באמצעות נתונים שנאספו מפעילויות קודמת ברשת כדי לברר את רמת הסכנה של איומים חדשים.

![image](https://github.com/user-attachments/assets/6ae8e265-0857-4b2d-a805-958db05457e3)

