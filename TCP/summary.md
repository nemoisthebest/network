# מבנה TCP

ה-TCP עוטף כל חבילת נתונים ב-header המכיל 10 שדות חובה בגודל של 20 ביטים. כל header מכיל מידע על החיבור והנתונים הנוכחיים הנשלחים.

10 שדות הכותרת של TCP הם:
<br>
יציאת מקור (Source port) - יציאת המכשיר השולח.
<br>
יציאת יעד (Destination port) - יציאת המכשיר המקבל.
<br>
מספר רצף (Sequence number) - התקן המפעיל חיבור TCP חייב לבחור מספר רצף ראשוני אקראי, אשר לאחר מכן מוגדל בהתאם למספר הבתים המשודרים.
<br>
מספר אישור (Acknowledgment number) - המכשיר המקבל שומר על מספר אישור שמתחיל באפס. הוא מגדיל את המספר הזה בהתאם למספר הבייטים שהתקבלו.
<br>
היסט נתוני TCPי* (TCP data offset) - זה מציין את גודל כותרת ה-TCP, מבוטא במילים של 32 סיביות. מילה אחת מייצגת ארבעה בתים.
<br>
נתונים שמורים (Reserved data) - השדה השמור תמיד מוגדר לאפס.
<br>
דגלי בקרה (Control flags ) - TCP משתמשת בתשעה דגלי בקרה כדי לנהל את זרימת הנתונים במצבים ספציפיים, כגון התחלת איפוס.
<br>
גודל חלון TCP checksumי* (Window size TCP checksum ) - השולח יוצר סכום ביקורת ומשדר אותו בכל כותרת מנות. המכשיר המקבל יכול להשתמש בסכום הבדיקה כדי לבדוק אם יש שגיאות בכותרת ובטעינה שהתקבלו.
<br>
מצביע דחוף (Urgent pointer) - אם מוגדר דגל בקרת URG, ערך זה מציין היסט ממספר הרצף, המציין את בייט הנתונים הדחוף האחרון.
<br>
נתונים אופציונליים mTCPי (mTCP optional data) - אלו הם שדות אופציונליים להגדרת גדלי מקטעים מקסימליים, אישורים סלקטיביים והפעלת קנה מידה חלונות לשימוש יעיל יותר ברשתות ברוחב פס גבוה.

*להתעלם מה-י, היא שם כי המילים באנגלית קופצות לסוף הסוגריים ואני לא מעוניינת בכך!! 😅🙄🤫
