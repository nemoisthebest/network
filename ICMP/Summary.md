# פרוטוקול ICMP
פרוקוטול Internet Control Message Protocol) ICMP) הוא פרוטוקול משכבת הרשת המשמש רכיבי רשת לאבחון בעיות תקשורת ברשת. ICMP משמש בעיקר כדי לקבוע אם הנתונים בפקטות מגיעים ליעדם המיועד בתזמון המיועד. בדרך כלל, פרוטוקול ICMP משמש ברכיבי רשת, כגון נתבים. ICMP חיוני לדיווח ובדיקות שגיאות, אך ניתן להשתמש בו גם בהתקפות מניעת שירות (DDoS).

### למה להשתמש בפרוטוקול ICMP?
המטרה העיקרית של ICMP היא לדווח על שגיאות. כאשר שני רכיבים מתחברים דרך האינטרנט, ה-ICMP מייצר שגיאות לשיתוף עם המכשיר השולח במקרה שאחד מהנתונים לא הגיע ליעדו. לדוגמה, אם פקטת נתונים גדולה מדי עבור ראוטר, הוא ישחרר את הפקטה וישלח הודעת ICMP בחזרה למקור של הפקטה.

שימוש נוסף בפרוטוקול ICMP הוא ביצוע אבחון רשת, הפקודות הנפוצות traceroute ו-ping פועלות באמצעות ICMP. ה-traceroute משמש להצגת נתיב הניתוב בין שני רכיבי אינטרנט. נתיב הניתוב הוא הנתיב הפיזי בפועל של נתבים מחוברים שבקשה צריכה לעבור דרכם לפני שהיא מגיעה ליעדה. בנוסף הוא מדווח גם על הזמן הנדרש לכל קפיצה בדרך בין נתב אחד לאחר. זה יכול להיות שימושי לקביעת מקומות בהם נוצר עיכוב ברשת.

ה-ping הוא גרסה פשוטה של ​​traceroute. פינג יבדוק את מהירות החיבור בין שני מכשירים וידווח בדיוק כמה זמן לוקח לפקטת נתונים להגיע ליעדה ולחזור למכשיר השולח. פינג הוא מדד שימושי מאוד למדידת ההשהיה בין שני מכשירים למרות שמספק פחות מידע מ-traceroute. 

למרבה הצער, התקפות רשת יכולות לנצל את התהליך הזה, וליצור אמצעי שיבוש כמו מתקפת ICMP flood attack ומתקפת ping of death.

### איך עובד ICMP?
פרוטוקול ICMP הוא חסר חיבור, משאומר שמכשיר אחד לא צריך לפתוח חיבור עם מכשיר אחר לפני שליחת הודעת ICMP. תעבורת IP רגילה נשלחת באמצעות TCP, כלומר כל שני התקנים שמחליפים נתונים יבצעו תחילה לחיצת יד של TCP כדי להבטיח ששני המכשירים מוכנים לקבל נתונים. ICMP לא פותח חיבור בצורה זו. פרוטוקול ICMP גם אינו מאפשר מיקוד לפורט ספציפי במכשיר.

### מהי חבילת ICMP?
חבילת ICMP היא פקטה המשתמשת בפרוטוקול ICMP. פקטות ICMP כוללות ICMP header אחרי IP header רגיל. כאשר נתב או שרת צריכים לשלוח הודעת שגיאה, תוכן הפקטה או חלק ממנו תמיד יכיל עותק של ה-IP header של החבילה שגרמה לשגיאה.
