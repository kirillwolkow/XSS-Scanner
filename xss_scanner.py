import requests
from bs4 import BeautifulSoup


class XSSVulnScanner:
    def __init__(self):
        self.login_url = "http://localhost/login.php"
        self.url_to_scan = "http://localhost/vulnerabilities/xss_r/"
        self.js_script = "<script>alert('XSS')</script>"

    def get_token(self, source):
        soup = BeautifulSoup(source, "html.parser")
        return soup.find('input', { "type" : "hidden" })['value']

    def login(self):
        session = requests.Session()
        source = session.get(self.login_url).text
        login_payload = {
            "username"   : "admin",
            "password"   : "password",
            "Login"      : "Submit",
            "user_token" : self.get_token(source)
        }

        session.post(self.login_url, data=login_payload)
        return session.post(self.url_to_scan, data=login_payload)

    def get_first_form(self):
        try:
            response = self.login()
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, "html.parser")
            form = soup.find("form")

            if form:
                print(f"Found form on {self.url_to_scan}:\n")
                return form
            else:
                print(f"No forms found on {self.url_to_scan}")

        except requests.exceptions.RequestException as e:
                print(f"Error occurred: {e}")

    def get_form_details(self, form):
        action = form.attrs.get("action", "").lower()
        method = form.attrs.get("method", "get").lower()
        inputs = []

        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")

            inputs.append({
                "type": input_type,
                "name": input_name
            })

        details = {
            "action": action,
            "method": method,
            "inputs": inputs
        }
        return details

    def submit_form(self, form_details):
        session = requests.Session()
        self.login()
        source = session.get(self.login_url).text
        login_payload = {
            "username"   : "admin",
            "password"   : "password",
            "Login"      : "Submit",
            "user_token" : self.get_token(source)
        }

        session.post(self.login_url, data=login_payload)

        target_url = self.url_to_scan + form_details["action"]
        inputs = form_details["inputs"]
        data = {}

        for input in inputs:
            if input["type"] == "text" or input["type"] == "search":
                input["value"] = self.js_script
            input_name = input.get("name")
            input_value = input.get("value")

            if input_name and input_value:
                data[input_name] = input_value

        print(f"[+] Submitting malicious payload to {target_url}")
        print(f"[+] Data: {data}")

        if form_details["method"] == "post":
            return session.post(target_url, data=data)
        else:
            return session.get(target_url, params=data)

    def scan_xss(self):
        form = self.get_first_form()
        is_vulnerable = False
        form_details = self.get_form_details(form)
        content = self.submit_form(form_details).content.decode()

        if self.js_script in content:
            print(f"[+] XSS Detected on {self.url_to_scan}")
            print(f"[*] Form details:")
            print(form_details)
            is_vulnerable = True

        return is_vulnerable


if __name__ == "__main__":
    scanner = XSSVulnScanner()
    scanner.scan_xss()
