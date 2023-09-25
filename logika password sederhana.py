def password():
    user =input("user-nya =")
    passw=input("password-nya =")
    username_from_db = "user"
    password_from_db = "admin"
    if user == username_from_db:
        if passw == password_from_db:
            print("username dan password cocok")
        else:
            print("password salah")
    else:
        print ("username tidak ditemukan")

#memanggil
password()