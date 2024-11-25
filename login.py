import sqlite3


r = sqlite3.connect('tutorial.db')
c = r.cursor()

user_value = int(input("Pentru sign up tasteaza 0, pentru login apasa 1: "))

if user_value == 0:
    user_email = input("Introduce-ti emailul dvs: ")
    if '@' in user_email:
        c.execute(f"SELECT email FROM Login WHERE email = '{user_email}'")
        db_email = c.fetchone()
        if db_email:
            print("Emailul introd exista deja in baza de date! Va rugam selectati alt email")
        else:
            user_password = input("Introdu parola ta: ")
            c.execute(f"INSERT INTO Login (email, password) VALUES ('{user_email}', '{user_password}')")
            r.commit()
            print("Contul a fost creat. Va puteti Loga.")
    else:
        print("Nu ati introdus un email valabil!")

elif user_value == 1:
    user_email = input("Introduce-ti emailul dvs: ")
    if '@' in user_email:
        c.execute(f"SELECT email FROM Login WHERE email = '{user_email}'")
        db_email = c.fetchone()
        if not db_email:
            print("Nu ai un cont pe acest email.")
        else:
            user_password = input("Introdu parola ta: ")
            c.execute(f"SELECT password FROM Login WHERE email = '{user_email}'")
            db_password = c.fetchone()
            #print(db_password)
            if user_password == db_password[0]:
                print("Felicitari te-ai logat cu succes!")
            else:
                print("Parola introdusa nu este corecta")
    else:
        print("Nu ati introdus un email valabil!")

else:
    print("Nu ai selectat 0 sau 1, te rog selecteaza 0 sau 1!")