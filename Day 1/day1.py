'''Import the re module'''
import re
    
'''Check if the password is strong or weak using regular expressions and print the result'''
def check_password_strength(password):
    score = 0
    strong_pattern =  r"(?=.*[A-Z])(?=.*[!@#$&*])(?=.*[0-9])(?=.*[a-z]).{8}"
    weak_pattern = r'(?=.*[a-z])(?=.*[0-9])'
    result = re.search(strong_pattern, password)
    result_weak = re.search(weak_pattern, password)
    if bool(result):
        score += 5
        print("Password Strength: You have a strong password")
    if bool(result_weak):
        score += 2
        print("Password Strength: You have a weak password")

'''Main function'''
def main():
    '''Ask the user to enter a password and store it in a variable called passwd'''
    passwd = input("Enter your password: ")
    check_password_strength(passwd)
    
__name__ == '__main__'
main()