# חומת אש 🔥🧱🔥🧱🔥🧱


חומת האש (Firewall - FW) היא מערכת אבטחה שמטרתה לשלוט בתנועת התקשורת בין רשתות שונות, ולסנן את התקשורת על פי כללים מוגדרים מראש. לחומת האש שני מצבים עיקריים: stateful ו-stateless.

## הראשון Stateful Firewall (FW)
   - **מיקום ברשת**: ממוקם בין הרשת הפנימית של הארגון לרשת החיצונית (לדוגמה, האינטרנט). הוא מסוגל לנתח תעבורת רשת ברמה של חיבורים (connections) ולעקוב אחרי מצב החיבור בזמן אמיתי.
   - **מיקוד ברכיב**: ה-FW ה-stateful מתייחס לתעבורה בהתבסס על מצב החיבור בו היא מגיעה, כלומר על פי מידע על החיבור כולל כתובות IP, פורטים, ומצב החיבור (כמו מצב הסנכרון שלו, סוג הפרוטוקול של החיבור, וכדומה).
   - **תכונות**: יכולת לעקוב אחרי מצב החיבור מבטיחה שה-FW יכול להחליט על הכרעה במהירות וביעילות אם לאפשר או לחסום פעולות בהתאם לכללים המוגדרים.

## השני Stateless Firewall (FW)
   - **מיקום ברשת**: גם כאן, המיקום הוא בין רשת פנימית לרשת חיצונית.
   - **מיקוד ברכיב**: ה-FW ה-stateless לא נותן דגש על מצב החיבור אלא על הפרטים הסטטיים של כל חבילת תעבורה, כמו כתובת IP מקור ויעד, פורטים, ואולי סוג הפרוטוקול.
   - **תכונות**: הפילטר ה-stateless יכול לאפשר או לחסום תעבורת בהתאם לכללים שהוגדרו, אך אינו יכול לקחת בחשבון את ההיסטוריה של החיבור או מצבו הנוכחי.

בסיכום, ההבדל העיקרי בין stateful ו-stateless Firewall הוא ביכולת ה-stateful לנהל ולסנן תעבורת רשת באופן ממוקד על פי מצב החיבורים הפעילים, בעוד שה-stateless מתמקד בנתונים סטטיים בלבד בכדי לקבוע האם להתיר או לחסום תעבורת.
