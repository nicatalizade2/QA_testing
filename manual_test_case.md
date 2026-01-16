# Login Page – Test Cases

## TC-01: Login with valid credentials
**Precondition:** User is on login page  
**Steps:**
1. Enter valid email
2. Enter valid password
3. Click Login  
**Expected Result:** User is redirected to dashboard

---
## TC-02: Login with invalid password
**Precondition:** User is on login page  
**Steps:**
1. Enter valid email
2. Enter wrong password
3. Click Login 

**Expected Result:** Error message "Invalid credentials" is displayed

---
## TC-03: Login with empty fields
**Steps:**
1. Leave email empty
2. Leave password empty
3. Click Login  
**Expected Result:** Validation message is shown

---
## TC-04: Password field masked
**Steps:**
1. Type password in password field  
**Expected Result:** Password is displayed as dots (****)

---

## TC-05: Remember Me checkbox
**Steps:**
1. Check "Remember Me"
2. Login successfully
3. Close and reopen browser  
**Expected Result:** User is still logged in