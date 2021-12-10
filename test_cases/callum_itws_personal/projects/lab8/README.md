# ITWS 1100 Lab 8

In this lab we set up XAMPP and did some practice with XSS attacks. I had no issues with XAMPP, and had some fun messing around with XSS attack stuff. This lab helped me understand how an XSS attack might lead to user privacy breaches and security issues.

## Part 3: Understanding of XSS Attack

From what I understand, what my code does is access the current URL of the browser window, and changes it to <http://www.rpi.edu>. This effectively causes a redirect and the browser reloads <http://www.rpi.edu> instead of submitting the form on `lab8.html`.

### Code

`change the href of the browser window <script>window.location.href = "http://www.rpi.edu";</script>`

## [Link to GitHub](https://github.com/callumhauber/ITWS-1100)

## Sources

* <https://www.w3schools.com/js/js_window_location.asp>
