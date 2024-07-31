# מבנה TCP

ה-TCP עוטף כל חבילת נתונים ב-header המכיל 11 שדות חובה בגודל של 20-60 ביטים. כל header מכיל מידע על החיבור והנתונים הנוכחיים הנשלחים.

11 שדות הכותרת של TCP הם:
<br>
פורט מקור (Source port) - הפורט של המכשיר השולח. 16 ביטים.
<br>
פורט יעד (Destination port) - הפורט של המכשיר המקבל. 16 ביטים.
<br>
מספר רצף (Sequence number) - התקן המפעיל של חיבור ה-TCP חייב לבחור מספר רצף ראשוני אקראי, אשר לאחר מכן מוגדל בהתאם למספר הבטים המשודרים. 32 ביטים.
<br>
מספר אישור (Acknowledgment number) - המכשיר המקבל שומר על מספר אישור שמתחיל באפס. הוא מגדיל את המספר הזה בהתאם למספר הבייטים שהתקבלו. 32 ביטים.
<br>
אורך ה-headerי (Header Length (HLEN)) - זה מציין את גודל header ה-TCP, מבוטא במילים של 32 סיביות. מילה אחת מייצגת ארבעה בטים. 4 ביטים.
<br>
נתונים שמורים (Reserved data) - השדה של הרזרווה תמיד מוגדר כאפס. 6 ביטים.
<br>
דגלי בקרה (Control flags) - TCP משתמשת בתשעה דגלי בקרה כדי לנהל את זרימת הנתונים במצבים ספציפיים, כגון התחלת איפוס. 8 ביטים. באיור המצורף מופיע כ-URG, ACK, PSH, RST, SYN, FIN שאלה הם הפונקציות שיש לדגלי הבקרה.
<br>
גודל חלון (Window size) - שדה זה מציין את גודל החלון של ה-TCP השולח בביטים. 16 ביטים.
<br>
סיכום בדיקה (Checksum) - שדה זה מכיל את סיכום הבדיקה לבקרת שגיאות. זה חובה ב-TCP בניגוד ל-UDP. 16 ביטים.
<br>
מצביע נחוץ (Urgent pointer) - אם מוגדר דגל בקרת URG, ערך זה מציין offset ממספר הרצף, המציין את בייט הנתונים הנחוץ האחרון. 16 ביטים.
<br>
נתונים אופציונליים mTCPי (mTCP optional data) - אלו הם שדות אופציונליים להגדרת גדלי מקטעים מקסימליים, אישורים סלקטיביים והפעלת קנה מידה חלונות לשימוש יעיל יותר ברשתות ברוחב פס גבוה. 0-320 ביטים בקבוצות של 32 ביטים.

*להתעלם מה-י, היא שם כי המילים באנגלית קופצות לסוף הסוגריים ואני לא מעוניינת בכך!! 😅🙄🤫
 <div align="center">
   
   ![image](https://github.com/user-attachments/assets/f2580e0f-8660-4a6f-8acb-385c5193a7ba)

</div>
