def is_valid_email(email):
    if email.count("@") > 1:
        return False
    else:
        email = email.split("@")
        if email[0][0] == "." or email[0][len(email[0]) - 1] == ".":
            return False
        else:
            if email[1].count(".") < 1:
                return False
            else:
                email[1] = email[1].split(".")
                for part in email[1]:
                    for element in part:
                        if not ((48 <= ord(element) <= 57) or (65 <= ord(element) <= 90) or (97 <= ord(element) <= 122)):
                            return False
                return True
print(is_valid_email("maciej@student.agh.edu.pl"))