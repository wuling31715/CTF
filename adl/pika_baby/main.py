# http://140.115.59.7:12002/login.php?user=pikachu&pass=s214587387a
# view-source:http://140.115.59.7:12002/login.php.back

user = "pikachu"
password = "s214587387a"

print("user: {}".format(user))
print("pass: {}".format(password))

# <?php
#     $flag = "adlctf{pika_pika_pikachu}";
#     $user = $_GET['user'];
#     $pass = $_GET['pass'];
#     if (!isset($user) || !isset($pass)) {
#         header('Location', "./secret.html");
#     } else {
#         if ($user == "pikachu" && md5($pass) == "0e481756596645574257920728035178") {
#             $text = $flag;
#         } else {
#             $text = "PIKA PIKA.";
#         }
#     }
# ?>